# 예제 10
# 리스트
# 조건문

# 코드

n = 10
total = 0

for number in range(0, n + 1): # range는 0부터 10까지의 요소를 가진 리스트
    if number % 2 == 0:
        total += number * 2 # number가 짝수면, number에 2를 곱해서 total에 더해라
    elif number % 2 == 1:
        total += number + 1 * 3 # number가 홀수면, number에 3을 더하고 total에 더해라 

print(total) # ? 100