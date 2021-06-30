
# -*- coding: utf-8 -*-

# Test the height interpolators.

__all__ = ('Tests',)
__version__ = '21.04.06'

import warnings  # PYCHOK expected
# RuntimeWarning: numpy.ufunc size changed, may indicate binary
# incompatibility. Expected 192 from C header, got 216 from PyObject
# warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings('ignore')  # or 'error'

from base import coverage, scipy, PyGeodesy_dir, TestsBase

from pygeodesy import fstr, len2, egmGeoidHeights, GeoidError, \
                      GeoidG2012B, GeoidKarney, GeoidPGM, \
                      LatLon_, RangeError, reprs

import os.path as _os_path
from os import SEEK_SET as _SEEK_SET

_GeoidHeights_dat = b'''
# the first and last 100 tests from GeoidHeights.dat.gz
# <https://GeographicLib.SourceForge.io/html/geoid.html> or
# <https://SourceForge.net/projects/geographiclib/files/testdata/>

# Lat EasternLon egm84-15 egm96-5 egm2008-1-height

-76.981466 34.17016 11.728631 11.423169 12.63629
79.695484 88.805571 .270438 .891749 .749472
-15.244804 168.747961 67.073604 65.225787 65.108852
-19.379357 15.85511 25.343778 24.463147 24.888926
43.377784 229.448418 -28.919198 -29.682024 -29.55705
-16.074554 21.79547 14.386181 10.50343 9.741516
-11.256389 286.249745 30.699577 29.325619 30.058864
69.016564 344.078885 62.22524 60.423629 60.69041
2.221008 139.73935 70.222337 68.996386 69.133157
-9.096878 119.141551 34.336473 36.28656 36.520307
-28.523717 337.8075 8.206342 6.62604 6.80124
12.27231 223.575832 -20.073991 -20.86047 -20.651171
-15.20317 274.396247 -3.129 -3.267352 -3.040335
-63.735565 282.830364 -3.216893 -1.294072 -1.328486
-48.770825 269.897883 -1.531173 -2.322219 -2.171739
-.178524 233.631721 -16.741719 -17.556563 -17.410584
1.585536 231.113033 -15.412191 -16.593709 -16.424896
-48.780705 357.315776 25.078435 24.452906 24.698135
-49.091632 136.862256 -18.120484 -18.592271 -18.328547
47.731727 17.552416 46.224162 44.048683 43.80209
-49.109549 85.706437 18.648819 18.581347 18.715655
-49.162281 40.321209 44.763702 44.289338 44.468585
3.498333 158.117699 51.089409 49.816268 49.944166
-35.616495 122.648407 -34.470784 -36.114401 -35.878488
56.598256 263.886304 -39.124416 -41.047955 -40.777363
-31.850231 149.120596 28.142406 26.455814 26.559031
-26.568996 182.207804 49.618755 49.317355 49.360929
76.734699 294.247048 22.575416 20.713728 21.106933
-21.404166 237.732131 -6.893444 -7.361787 -7.201667
-77.133426 294.526181 -15.011837 -16.491509 -17.168179
-58.811779 2.276142 18.775885 18.11021 18.358801
4.415102 155.683336 53.645102 51.857634 52.1179
-28.145768 107.081334 -39.074187 -38.980789 -38.949896
-10.551267 233.309532 -9.644782 -9.913469 -9.934107
-25.444344 256.662816 -2.527513 -2.827762 -2.879439
24.435896 46.158715 -6.907432 -5.71888 -5.02473
-72.888898 37.106907 21.711451 22.42618 24.296122
-19.628762 13.244525 25.611378 24.545472 25.131399
-7.602449 171.264763 41.569322 40.652208 40.720931
-45.364396 358.123588 23.27953 22.383208 22.38785
-7.292121 290.820435 24.501779 22.181925 22.485568
-31.566264 193.311015 14.826064 14.929537 14.942774
-82.751144 197.91477 -45.104466 -47.094479 -47.38728
-40.699637 99.465509 -17.252382 -18.42052 -18.403108
48.675771 39.690012 12.971704 10.054773 10.184582
74.817287 281.595813 4.775889 5.785837 5.671428
-81.032306 296.135102 -23.577487 -22.83844 -24.576521
74.021785 9.431926 43.884933 42.989094 43.288464
-75.070563 17.57935 17.071599 15.353044 13.747941
-12.54612 305.149386 -6.643347 -6.336934 -5.341732
-13.621418 42.407805 -23.324774 -25.5549 -25.579123
-2.265774 268.048563 -10.69818 -9.922819 -9.849219
-18.672316 42.547125 -10.265162 -10.85178 -10.490815
-41.439867 157.413161 .689022 -.135359 .244268
53.68637 280.625 -43.757679 -43.809145 -43.820782
39.260397 329.648641 57.554204 57.150303 57.401275
-51.699195 218.506918 -16.936125 -17.657204 -17.889512
36.584861 4.515157 45.294724 46.358218 46.421497
39.641638 305.341154 -13.585597 -14.404308 -14.474804
59.761024 166.566646 11.467687 11.241571 11.118082
51.830001 13.357464 42.091574 42.236804 42.290864
-36.530912 184.569196 22.829999 22.146699 22.326393
-37.079518 125.263901 -32.302423 -33.395909 -33.097781
-68.650762 92.731524 9.227858 7.961014 9.430239
35.086645 45.335611 5.964588 7.229317 6.03228
-61.355646 190.621071 -45.012801 -44.291815 -44.33029
-36.954967 179.11982 21.117704 21.874779 21.774899
10.248399 353.286441 30.496904 28.933062 29.243138
36.868193 84.602243 -40.396259 -41.23805 -40.675514
28.636703 88.932955 -31.70367 -31.330591 -31.352523
54.810777 260.031957 -32.276942 -32.701812 -32.700724
7.610621 145.911188 61.024116 60.116956 60.628741
59.411557 170.102394 4.994457 6.45672 6.616738
-61.468618 126.144056 -30.237492 -31.961455 -31.887254
18.514019 222.916699 -26.005544 -26.571452 -26.53512
7.854318 233.200852 -29.283445 -29.76023 -29.62976
47.489222 134.182527 22.393817 21.98005 22.274668
-34.143602 348.078433 17.549603 16.848958 17.094407
-58.388787 117.457755 -20.622029 -20.922656 -20.940551
9.772764 95.845943 -41.484214 -42.748629 -42.739663
-53.120381 136.993994 -20.967976 -21.841353 -21.650771
-50.349867 .07532 25.567797 25.482432 25.240177
31.438387 189.121452 -8.580764 -8.847394 -8.757998
37.540689 206.975772 -18.329185 -19.603604 -19.60685
27.586088 2.443556 25.000651 25.668106 26.258251
-26.139126 253.79919 -2.940176 -3.772451 -3.82443
-33.425976 345.159641 18.228244 17.747731 18.195353
39.586286 206.981026 -16.506817 -17.838751 -17.724519
-60.790289 357.421837 14.274585 14.292293 14.512553
-20.130538 21.974941 16.852191 16.529145 16.808723
75.64878 99.920587 -6.872251 -8.228616 -8.025835
-.385453 336.211664 9.006041 9.829743 9.688362
-51.559564 309.67313 6.295961 6.214608 6.218105
-43.129209 192.72853 -1.481421 -2.95956 -2.724054
46.374177 71.947616 -40.915253 -42.323099 -42.565295
-22.783085 140.657444 37.495018 38.355565 38.341296
-12.05584 122.80402 32.257731 34.259127 33.888543
30.127372 94.738186 -41.528667 -37.397451 -37.380369
46.296018 185.521384 -1.376543 -2.01595 -1.858026
34.989646 15.051646 35.280295 33.911985 34.195497

-51.287168 90.564711 12.958348 12.676251 12.766671
34.217016 141.301548 18.307327 15.691819 15.611693
-40.423023 217.213408 -10.399985 -11.117167 -11.06297
-17.854486 189.783646 28.637699 27.436544 27.387362
47.803271 112.700942 -24.058856 -23.893792 -23.816559
-23.275962 133.453821 18.806212 18.76554 18.712425
-26.884369 323.429346 -6.820405 -7.451636 -7.343834
-37.106468 31.127939 31.486465 30.143266 29.997919
-75.363185 186.326351 -62.023637 -61.171934 -61.869194
-18.30485 69.015565 -24.24778 -24.889693 -24.937103
39.527401 23.580206 43.255362 39.51882 38.556254
68.903148 30.970247 18.498052 19.419431 19.671416
53.936937 168.318201 4.066592 2.068616 2.272381
-38.600098 64.811532 25.454194 25.047773 24.862823
-41.395739 290.260582 26.656734 22.546619 21.635812
50.157749 72.319017 -31.965646 -34.358649 -33.850823
27.691879 176.152884 -4.415253 -5.452957 -5.298515
-48.419449 170.454472 -6.741234 -6.803845 -6.788802
-65.34567 235.024039 -34.899718 -35.054051 -35.03012
-51.873009 167.265613 -14.222699 -15.41797 -15.338108
-7.262544 84.307626 -79.316645 -79.557063 -79.355862
-1.461003 254.541677 -16.163092 -16.894081 -16.649513
7.684324 161.87293 36.28664 36.215074 36.359233
-31.474549 201.479967 4.067589 3.523011 3.614578
-36.187212 62.917075 24.406552 23.797348 23.946648
16.002975 141.686552 53.054459 51.585904 51.495032
30.182218 86.260576 -30.622274 -30.131119 -30.90993
-77.303842 159.497665 -53.539632 -51.847914 -52.130637
39.536 139.795358 36.262233 37.191528 37.044702
8.569309 134.618403 64.368519 63.59657 64.179967
14.473483 90.595663 -61.299612 -62.636188 -62.474757
-13.13767 260.410798 -7.999483 -8.717383 -8.454344
34.211572 333.692806 41.47749 40.645455 40.833883
21.889732 76.371362 -59.875563 -60.728795 -60.455377
29.792909 120.48703 8.403634 8.782794 9.726744
15.723814 122.713685 39.152283 31.522843 32.141881
-66.20776 281.501193 -7.076284 -6.250418 -6.220363
-39.507049 55.808743 33.17796 32.599113 32.488683
28.159494 51.476474 -23.83233 -24.535816 -24.691902
-36.206825 120.205019 -38.206222 -38.869477 -38.748596
30.574607 260.001867 -22.142407 -23.212882 -23.254521
-16.992515 37.135881 -13.765389 -11.824355 -13.454976
-11.476997 12.038708 16.898354 16.709275 16.627228
30.428465 215.234951 -22.473854 -22.378764 -22.2212
-17.439773 267.575661 -4.717712 -4.940867 -4.835735
40.203164 143.429799 16.635366 19.393545 19.571063
-37.098392 253.426288 -9.011662 -9.380758 -9.226603
54.620478 291.587064 -23.543253 -23.318917 -23.247578
-31.633252 148.181926 26.236233 24.468356 24.829144
-56.069748 218.593222 -21.95316 -21.761095 -21.705174
-8.195214 307.308823 -17.959479 -18.797699 -17.05341
17.850526 24.748606 9.078096 12.611532 11.715897
0.349465 251.667333 -19.158189 -19.706347 -19.530079
15.037932 126.190545 46.775901 45.791796 45.929352
-21.111105 236.304019 -8.054682 -8.405877 -8.283123
30.946618 173.002137 -7.696224 -8.367274 -8.466797
-10.698334 215.908891 -1.048564 -2.02472 -1.829127
-29.412071 124.75279 -16.0813 -16.568968 -16.505889
38.223621 222.810624 -35.426661 -35.435226 -35.384083
36.063775 227.590716 -38.64802 -39.008674 -38.962653
29.974676 178.075894 -5.518814 -6.920902 -6.956012
-21.346396 169.259508 53.430852 50.794726 51.005387
49.282472 207.065591 1.978855 1.070289 1.192049
16.349121 260.037771 -13.196886 -14.214219 -15.038289
-14.293325 192.660201 18.944781 17.600467 17.791473
47.165911 321.477371 45.186641 44.804262 44.652484
-58.910597 114.346927 -17.145188 -17.922401 -17.97107
-9.055095 111.294422 13.145756 10.661522 11.631261
18.390988 29.691577 4.932744 7.670083 7.393769
-15.074412 22.152663 12.326416 8.623243 7.932082
-4.234571 62.001081 -60.029589 -60.722522 -60.593396
15.170822 273.417071 3.110034 3.818214 4.38383
79.254009 112.115515 -2.740569 -1.871357 1.296574
15.947068 156.092678 32.08547 30.633315 30.851522
68.370605 182.617873 2.059527 2.800537 2.704084
-41.931009 287.906587 22.915549 19.859478 21.263923
-1.192967 216.866922 5.518518 5.347503 5.442511
-37.006115 154.512534 11.020238 9.941435 9.997852
-22.148493 9.938408 22.171442 22.320708 22.427896
24.328746 109.043774 -22.943766 -24.13483 -23.154175
-54.877699 114.691444 -17.579665 -17.679452 -17.661936
45.600662 279.542021 -35.737741 -37.150173 -36.839234
2.371766 58.974082 -61.040248 -61.157623 -61.220881
15.936522 165.854035 20.907109 20.601618 20.355248
4.889499 335.786806 13.874119 13.055023 13.147246
-11.392365 179.558198 40.92905 40.132377 41.072213
58.24629 4.862128 43.191036 43.262637 42.982287
34.302001 250.891341 -22.005975 -23.126167 -22.998424
-58.195787 117.305696 -20.375014 -20.677701 -20.662136
44.499876 173.768568 -7.85222 -8.528636 -8.438426
-28.862539 220.225188 -8.674412 -8.665908 -8.711761
19.507043 263.900567 -14.116994 -12.795613 -12.653472
-42.487604 286.093398 17.251016 15.773284 17.165992
46.138437 218.570807 -19.435532 -19.954462 -19.873676
60.506969 93.74336 -31.330133 -31.479738 -31.124006
26.219081 214.565609 -17.090479 -17.429026 -17.30664
-28.68714 3.370196 24.183794 24.037253 23.434054
-15.007944 117.449536 6.142445 4.519942 4.507939
40.710024 144.095126 11.693337 11.393603 11.54915
20.823096 186.389203 6.839505 5.679085 5.74824

# the Timbuktu example from online GeoidEval
# <https://GeographicLib.SourceForge.io/cgi-bin/GeoidEval>
16.776 -3.009 31.2979 28.7067 28.7880

# the G2012B/g2012bu*.bin centers, heights from GeoidEval
41  -95.0 -31.9524 -30.2615 -30.5889
49 -120.5 -14.9456 -15.9842 -15.2731
49 -103.5 -17.0318 -18.6354 -18.6241
49  -86.5 -37.9619 -37.7488 -37.8725
49  -69.5 -26.4922 -26.6913 -26.5105
33 -120.5 -39.5433 -39.5610 -39.6000
33 -103.5 -22.5560 -22.5622 -22.6888
33  -86.5 -28.7099 -30.0115 -30.0667
33  -69.5 -46.5897 -48.0387 -48.0929
'''


