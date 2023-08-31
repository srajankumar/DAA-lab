def knapsack(weight, cost, N, W):
    sol, selected = [[0]*(W+1) for _ in range(N+1)], [0]*(N+1)
    for i in range(1, N+1):
        for j in range(1, W+1):
            sol[i][j] = sol[i - 1][j] if weight[i] > j else max(
                sol[i - 1][j], sol[i - 1][j - weight[i]] + cost[i])
    i, j = N, W
    while i > 0 and j > 0:
        if sol[i][j] != sol[i - 1][j]:
            selected[i], j = 1, j - weight[i]
        i -= 1
    print("\nThe Optimal Solution is:", sol[N][W])
    print("Items selected are:", [i for i in range(N + 1) if selected[i]])


# Predefined values
N = 4
weight = [0, 2, 3, 4, 5]
cost = [0, 10, 20, 30, 40]
W = 10
knapsack(weight, cost, N, W)
