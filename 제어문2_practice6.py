# 문제 6
# 양의 정수만 저장한 리스트가 주어집니다.

# 리스트에 저장된 정수 중 가장 큰 값을 출력하세요.

# 단, max() 함수는 사용하지 마세요.

# 코드

number_list = [1, 18, 10, 5]
A = 0

for B in number_list:
    if A < B:
        A = B
print(A)