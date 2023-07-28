import random

# 0번 당첨. 나머지 꽝
# 당첨 될 때까지 돌리기
TotalCnt = 0
GoodCnt = 0
BadCnt = 0

while GoodCnt < 1000000:
    result = random.randrange(0,5)
    TotalCnt += 1
    if result == 0:
        GoodCnt += 1
    else:
        BadCnt += 1
    print(TotalCnt)

print("Total: ", TotalCnt, "\nGood: ", GoodCnt, "\nBad: ", BadCnt, "\nGoodRatio: ", GoodCnt/TotalCnt)