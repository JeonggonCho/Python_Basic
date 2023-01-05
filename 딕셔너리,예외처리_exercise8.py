# 예제 8
# 에러가 발생한 원인을 작성하세요.
# 리스트
# 예외처리

# 코드

list_variable = []

try:
    list_variable.append(0) # 리스트에 0추가
    list_variable.append(1) # 리스트에 1추가
    list_variable.append(2) # 리스트에 2추가 -> [0, 1, 2]
    print(list_variable[3]) # 리스트 인덱스3번 출력
    
except:
    print("에러가 발생했습니다.")
    print("에러의 원인은 무엇인가요?")

"""
출력 결과를 예측해서 작성하세요.
?
에러가 발생했습니다.
에러의 원인은 무엇인가요?
"""
# 인덱스가 0~2까지 생성되어있는데 3을 출력하고자 함