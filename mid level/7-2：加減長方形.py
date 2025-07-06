#輸入兩個正整數 l 和 w，交錯使用「+」和「-」輸出一個長寬分別為 l 和 w 的長方形。
#+結束 下一行會式-開始 反之亦然
I = int(input())
W = int(input())
symbol = ['+', '-']

def start_with_plus(I):
    for i in range(I):
        if i % 2 ==0:
            print(symbol[0], end = '')
        else:
            print(symbol[1], end = '')

# def start_with_minus(I):
#     if I % 2 == 1: #代表他是奇數

def start_with_minus(I):
    for i in range(I):
        if i % 2 ==0:
            print(symbol[1], end = '')
        else:
            print(symbol[0], end = '')


#判斷從哪個開始



#判斷I是偶數嗎
if I % 2 == 0:
    for i in range(W):
        start_with_plus(I)
        print('')
else:
    start_with_plus(I)
    print("")
    for i in range(W-1):
        if i % 2 ==0:
            start_with_minus(I)
            print('')
        else:
            start_with_plus(I)
            print('')