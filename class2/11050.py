NK = list(input().split())
N = int(NK[0])
K = int(NK[1])
result = 1
resultF1 = 1

if N == 1 :
    print(1)

elif K == 0 or K == N :
    print(1)

else:
    for i in range(N - K) :
        result *= (N - i)
    for j in range(N - K) :
        resultF1 *= (j+1)

    print(int(result/resultF1))