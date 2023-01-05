# 문제 1
# 문자열을 입력 받고 문자열에서 e 의 개수를 구해서 출력하세요.

# 단, count() 함수는 사용하지마세요.

# 출력 예시 1
# 문자열을 입력하세요 > hello # 사용자 입력
# 1
# 출력 예시 2
# 문자열을 입력하세요 > hello hypErgrowth # 사용자 입력
# 1

# 코드

char = input('문자열을 입력하세요 > ')
list1 = list(char)
cnt = 0

for i in list1:
    if i == 'e':
        cnt += 1
print(cnt)