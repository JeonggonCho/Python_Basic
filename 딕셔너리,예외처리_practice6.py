# 문제 6
# 문자열을 입력받고, 문자열에서 개별 문자가 나오는 횟수를 출력하세요.

# 출력 예시 1
# 문자열을 입력하세요 > hello # 사용자 입력
# h 1
# e 1
# l 2
# o 1
# 출력 예시 2
# 문자열을 입력하세요 > else # 사용자 입력
# e 2
# l 1
# s 1

# 코드

char = input('문자열을 입력하세요 > ')
char_list = list(char)
list1 = {}

for i in char_list:
    if i not in list1:
        list1[str(i)] = 1
    else:
        list1[str(i)] += 1
        
for letter in list1:
    print(letter, list1[letter])