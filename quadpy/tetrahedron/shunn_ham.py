# -*- coding: utf-8 -*-
#
from .helpers import untangle2


class ShunnHam(object):
    """
    Lee Shunn, Frank Ham,
    Symmetric quadrature rules for tetrahedra based on a cubic close-packed
    lattice arrangement,
    Journal of Computational and Applied Mathematics,
    2012,
    <https://doi.org/10.1016/j.cam.2012.03.032>.

    Abstract:
    A family of quadrature rules for integration over tetrahedral volumes is
    developed. The underlying structure of the rules is based on the cubic
    close-packed (CCP) lattice arrangement using 1, 4, 10, 20, 35, and 56
    quadrature points. The rules are characterized by rapid convergence,
    positive weights, and symmetry. Each rule is an optimal approximation in
    the sense that lower-order terms have zero contribution to the truncation
    error and the leading-order error term is minimized. Quadrature formulas up
    to order 9 are presented with relevant numerical examples.
    """

    def __init__(self, index):
        if index == 1:
            self.degree = 1
            data = {"s4": [[1.0]]}
        elif index == 2:
            self.degree = 2
            data = {"s31": [[0.25, 0.1381966011250110]]}
        elif index == 3:
            self.degree = 3
            data = {
                "s31": [[0.0476331348432089, 0.0738349017262234]],
                "s22": [[0.1349112434378610, 0.0937556561159491]],
            }
        elif index == 4:
            self.degree = 5
            data = {
                "s31": [
                    [0.0070670747944695, 0.0323525947272439],
                    [0.1019369182898680, 0.3097693042728620],
                ],
                "s211": [[0.0469986689718877, 0.0603604415251421, 0.2626825838877790]],
            }
        elif index == 5:
            self.degree = 6
            data = {
                "s4": [[0.0931745731195340]],
                "s31": [[0.0021900463965388, 0.0267367755543735]],
                "s22": [[0.0250305395686746, 0.0452454000155172]],
                "s211": [
                    [0.0143395670177665, 0.0391022406356488, 0.7477598884818090],
                    [0.0479839333057554, 0.2232010379623150, 0.0504792790607720],
                ],
            }
        else:
            assert index == 6
            self.degree = 8
            data = {
                "s31": [
                    [0.0010373112336140, 0.0149520651530592],
                    [0.0366291366405108, 0.1344783347929940],
                ],
                "s211": [
                    [0.0096016645399480, 0.0340960211962615, 0.1518319491659370],
                    [0.0164493976798232, 0.0462051504150017, 0.5526556431060170],
                    [0.0153747766513310, 0.2281904610687610, 0.0055147549744775],
                    [0.0293520118375230, 0.3523052600879940, 0.0992057202494530],
                ],
            }

        self.bary, self.weights = untangle2(data)

        self.points = self.bary[:, 1:]
        return
