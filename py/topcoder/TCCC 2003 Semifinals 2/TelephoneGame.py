# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class TelephoneGame:
    def howMany(self, connect1, connect2, numPeople):
        """
        分成两组，使得相交的区间最少
        :param connect1:
        :param connect2:
        :param numPeople:
        :return:
        """
        connections = [(connect1[i], connect2[i]) for i in range(len(connect1))]

        collections = sorted(connections, key=lambda x: x[0])
        print(connections)

        crosses = [connections[0]]
        for i in range(1, connections):
            if self.crosses(crosses[-1], connections[i], numPeople):
                crosses.append(connections[i])

        connections = [crosses[0]]
        res = 0
        for i in range(1, crosses):
            if self.cross(connections[-1], crosses[i], numPeople):
               res += 1
            else:
                connections.append(crosses[i])
        return res


    def cross(self, connection1, connection2, numPeople):

        if connection1[0] > connection2[0]:
            connection1, connection2 = connection2, connection1

        l1, r1 = connection1
        l2, r2 = connection2
        if l1 < l2 < r1 < r2:
            return True

        return False





        return 0

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

def do_test(connect1, connect2, numPeople, __expected):
    startTime = time.time()
    instance = TelephoneGame()
    exception = None
    try:
        __result = instance.howMany(connect1, connect2, numPeople);
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
    sys.stdout.write("TelephoneGame (1050 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("TelephoneGame.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            connect1 = []
            for i in range(0, int(f.readline())):
                connect1.append(int(f.readline().rstrip()))
            connect1 = tuple(connect1)
            connect2 = []
            for i in range(0, int(f.readline())):
                connect2.append(int(f.readline().rstrip()))
            connect2 = tuple(connect2)
            numPeople = int(f.readline().rstrip())
            f.readline()
            __answer = int(f.readline().rstrip())

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(connect1, connect2, numPeople, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1430752249
    PT, TT = (T / 60.0, 75.0)
    points = 1050 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
