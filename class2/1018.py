#입력 처리
NM = list(input().split())
N = int(NM[0])
M = int(NM[1])
board = []
for i in range(N) :
    board += [input()]

#이차원 리스트 생성
WB = []
BW = []
for i in range(N) :
    for j in range(N) :
        WB[i][j] += []
for i in range(N) :
    for j in range(M) :
        BW[i][j] = 0