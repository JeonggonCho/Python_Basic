# 예제 1
# 리스트
# 반복문

# 코드

list_variable = [0, 1, 2, 3, 4, 5, 6]
list_variable.pop() # 마지막 리스트 요소제거
list_variable.append(7)
list_variable.append(8) # 7과 8 리스트 요소추가

for element in list_variable[2:]:
    print(element, end=" ") # 2인덱스 요소부터 줄바꿈 없이 출력
    
"""
예측을 작성하세요.
?
2 3 4 5 7 8
"""