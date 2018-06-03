# -*- coding: utf-8 -*-
#
from __future__ import division

from ..helpers import untangle, fsd, z


class Stenger(object):
    """
    Review: Tabulation of Certain Fully Symmetric Numerical Integration
    Formulas of Degree 7, 9 and 11 by Frank Stenger,
    Mathematics of Computation,
    Vol. 25, No. 116 (Oct., 1971), pp. 935+s58-s125,
    <https://www.jstor.org/stable/2004361>.
    """

    def __init__(self, n, degree, variant):
        self.degree = degree
        self.dim = n

        if degree == 7:
            d = {
                ("a", 3): (
                    0.524647623275290,
                    0.165068012388578e1,
                    [
                        -0.166705761599566e2,
                        +0.100296981655678e2,
                        +0.161699246687754,
                        -0.604719151221535e1,
                        +0.234381399489666e-1,
                        +0.417194501880647e1,
                    ],
                ),
                ("a", 4): (
                    0.524647623275290,
                    0.165068012388578e1,
                    [
                        -0.167539329651562e3,
                        +0.687922329603575e2,
                        +0.203518409659014,
                        -0.255075279116885e2,
                        +0.415430214106084e-1,
                        +0.739458001434961e1,
                    ],
                ),
                # TODO find the mistake here
                # ("a", 5): (
                #     0.524647623275290,
                #     0.165068012388578e1,
                #     [
                #         -0.826940846964452e3,
                #         +0.264779097660331e3,
                #         +0.213460812375320,
                #         -0.714240197186780e2,
                #         -0.736330882774831e1,
                #         +0.131065518222629e2,
                #     ],
                # ),
                ("a", 6): (
                    0.524647623275290,
                    0.165068012388578e1,
                    [
                        -0.309679578630802e4,
                        +0.815423321880237e3,
                        +0.117326937169073,
                        -0.173057295296448e3,
                        +0.130511250871491,
                        +0.232307582494626e2,
                    ],
                ),
                ("b", 3): (
                    0.165068012388578e1,
                    0.524647623275290,
                    [
                        +0.166705761599566e2,
                        +0.178903161957074,
                        -0.665808190965810e1,
                        +0.148361823143070e-1,
                        +0.229669852539758e1,
                        +0.430097881732984e-2,
                    ],
                ),
                ("b", 4): (
                    0.165068012388578e1,
                    0.524647623275290,
                    [
                        +0.688432856406677e2,
                        +0.294997847268286,
                        -0.199427272118378e2,
                        +0.110498755408511e-1,
                        +0.407079214570997e1,
                        +0.762328646743931e-2,
                    ],
                ),
                ("b", 5): (
                    0.165068012388578e1,
                    0.524647623275290,
                    [
                        +0.220502344940121e3,
                        +0.537746975313769,
                        -0.497781460739792e2,
                        -0.743845245712926e-2,
                        +0.721529121489956e1,
                        +0.135119234557687e-1,
                    ],
                ),
                ("b", 6): (
                    0.165068012388578e1,
                    0.524647623275290,
                    [
                        +0.616293651884027e3,
                        +0.107529736766179e1,
                        -0.113807008098269e3,
                        -0.610828352270520e-1,
                        +0.127887706992535e2,
                        +0.239492607623178e-1,
                    ],
                ),
            }

            u, v, B = d[(variant, n)]

            data = [
                (B[0], z(n)),
                (B[1], fsd(n, (u, 1))),
                (B[2], fsd(n, (v, 1))),
                (B[3], fsd(n, (u, 2))),
                (B[4], fsd(n, (v, 2))),
                (B[5], fsd(n, (u, 3))),
            ]
        elif degree == 9:
            d = {
                ("a", 3): (
                    0.202018287045609e1,
                    0.958572464613819,
                    [
                        0.676448734429924,
                        0.511989106291551e-2,
                        0.448595723493744,
                        0.235223454595606e-3,
                        0.915390713080005e-1,
                        0.139208199920793e-1,
                        0.235223454595606e-3,
                        0.915390713080008e-1,
                    ],
                ),
                ("a", 4): (
                    0.202018287045609e1,
                    0.958572464613819,
                    [
                        -0.860452945007048,
                        -0.405511998533795e-1,
                        +0.107026475449715e+1,
                        +0.138974239307092e-3,
                        -0.162248779448181,
                        +0.246740110027234e-1,
                        +0.138974239307094e-3,
                        +0.162248779448181,
                        +0.138974239307094e-3,
                    ],
                ),
                ("a", 5): (
                    0.202018287045609e1,
                    0.958572464613819,
                    [
                        -0.827347006200826e1,
                        -0.160820174530905,
                        +0.353499863758467e1,
                        +0.738976276909564e-3,
                        -0.862735421812943,
                        +0.437335458190621e-1,
                        -0.246325425636523e-3,
                        +0.287578473937648,
                        +0.246325425636523e-3,
                    ],
                ),
                ("a", 6): (
                    0.202018287045609e1,
                    0.958572464613819,
                    [
                        -0.361840434143098e2,
                        -0.447936529138517,
                        +0.112077863004144e2,
                        +0.392940404320855e-2,
                        -0.254859786784158e1,
                        +0.775156917007496e-1,
                        -0.130980134773619e-2,
                        +0.509719573568315,
                        +0.436600449245395e-3,
                    ],
                ),
                ("b", 4): (
                    0.958572464613819,
                    0.202018287045609e1,
                    [
                        +0.265029088766810e-2,
                        +0.637601342635332,
                        -0.394394059389228e-1,
                        +0.540829264827264e-1,
                        -0.416922717921281e-3,
                        +0.246740110027234e-1,
                        +0.540829264827270e-1,
                        +0.416922717921281e-3,
                        +0.540829264827269e-1,
                    ],
                ),
                ("b", 5): (
                    0.958572464613819,
                    0.202018287045609e1,
                    [
                        -0.624416791055272,
                        +0.467494915583104,
                        -0.152937760910536,
                        +0.287578473937646,
                        -0.221692883072871e-2,
                        +0.437335458190621e-1,
                        -0.958594913125490e-1,
                        +0.738976276909568e-3,
                        +0.958594913125492e-1,
                    ],
                ),
                ("b", 6): (
                    0.958572464613819,
                    0.202018287045609e1,
                    [
                        +0.448873836333650e1,
                        -0.238473566140736e1,
                        -0.413008493198885,
                        +0.152915872070494e1,
                        -0.654900673868093e-2,
                        +0.775156917007496e-1,
                        -0.509719573568314,
                        +0.130980134773618e-2,
                        +0.169906524522772,
                    ],
                ),
            }

            u, v, B = d[(variant, n)]

            data = [
                (B[0], z(n)),
                (B[1], fsd(n, (u, 1))),
                (B[2], fsd(n, (v, 1))),
                (B[3], fsd(n, (u, 2))),
                (B[4], fsd(n, (v, 2))),
                (B[5], fsd(n, (u, 1), (v, 1))),
                (B[6], fsd(n, (u, 3))),
                (B[7], fsd(n, (v, 3))),
            ]
            if n > 3:
                data += [(B[8], fsd(n, (u, 4)))]

        else:
            assert degree == 11

            d = {
                ("a", 3): (
                    0.235060497367449e1,
                    0.436077411927617,
                    0.133584907401370e1,
                    [
                        -0.881591029957858e1,
                        -0.751996143360650e-1,
                        +0.621743189471515e1,
                        +0.241426451456494,
                        -0.120709739276065e-2,
                        -0.427751221210138e1,
                        +0.550169924840163e-1,
                        +0.237084999634707e-1,
                        -0.169791992887741e-2,
                        -0.252266276123350e-4,
                        +0.326777873717691e1,
                        +0.968469949206802e-2,
                        +0.789754514877422e-3,
                    ],
                ),
                ("a", 4): (
                    0.235060497367449e1,
                    0.436077411927617,
                    0.133584907401370e1,
                    [
                        +0.241502736147339e3,
                        -0.196095938531478,
                        -0.128675737999280e3,
                        +0.307568784278696,
                        -0.480908422319460e-2,
                        +0.698087019367085e2,
                        +0.631837143743771e-1,
                        +0.392226151971179e-1,
                        -0.300948471646799e-2,
                        -0.650235306755170e-4,
                        -0.386951974646715e2,
                        +0.171656829095787e-1,
                        +0.139980343116450e-2,
                        +0.101552487093372e-4,
                        +0.222435922356439e2,
                    ],
                ),
                # TODO find the mistake here
                # ("a", 5): (
                #     0.235060497367449,
                #     0.436077411927617,
                #     0.133584907401370e1,
                #     [
                #         +0.255885269311763e4,
                #         -0.439598677491526,
                #         -0.106541406144610e4,
                #         +0.453540909054264,
                #         -0.132100905623778e-1,
                #         +0.418606568954203e3,
                #         +0.511394563043680e-1,
                #         +0.645581013845604e-1,
                #         -0.533417277494500e-2,
                #         -0.137981626254496e-3,
                #         -0.147436933189884e3,
                #         +0.304253807765057e-1,
                #         +0.248108698207828e-2,
                #         +0.113652094546015e-4,
                #         +0.394257407160391e2,
                #         +0.331725011358320e-5,
                #     ],
                # ),
                ("b", 3): (
                    0.235060497367449e1,
                    0.133584907401370e1,
                    0.436077411927617,
                    [
                        -0.141214037032900e2,
                        -0.803730274707282e-1,
                        +0.235546545595906,
                        +0.888123191556611e1,
                        +0.142467131155533e-3,
                        +0.582993124006494e-1,
                        -0.561099173155661e1,
                        -0.204028691521686e-2,
                        +0.252880089932256e-1,
                        -0.814378678627283e-4,
                        +0.804353953375146e-2,
                        +0.393451849690453e1,
                        +0.171183493169724e-3,
                    ],
                ),
                ("b", 4): (
                    0.235060497367449e1,
                    0.133584907401370e1,
                    0.436077411927617,
                    [
                        -0.151944464736584e3,
                        -0.223498438689039,
                        +0.243574919068010,
                        +0.634373877008693e2,
                        -0.782065187814018e-4,
                        +0.911833754536616e-1,
                        -0.238927288245914e2,
                        -0.422314408318853e-2,
                        +0.448218289217760e-1,
                        -0.138053374667391e-3,
                        +0.607473265800655e-2,
                        +0.697375246129742e1,
                        +0.303414841680135e-3,
                        -0.314574391771792e-5,
                        +0.409103498175100e-2,
                    ],
                ),
                ("b", 5): (
                    0.235060497367449e1,
                    0.133584907401370e1,
                    0.436077411927617,
                    [
                        -0.761305347548192e3,
                        -0.536360805019297,
                        +0.110669832078736,
                        +0.246421088923968e3,
                        -0.773649327968607e-3,
                        +0.169088641205970,
                        -0.670700680243651e2,
                        -0.856090560229205e-2,
                        +0.794446232770302e-1,
                        -0.220272863263544e-3,
                        -0.373515812228225e-2,
                        +0.123606544052884e2,
                        +0.537788804557843e-3,
                        -0.122101861480881e-4,
                        +0.725117070759373e-2,
                        +0.331725011358320e-5,
                    ],
                ),
            }

            u, v, w, B = d[(variant, n)]

            data = [
                (B[0], z(n)),
                (B[1], fsd(n, (u, 1))),
                (B[2], fsd(n, (v, 1))),
                (B[3], fsd(n, (w, 1))),
                (B[4], fsd(n, (u, 2))),
                (B[5], fsd(n, (v, 2))),
                (B[6], fsd(n, (w, 2))),
                (B[7], fsd(n, (u, 1), (v, 1))),
                (B[8], fsd(n, (u, 1), (w, 1))),
                (B[9], fsd(n, (u, 3))),
                (B[10], fsd(n, (v, 3))),
                (B[11], fsd(n, (w, 3))),
                (B[12], fsd(n, (u, 2), (v, 1))),
            ]
            if n > 3:
                data += [(B[13], fsd(n, (u, 4))), (B[14], fsd(n, (v, 4)))]
            if n > 4:
                data += [(B[15], fsd(n, (u, 5)))]

        # TODO According to Stroud,
        #      Stenger's original article has data up to n == 20.

        self.points, self.weights = untangle(data)
        return
