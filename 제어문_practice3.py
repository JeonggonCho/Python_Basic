# 문제
# 정수 한 개를 입력 받고, 해당 정수가 1보다 크고, 10보다
# 작으면 True, 그렇지 않다면 False를 출력하세요.

# 코드

num1 = int(input('정수를 입력하세요 > '))
if num1 > 1:
    if num1 < 10:
        print('True')
    else:
        print('False')