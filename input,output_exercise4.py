# word1 word2 word3를 입력받고 출력해주세요.

# 코드1

list1 = list(input().split())
print(*list1, end='')

# 코드2

number = int(input())
for i in range(1, number + 1):
    print(f"word{i}", end=' ')