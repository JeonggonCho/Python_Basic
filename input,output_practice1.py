# 문제 1
# 문자열을 입력받고, e 가 처음 나오는 위치(index)를 출력하세요.

# 만약, 문자열에서 e 가 없으면 -1 을 출력하세요.

# 단, index() / find() 메서드는 사용하지마세요.

# 출력 예시 1
# 문자열을 입력하세요 > hello # 사용자 입력
# 1
# 출력 예시 2
# 문자열을 입력하세요 > hEllo hypergrowth # 사용자 입력
# 9
# 출력 예시 3
# 문자열을 입력하세요 > java # 사용자 입력
# -1

# 코드

cnt = 0
chars = input()

if 'e' not in chars:
    print('-1')
else:
    for i in chars:
        if i == 'e':
            print(cnt)
        cnt += 1