class Tests(TestsBase):

    _crop4     = None
    _dat5tests = _GeoidHeights_dat
    _epsHeight = 0.010  # 1 centi-meter
    _hIndex    = 0  # invalid
    _kind      = 3

    def dat5llhs3(self, grid, hIndex=4):
        # Generate test 3-tuples (lat, lon, expected)
        egm = _os_path.basename(grid).lower()
        # tuple index of the expected geoid height
        h = 2 if 'egm84-'  in egm else (
            3 if 'egm96-'  in egm else (
            4 if 'egm2008-'in egm else (
            self._hIndex or hIndex)))
        if not 2 <= h <= 4:
            raise ValueError('%s: %s' % ('-hindex', h))

        for t5 in egmGeoidHeights(self._dat5tests):
            lat, lon = t5.lat, t5.lon
#           if lon > 180:  # EasternLon to earth lon
#               lon -= 360
            yield lat, lon, t5[h]

    def testGeoid(self, G, grid, llh3, crop=None, eps=None, kind=None):  # MCCABE 13
        # test geoid G(grid) for (lat, lon, height, eps)
        if scipy or G is GeoidKarney:
            e_max = 0
            eps = eps or self._epsHeight
            f = self.failed - self.known
            with G(grid, kind=kind or self._kind, crop=crop) as g:
                s = '%s.height(%%s) kind %s' % (g, g.kind)
                for lat, lon, expected in llh3:
                    t = s % (fstr((lat, lon), prec=3),)
                    try:
                        h = g.height(lat, lon)
                        e = abs(h - expected)
                        if e_max < e:
                            e_max = e
                        self.test(t, h, expected, fmt='%.3f', known=e < eps)
                    except GeoidError as x:
                        self.test(t, str(x), '%.3f' % (expected,),
                                     known=G not in (GeoidKarney, GeoidPGM))
                    except RangeError as x:
                        self.test(t, str(x), '%.3f' % (expected,),
                                     known=bool(crop))

                    except KeyboardInterrupt as x:
                        self.printf(repr(x), nl=1)
                        break

                f = self.failed - self.known - f
                if f > 0 or e_max > 0:
                    h = '' if g.hits is None else ', hits %s' % (g.hits,)
                    t = '%s.height() kind %s%s, eps max (in %s FAILED)' % (g, g.kind, h, f)
                    x = eps if f > 0 else e_max
                    self.test(t, e_max, x, fmt='%.3f', known=e_max < eps, nl=1, nt=1)

                # print('%r\n\n%r' % (g, getattr(g, 'pgm', None)))
                if coverage:
                    for a in ('highest', 'lowerleft', 'lowerright', 'lowest', 'upperleft', 'upperright'):
                        t = fstr(getattr(g, a)(), prec=3)
                        self.test('%s.%s()' % (g, a), t, t, known=True)
                    for p in ('dtype', 'knots', 'mean', 'nBytes', 'scipy', 'smooth', 'stdev'):  # , 'pgm'
                        t = ''.join(reprs((getattr(g, p),), prec=3))
                        self.test('%s.%s' % (g, p), t, t, known=True)
                    for a in ('_g2ll2', '_ll2g2'):
                        t = getattr(g, a)(180, 360)
                        self.test('%s.%s(180, 360)' % (g, a), t, t, known=True)
                    for t in ((LatLon_(-10, -100), LatLon_(10, 100)),
                              (       (-10, -100),        (10, 100))):
                        t = g._swne(t)
                        self.test('%s.%s' % (g, '_swne'), t, '(-10.0, -100.0, 10.0, 100.0)')

                t = g.toStr()
                self.test('%s.%s' % (g, 'toStr'), t, t, known=True, nt=1)

            self.test('closed', g.closed, True)
            self.testCopy(g)

        else:
            n, _ = len2(llh3)
            if coverage:
                n += 19
            self.skip('no scipy', n=n + 3)


