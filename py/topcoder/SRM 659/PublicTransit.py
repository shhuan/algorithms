# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class PublicTransit:

    def distRaw(self, R, C, i1, j1, i2, j2):
        # q = [(i1, j1, 0)]
        # deltas = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        # while q:
        #     i, j, d = q.pop(0)
        #     if i == i2 and j == j2:
        #         return d
        #     for delta in deltas:
        #         ni = i + delta[0]
        #         nj = j + delta[1]
        #         if 0 <= ni < R and 0 <= nj < C:
        #             q.append((ni, nj, d+1))
        # return 1000
        return abs(i1-i2)+abs(j1-j2)



    def distAfterConnect(self, R, C, connect, i1, j1, i2, j2):
        if i1 == i2 and j1 == j2:
            return 0
        return min(self.distRaw(R, C, i1, j1, i2, j2), \
                   self.distRaw(R, C, i1, j1, connect[0], connect[1]) + self.distRaw(R, C, connect[2], connect[3], i2, j2), \
                   self.distRaw(R, C, i1, j1, connect[2], connect[3]) + self.distRaw(R, C, connect[0], connect[1], i2, j2))

    def maxDist(self, R, C, connect):
        res = 1
        for i1 in range(R):
            for j1 in range(C):
                for i2 in range(R-1, -1, -1):
                    for j2 in range(C-1, -1, -1):
                        if abs(i1-i2) + abs(j1-j2) <= res:
                            continue
                        res = max(res, self.distAfterConnect(R, C, connect, i1, j1, i2, j2))
        return res

    def minimumLongestDistance(self, R, C):

        if R <= 0 or C <= 0:
            return 0
        if R*C <= 2:
            return 1

        res = 1000
        for i1 in range(R):
            for j1 in range(C):
                for i2 in range(R):
                    for j2 in range(C):
                        if i1 == i2 and j1 == j2:
                            continue
                        # connect (i, j) and (i2, j2)
                        res = min(res, self.maxDist(R, C, (i1, j1, i2, j2)))

        return res

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(R, C, __expected):
    startTime = time.time()
    instance = PublicTransit()
    exception = None
    try:
        __result = instance.minimumLongestDistance(R, C);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("PublicTransit (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("PublicTransit.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            R = int(f.readline().rstrip())
            C = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(R, C, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1431783977
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
