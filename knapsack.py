n=int(input("Enter the value:"))
wt=list()
for i in range(n):
    value=int(input(f"The weight are {i+1}:"))
    wt.append(value)
print("The weight list:",wt)
prof=list()
for i in range(n):
    next_Value=int(input(f"The profit are {i+1}:"))
    prof.append(next_Value)
mx=int(input("Enter the maximum capacity:"))
dp=[[0 for _ in range(mx+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for w in range(1,mx+1):
        if wt[i-1]<=w:
            dp[i][w]=max(dp[i-1][w],dp[i-1][w-wt[i-1]]+prof[i-1])
        else:
            dp[i][w]=dp[i-1][w]
print("\n Maximum profit is:",dp[n][mx])
print("\n The dp table:")
for row in dp:
    print(*row)

