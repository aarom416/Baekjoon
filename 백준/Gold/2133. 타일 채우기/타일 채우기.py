n = int(input())
dp=[0]*(31)
dp[2]=3
for i in range(4,31,2):
    dp[i]=dp[i-2]*3 + 2*sum(dp[:i-2]) + 2
    #i-2번째에 3*1 타일로 만들 수 있는 경우인 3을 곱한 것과
    #i가 6부터 2개씩 추가로 더 생김 0 ~ i-4까지의 타일 뒤에 자신을 붙혀 만들 수 있는 2가지 경우와
    #->(dp[0]+dp[1]+dp[2]+...dp[i-4])*2
    #가로의 길이가 i짜리 새로운 타일 덩어리를 만드는 2가지의 경우의 합과 같음
print(dp[n])
