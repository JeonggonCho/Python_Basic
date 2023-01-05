# 예제 3
# 딕셔너리

# 코드

dict_variable = {}
dict_variable["apple"] = 5000
dict_variable["banana"] = 3000
dict_variable["apple"] = 2000 # apple 값 변환
dict_variable["banana"] = dict_variable["banana"] + 1000 # banana기존 값 + 1000

print(dict_variable["apple"] + dict_variable["banana"]) # ? 6000