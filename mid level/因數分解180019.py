#迴圈 對n 遍歷
#如果餘數為0，則輸出
#另n為10 會在 1,2,4,5,10 的時候 餘數為0
n = int(input("請輸入一個正整數: "))
for i in range(1, n+1):
    if n % i == 0:
        print(i)

