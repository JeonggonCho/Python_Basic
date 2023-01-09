# 문제 2
# 문자열을 입력받고, 각 단어의 등장 횟수를 출력하세요.

# 단, count() 메서드는 사용하지마세요.

# 출력 예시 1
# 문자열을 입력하세요 > hello # 사용자 입력
# hello 1
# 출력 예시 2
# 문자열을 입력하세요 > hello hypergrowth # 사용자 입력
# hello 1
# hypergrowth 1
# 출력 예시 3
# 문자열을 입력하세요 > apple apple banana grape # 사용자 입력
# apple 2
# banana 1
# grape 1

# 코드

list1 = input().split()
chars = {}

for word in list1:
    if word not in chars:
        chars[word] = 1
    else:
        chars[word] += 1
for word2 in chars:
    print(word2, chars[word2])