# 문제 4
# 문자열과 알파벳을 공백으로 구분해서 입력받고,문자열에서 입력한
# 알파벳의 개수를 출력하세요.

# 단, count() 메서드는 사용하지마세요.

# 출력 예시 1
# 문자열을 입력하세요 > apple p # 사용자 입력
# 2
# 출력 예시 2
# 문자열을 입력하세요 > hello o # 사용자 입력
# 1
# 출력 예시 3
# 문자열을 입력하세요 > hEllo a # 사용자 입력
# 0

# 코드

a, b = input().split()
cnt = 0

for i in a:
    if i == b:
        cnt += 1
print(cnt)