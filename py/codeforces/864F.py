# -*- coding: utf-8 -*-


import collections

N, M, Q = map(int, input().split())

ST = []
for i in range(M):
    ST.append([int(x) for x in input().split()])
ST.sort()

P = collections.defaultdict(list)
for s,t in ST:
    P[s].append(t)

INF = False
VISITED = [0] * (N+1)
def dfs(start, end, path, circle, kth):
    global INF
    if INF:
        return -1

    if start == end:
        if kth < len(path):
            return path[kth]
        return -1

    for to in P[start]:
        if not VISITED[to]:
            path.append(to)
            VISITED[to] = 1
            ans = dfs(to, end, path, circle, kth)
            if ans > 0:
                return ans
            VISITED[to] = 0
            path.pop()
        else:
            if not circle:
                # circle, break out from some point on the circle,
                # if it can reach destination, no smallest lexicographically path.
                # no need to record path
                print(path, to)
                ci = path.index(to)
                for j in range(ci+1, len(path)+1):
                    if dfs(path[j-1], end, [], True, kth):
                        INF = True
                        return -1
    return -1


for i in range(Q):
    VISITED = [0] * (N+1)
    s, t, k = map(int, input().split())
    INF = False
    print(dfs(s, t, [s], False, k-1))


# 2 3 4 5 4 5 4 5 .... 4 6