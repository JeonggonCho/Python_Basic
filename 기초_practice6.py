# 문제
# 정수형 숫자 두 개를 입력 받고, 두 정수형 숫자에 대한 아래 산술 연산
# 결과를 출력하세요.

# - 산술연산
# 1. 더하기
# 2. 빼기
# 3. 곱하기
# 4. 몫
# 5. 나머지

number1 = int(input('첫 번째 정수형 숫자를 입력해주세요 > '))
number2 = int(input('두 번째 정수형 숫자를 입력해주세요 > '))

print('더하기 연산 :',number1 + number2)
print('빼기 연산 :', number1 - number2)
print('곱하기 연산 :', number1 * number2)
print('몫 연산 :', number1 // number2)
print('나머지 연산 :', number1 % number2)