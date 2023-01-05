# 문제 2
# 문자열을 입력 받고, 문자열 중 알파벳 모음의 총 개수를 출력하세요.

# 알파벳 모음 : a(A) e(E) i(I) o(O) u(U)

# 단, count() 함수는 사용하지마세요.

# 출력 예시 1
# 문자열을 입력하세요 > hello # 사용자 입력
# 2
# 출력 예시 2
# 문자열을 입력하세요 > aeiouAEIOU # 사용자 입력
# 10
# 출력 예시 3
# 문자열을 입력하세요 > bcd # 사용자 입력
# 0

# 코드

char = input('문자열을 입력하세요 > ')
list1 = list(char)
list2 = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
cnt = 0

for i in list1:
    for j in list2:
        if i == j:
            cnt += 1
print(cnt)