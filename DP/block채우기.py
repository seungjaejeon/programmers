def solution(n):
    answer = 0
    # dp 문제
    dp = []
    # dp[n] = dp[n-2] + dp[n-1]
    # n-2까지 + 가로로 2개 배치
    # n-1까지 + 세로로 1개 배치
    dn2 = 2
    dn1 = 3 # 3
    # dp[n-2] = dn2
    # dp[n-1] = dn1
    for i in range(3,n):
        answer = dn2 + dn1
        dn2 = dn1
        dn1 = answer
    answer %= 1000000007
    return answer