import sys

# 為了防止遞迴深度過深導致堆疊溢位（Stack Overflow），特別是當 x 很大時。
# Python 預設的遞迴深度限制約為 1000。根據題目可能的最大 x 值來調整。
# 如果 x 可能超過 1000，建議適當調高。
sys.setrecursionlimit(2000) # 設定一個比預設值更高的限制，防止 x 較大時爆掉

# 記憶化字典：用來儲存已經計算過的值
# 這是關鍵！它將時間複雜度從指數級降到線性級 O(x)
memo = {}

def f(x):
    # 基本情況 (Base Cases): 當 x 在 1 到 4 之間時
    if x <= 0:
        # 處理非法的輸入。雖然題目暗示 x 會是正整數，
        # 但穩健的程式碼會考慮這種情況。
        # 這裡返回 0 或拋出錯誤都可以，取決於題目對非法輸入的要求。
        return 0
    if x <= 4:
        return x

    # 檢查是否已經計算過這個 x 的值
    if x in memo:
        return memo[x]

    # 遞迴步驟 (Recursive Step): 當 x > 4 時
    # 這裡的迴圈正確地實現了 f(x-1)*1 + f(x-2)*2 + f(x-3)*3 + f(x-4)*4
    result = 0
    # range(1, 5) 會產生 1, 2, 3, 4
    for i in range(1, 5):
        # 這裡呼叫自身 f(x-i)，並乘以對應的 i
        result += f(x - i) * i

    # 將計算結果存入記憶化字典，下次再需要 f(x) 時直接返回
    memo[x] = result
    return result

# 讀取輸入
input_x = int(input())

# 輸出結果
print(f(input_x))