if __name__ == '__main__':  # PYCHOK internal error?

    import sys

    # usage: testGeoids.py [-dat GeoidHeights.dat] [-eps 0.010]
    #        [-hindex 2-4] [-kind -5, -3, -2, 1, 2, 3, 4, 5]
    #        [.../testGeoids/egm*.pgm]
    #        [.../testGeoids/g2012b*.bin] ...

    t = Tests(__file__, __version__)

    _CONUS = 25, -125, 55, -65
    _GeoidEGM = None

    gs = sys.argv[1:]
    while gs:  # get cmd line options
        g = gs.pop(0)
        g_ = g.lower()

        if '-crop'.startswith(g_) and len(g_) > 1:
            t._crop4 = _CONUS
        elif '-karney'.startswith(g_) and len(g_) > 1:
            _GeoidEGM = GeoidKarney
        elif '-pgm'.startswith(g_) and len(g_) > 1:
            _GeoidEGM = GeoidPGM

        elif not gs:
            gs.insert(0, g)
            break
        elif '-dat'.startswith(g_) and len(g_) > 1:
            # load GeoidHeights.dat from file
            f = open(gs.pop(0), 'rb')
            if f.read(2) == b'\037\213':  # .gz
                t.test('-dat <file.dat>', f.name, '-.dat')
                t.exit()
            f.seek(0, _SEEK_SET)
            t._dat5tests = f
        elif '-eps'.startswith(g_) and len(g_) > 1:
            t._epsHeight = float(gs.pop(0))
        elif '-hindex'.startswith(g_) and len(g_) > 1:
            t._hIndex = int(gs.pop(0))
        elif '-kind'.startswith(g_) and len(g_) > 1:
            t._kind = int(gs.pop(0))
        else:
            gs.insert(0, g)
            break

    if not gs:  # look for ../testGeoids/egm*.pgm
        from glob import glob
        gs = glob(_os_path.join(PyGeodesy_dir, '../testGeoids/egm*.pgm')) \
           + glob(_os_path.join(PyGeodesy_dir, '../testGeoids/g*u0.bin'))

    if gs:  # test one or more geoids/grids
        for g in gs:
            g_ = g.lower()

            if g_.endswith('.pgm',):
                # Karney or PGM geoids .../egm*.pgm
                if _GeoidEGM:
                    t.testGeoid(_GeoidEGM, g, t.dat5llhs3(g), crop=t._crop4)
                else:
                    t.testGeoid(GeoidKarney, g, t.dat5llhs3(g), kind=2, eps=0.12)
                    t.testGeoid(GeoidKarney, g, t.dat5llhs3(g), kind=3)
                    try:
                        t.testGeoid(GeoidPGM, g, t.dat5llhs3(g), crop=_CONUS)
                    except ImportError as x:
                        t.skip(str(x), n=231)

            elif g_.endswith('g2012bu0.bin'):
                try:  # .../G2012B/CONUS/g2012bu0.bin
                    t.testGeoid(GeoidG2012B, g,
                        # centers of g2012bu*.bin grids
                        ((41,  -95.0, -30.312),
                         (49, -120.5, -16.112),
                         (49, -103.5, -18.955),
                         (49,  -86.5, -37.584),
                         (49,  -69.5, -25.867),
                         (33, -120.5, -39.554),
                         (33, -103.5, -21.917),
                         (33,  -86.5, -29.001),
                         (33,  -69.5, -46.725)))
                    # t.testGeoid(GeoidG2012B, g, *t.dat5llhs3(g, hIndex=4))
                except ImportError as x:
                    t.skip(str(x), n=30)

            elif not g_.endswith('.bin'):
                t.test('geoid', repr(g), "'.pgm' or '.bin'")

        t.results()
    else:
        t.results(passed='SKIPPED', nl=0)

    t.exit()
