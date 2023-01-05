# 예제 2
# 딕셔너리

# 코드

dict_variable = {"a": "A", "B": "b"}
dict_variable["c"] = "C"
dict_variable["D"] = "d"
dict_variable["e"] = "E"
# dict_variable = {"a": "A", "B": "b", "c":"C", "D": "d", "e": "E"}

# 리스트의 키(key)를 통해 출력되며, 값을 넣을 경우 에러
print(dict_variable["a"]) # ? A
print(dict_variable["D"]) # ? d
print(dict_variable["b"]) # ? 에러