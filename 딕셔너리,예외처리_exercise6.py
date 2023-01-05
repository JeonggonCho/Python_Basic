# 예제 6
# 딕셔너리

# 코드

dict_variable = {
    "이름": "정우영",
    "생년월일": "19000101",
    "회사": "하이퍼그로스",
}

# in 연산자는 boolean타입의 연산자로 데이터가 있는 경우 True를,
# 없는 경우 False를 출력
# 지금 리스트의 키에는 이름, 생년월일,회사 만 있고
# "나이" 가 없으므로 False
print("나이" in dict_variable) # ? False