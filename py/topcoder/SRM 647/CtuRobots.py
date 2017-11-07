# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class CtuRobots:
    def maxDist(self, B, cost, cap):
        N = len(cost)
        pqr = [(cap[i], cost[i]) for i in range(N)]
        pqr = sorted(pqr)

        f = [[0.0 for b in range(B+1)] for n in range(N)]
        for b in range(pqr[0][1], B+1):
            f[0][b] = pqr[0][0]

        for n in range(1, N):
            for b in range(B+1):
                if b >= pqr[n][1]:
                    f[n][b] = max(f[n-1][b-pqr[n][1]]/3.0 + pqr[n][0], f[n-1][b])
                else:
                    f[n][b] = f[n-1][b]

        return f[N-1][B]/2.0

    def distanceFromFuel(self, fuel):
        """
        如果已经知道买了哪些车之后。
        把油箱按照容量排序，容量小的车先返回，第i辆车容量为Li，总共N辆车。
        第一辆车开出L1/3之后把L1/3的平均分给其他车，车1返回。
        第二辆车有油f(2)=L1/3/(N-1)+L2，开出AL2/3，分AL2/3的油给其他车,返回。
        第三辆车f(3) = f(2)/3/(N-2)+L3
        ...
        第N辆车有油f(N) = f(N-1)/3+LN
        最远可以开出f(N)/2

        证明：先开油少的车比先开油多的车跑的远。


        在此基础上，使用动态规划，判断第i辆车买不买。
        f(i,b)表示前i辆车，在钱为b的情况下最多能够跑多远。
        f(i,b) = max{f(i-1,b-cost[i])/3+cap[i]/2, f(i-1, b)}  b>=cost[i]
                 f(i-1, b)  b<cost[i]

        :param fuel:
        :return:
        """
        if not fuel:
            return 0
        fuel = sorted(fuel)
        N = len(fuel)
        x = fuel[0]/(N+1)
        sumx = x
        for i in range(1, N):
            x = (fuel[i]+sumx)/(N-i+1)
            sumx += x
        # sys.stderr.write('{} => {}\r\n'.format(fuel,x))
        return x


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

def do_test(B, cost, cap, __expected):
    startTime = time.time()
    instance = CtuRobots()
    exception = None
    try:
        __result = instance.maxDist(B, cost, cap);
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
    sys.stdout.write("CtuRobots (500 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("CtuRobots.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            B = int(f.readline().rstrip())
            cost = []
            for i in range(0, int(f.readline())):
                cost.append(int(f.readline().rstrip()))
            cost = tuple(cost)
            cap = []
            for i in range(0, int(f.readline())):
                cap.append(int(f.readline().rstrip()))
            cap = tuple(cap)
            f.readline()
            __answer = float(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(B, cost, cap, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1437055677
    PT, TT = (T / 60.0, 75.0)
    points = 500 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
