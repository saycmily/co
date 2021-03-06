class Solution:
    def mincostTickets(self, days, costs):
        dp = [0 for _ in range(days[-1] + 1)]
        days_idx = 0
        for i in range(1, len(dp)):
            if i != days[days_idx]:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[max(0, i - 1)] + costs[0],
                            dp[max(0, i - 7)] + costs[1],
                            dp[max(0, i - 30)] + costs[2])
                days_idx += 1
        return dp[-1]
