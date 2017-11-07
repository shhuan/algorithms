# -*- coding: utf-8 -*-
import collections

N = int(raw_input())
W = [0] + map(int, raw_input().split())
E = collections.defaultdict(list)

for i in range(N - 1):
    s, t, l = map(int, raw_input().split())
    E[s].append((t, l))
    E[t].append((s, l))

Q = int(raw_input())

for qi in range(Q):
    s, r = map(int, raw_input().split())
    q = []
    v = [0] * (N+1)
    v[s] = 1
    for t, l in E[s]:
        v[t] = 1
        q.append((t, l))
    weight, node = float('-inf'), None
    while q:
        t, l = q.pop(0)
        if l <= r:
            # nodes.append(t)
            if W[t] > weight:
                weight = W[t]
                node = t
            elif W[t] == weight:
                node = min(node, t)
            for tt, lt in E[t]:
                if not v[tt]:
                    v[tt] = 1
                    q.append((tt, l + lt))
    print node
