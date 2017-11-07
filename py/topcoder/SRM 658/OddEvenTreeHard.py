# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class OddEvenTreeHard:
    def getTree(self, x):

        if not x:
            return [-1]

        x = list(map(list, x))

        for i in range(len(x)):
            if x[i][i] == 'O':
                return [-1]
            else:
                x[i][i] = 'E'
            for j in range(len(x)):
                if x[i][j] == 'E' and x[j][i] == 'O':
                    return [-1]
                if x[i][j] == 'O' and x[j][i] == 'E':
                    return [-1]
                if x[i][j] == '?':
                    x[i][j] = x[j][i]
                if x[j][i] == '?':
                    x[j][i] = x[i][j]

        # warshall
        for k in range(len(x)):
            for i in range(len(x)):
                for j in range(len(x)):
                    if x[i][j] == '?' or x[j][i] == '?':
                        continue
                    a = x[i][j] == 'O'
                    b = x[j][k] == 'O'
                    if x[i][k] == '?':
                        x[i][k] = x[k][i] = 'O' if a != b else 'E'
                    c = x[i][k] == 'O'
                    if c != (a != b):
                        return [-1]

        for k in range(len(x)):
            for i in range(len(x)):
                if x[k][j] == '?':
                    x[k][j] = 'O'
                    for j in range(len(x)):
                        if x[k][i] == '?' or x[i][j] == '?':
                            continue
                        if x[k][i] == x[i][j]:
                            x[k][j] = 'E'

        q = [0]
        res = []
        used = {0}
        while q:
            u = q.pop(0)
            for v in range(len(x)):
                if v not in used and x[u][v] == 'O':
                    used.add(v)
                    res.append(u)
                    res.append(v)
                    q.append(v)
        if len(res) != 2*len(x)-2:
            return [-1]

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

def do_test(x, __expected):
    startTime = time.time()
    instance = OddEvenTreeHard()
    exception = None
    try:
        __result = instance.getTree(x);
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
    sys.stdout.write("OddEvenTreeHard (1000 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("OddEvenTreeHard.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            x = []
            for i in range(0, int(f.readline())):
                x.append(f.readline().rstrip())
            x = tuple(x)
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(int(f.readline().rstrip()))
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(x, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1430926403
    PT, TT = (T / 60.0, 75.0)
    points = 1000 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
