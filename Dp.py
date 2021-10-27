import sys

# Using recursion
def minSteps(n):
    if n == 1:
        return 0
    ans1 = sys.maxsize
    if n%3 == 0:
        ans1 = minSteps(n//3)
    ans2 = sys.maxsize
    if n%2 == 0:
        ans2 = minSteps(n//2)
    ans3 = minSteps(n-1)
    ans = 1 + min(ans1,ans2,ans3)
    return ans

n = int(input())
print(minSteps(n))

# Dp
def min_dp(n,dp):
    if n == 1:
        return 0

    ans1 = sys.maxsize
    if n%3 == 0:
        if dp[n // 3] == -1:
            ans1 = min_dp(n // 3,dp)
            dp[n // 3] = ans1
        else:
            ans1 = dp[n//3]

    ans2 = sys.maxsize
    if n % 2 == 0:
        if dp[n // 2] == -1:
            ans2 = min_dp(n // 2,dp)
            dp[n // 2] = ans2
        else:
            ans2 = dp[n // 2]

    ans3 = sys.maxsize
    if dp[n-1] == -1:
        ans3 = min_dp(n-1,dp)
        dp[n-1] = ans3
    else:
        ans3 = dp[n-1]

    return 1 + min(ans1,ans2,ans3)

n = int(input())
dp = [-1 for i in range(n+1)]
print(min_dp(n,dp))