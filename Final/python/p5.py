import sys


def find(now, before):
    # 남아있는 경로를 이미 방문한 적이 있음
    if dp[now][before]:
        return dp[now][before]
    # 모두 방문한 경우
    if before == (1 << n) - 1:
        return path[now][0] if path[now][0] > 0 else sys.maxsize
    # 현재 지점에서 이동할 수 있는 지점들을 탐색
    cost = sys.maxsize
    for i in range(1, n):
        if not (before >> i) % 2 and path[now][i]:
            # i부터 0까지 순회를 만든 최소 비용
            # before | (1<<i) == before + (1<<i)
            tmp = find(i, before | (1 << i))
            # (now~i), (i~0)의 합과 현재까지의 최소 비용과 비교
            cost = min(cost, tmp + path[now][i])
        # 메모이제이션
    dp[now][before] = cost
    return cost


n = int(sys.stdin.readline())
path = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(path)
dp = [[0]*(1 << n) for _ in range(n)]


print(find(4, 1))

#
# 4
# 0 10 15 20
# 10 0 35 25
# 15 35 0 30
# 20 25 30 0
#

#
# 5
# 0 30 50 20 25
# 10 0 50 35 25
# 30 50 0 10 30
# 10 20 10 0 50
# 25 25 35 50 0
