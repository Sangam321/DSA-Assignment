def find_minimum_cost(costs):
    if not costs or not costs[0]:
        return 0
    venues = len(costs)
    themes = len(costs[0])
    #  dynamic programming table
    dp = [[0] * themes for _ in range(venues)]
    for j in range(themes):
        dp[0][j] = costs[0][j]
    # Dynamic programming approach 
    for i in range(1, venues):
        for j in range(themes):
            dp[i][j] = float('inf')
            for prev_j in range(themes):
                if j != prev_j:
                    dp[i][j] = min(dp[i][j], dp[i - 1][prev_j] + costs[i][j])
    # Finding the minimum cost 
    min_cost = float('inf')
    for j in range(themes):
        min_cost = min(min_cost, dp[venues - 1][j])
    return min_cost
if __name__ == "__main__":
    costs = [[1, 3, 2], [4, 6, 8], [3, 1, 5]]
    result = find_minimum_cost(costs)
    print("Minimum cost to decorate all venues:", result)
