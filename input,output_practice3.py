# 문제 3
# 문자열을 입력받고, e 를 제거한 결과를 출력하세요.

# 단, replace() 메서드는 사용하지 마세요.

# 출력 예시 1
# 문자열을 입력하세요 > apple # 사용자 입력
# appl
# 출력 예시 2
# 문자열을 입력하세요 > hello # 사용자 입력
# hllo
# 출력 예시 3
# 문자열을 입력하세요 > hEllo # 사용자 입력
# hEllo

# 코드

char = input()
char_re = ''

for i in char:
    if i != 'e':
        char_re += i
print(char_re)