import sys

input = sys.stdin.readline


def fibo_dp(n):
    global cnt

    fibo = [1] * (n + 1)

    for i in range(3, n + 1):
        cnt += 1
        fibo[i] = fibo[i - 1] + fibo[i - 2]

    return fibo[n]


n = int(input())
cnt = 0

print(fibo_dp(n), cnt)
