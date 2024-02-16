# 入力
N = int(input("材料の種類数: "))
Q = list(map(int, input("各材料の量: ").split()))
A = list(map(int, input("料理Aに必要な各材料の量: ").split()))
B = list(map(int, input("料理Bに必要な各材料の量: ").split()))

# 最大人数を初期化
max_people = 0

# 料理Aと料理Bの人数の組み合わせを全探索
for i in range(min(Q[k] // A[k] for k in range(N)) + 1):
    for j in range(min(Q[k] // B[k] for k in range(N)) + 1):
        # 材料が足りるかどうかを判定
        enough = True
        for k in range(N):
            if Q[k] < A[k] * i + B[k] * j:
                enough = False
                break
        # 材料が足りる場合は、人数の最大値を更新
        if enough:
            max_people = max(max_people, i, j)

# 結果を出力
print("最大で合計", max_people, "人分の料理を作れます。")
