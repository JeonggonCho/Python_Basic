# 문제 4
# 정수만 저장한 리스트가 주어집니다.

# 리스트에 저장된 정수들의 평균을 출력하세요.

# 단, len() / sum() 함수는 사용하지 마세요.

# 코드

number_list = [2, 3, 5, 7]
i = 0
k = 0

for j in number_list:
    i += float(j)
    k += 1
print(i / float(k))