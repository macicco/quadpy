# -*- coding: utf-8 -*-
#
import matplotlib.pyplot as plt
import numpy
import orthopy

from .dunavant import Dunavant

from .helpers import _s3, _s21, _s111ab, _rot_ab
from .. import helpers
from ..nsimplex import transform, get_vol, integrate


def show(*args, **kwargs):
    plot(*args, **kwargs)
    plt.show()
    return


def plot(
        scheme,
        triangle=numpy.array([
            [-0.5, 0.0],
            [+0.5, 0.0],
            [0, 0.5 * (numpy.sqrt(3))],
            ]),
        show_axes=False
        ):
    '''Shows the quadrature points on a given triangle. The size of the circles
    around the points coincides with their weights.
    '''
    plt.plot(triangle[:, 0], triangle[:, 1], '-k')
    plt.plot(
        [triangle[-1, 0], triangle[0, 0]],
        [triangle[-1, 1], triangle[0, 1]],
        '-k'
        )

    if not show_axes:
        plt.gca().set_axis_off()

    transformed_pts = transform(scheme.points.T, triangle.T).T

    vol = get_vol(triangle)
    helpers.plot_disks(
        plt, transformed_pts, scheme.weights, vol
        )

    plt.axis('equal')
    return


def _numpy_all_except(a, axis=-1):
    axes = numpy.arange(a.ndim)
    axes = numpy.delete(axes, axis)
    return numpy.all(a, axis=tuple(axes))


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def integrate_adaptive(
        f, triangles, eps,
        minimum_triangle_area=None,
        scheme1=Dunavant(5),
        scheme2=Dunavant(10),
        sumfun=helpers.kahan_sum
        ):
    triangles = numpy.array(triangles)
    if len(triangles.shape) == 2:
        # add dimension in the second-to-last place
        triangles = numpy.expand_dims(triangles, -2)

    areas = get_vol(triangles)
    total_area = sumfun(areas)

    if minimum_triangle_area is None:
        minimum_triangle_area = total_area * 0.25**10

    val1 = integrate(f, triangles, scheme1, sumfun=sumfun)
    val2 = integrate(f, triangles, scheme2, sumfun=sumfun)
    error_estimate = abs(val1 - val2)

    # Mark intervals with acceptable approximations. For this, take all()
    # across every dimension except the last one, which is the interval index.
    is_good = _numpy_all_except(
            error_estimate < eps * areas / total_area,
            axis=-1
            )

    # add values from good intervals to sum
    quad_sum = sumfun(val1[..., is_good], axis=-1)
    global_error_estimate = sumfun(error_estimate[..., is_good], axis=-1)

    is_bad = numpy.logical_not(is_good)
    while any(is_bad):
        # split the bad triangles into four #triforce
        #
        #         /\
        #        /__\
        #       /\  /\
        #      /__\/__\
        #
        triangles = triangles[..., is_bad, :]
        midpoints = [
            0.5 * (triangles[1] + triangles[2]),
            0.5 * (triangles[2] + triangles[0]),
            0.5 * (triangles[0] + triangles[1]),
            ]
        triangles = numpy.array([
            numpy.concatenate([
                triangles[0], triangles[1], triangles[2], midpoints[0]
                ]),
            numpy.concatenate([
                midpoints[1], midpoints[2], midpoints[0], midpoints[1]
                ]),
            numpy.concatenate([
                midpoints[2], midpoints[0], midpoints[1], midpoints[2]
                ]),
            ])
        areas = get_vol(triangles)
        assert all(areas > minimum_triangle_area)

        # compute values and error estimates for the new intervals
        val1 = integrate(f, triangles, scheme1, sumfun=sumfun)
        val2 = integrate(f, triangles, scheme2, sumfun=sumfun)
        error_estimate = abs(val1 - val2)

        # mark good intervals, gather values and error estimates
        is_good = _numpy_all_except(
                error_estimate < eps * areas / total_area,
                axis=-1
                )
        # add values from good intervals to sum
        quad_sum += sumfun(val1[..., is_good], axis=-1)
        global_error_estimate += sumfun(error_estimate[..., is_good], axis=-1)
        is_bad = numpy.logical_not(is_good)

    return quad_sum, global_error_estimate


def compute_weights(scheme):
    '''Computes weights from points for a given scheme. Useful for
    cross-checking scheme integrity.
    '''
    def eval_orthopolys(bary):
        return numpy.concatenate(
            orthopy.triangle.orth_tree(scheme.degree, bary, 'normal')
            )

    fun = eval_orthopolys

    a_data = []
    if 's3' in scheme.data:
        a_data.append(fun(_s3().T))

    if 's2' in scheme.data:
        d = numpy.array(scheme.data['s2']).T
        s2_data = _s21(d[1])
        a_data.append(numpy.sum(fun(s2_data), axis=1))

    if 's1' in scheme.data:
        d = numpy.array(scheme.data['s1']).T
        s1_data = _s111ab(*d[1:])
        a_data.append(numpy.sum(fun(s1_data), axis=1))

    if 'rot' in scheme.data:
        d = numpy.array(scheme.data['rot']).T
        rot_data = _rot_ab(*d[1:])
        a_data.append(numpy.sum(fun(rot_data), axis=1))

    A = numpy.column_stack(a_data)

    exact_vals = numpy.zeros(len(A))
    exact_vals[0] = numpy.sqrt(2) / 2

    return numpy.linalg.lstsq(A, exact_vals)