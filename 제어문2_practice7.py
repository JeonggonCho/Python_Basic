# 문제 7
# 양의 정수만 저장한 리스트가 주어집니다.

# 리스트에 저장된 정수 중 가장 작은 값을 출력하세요.

# 단, min() 함수는 사용하지 마세요.

# 코드

number_list = [100, 6, 3, 120, 5]
A = number_list[0]

for B in number_list:
    if A > B:
        A = B
print(A)