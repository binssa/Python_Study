# 사전 
# Key - Value의 형태로 저장
# Key에 대한 중복 허용하지 않음

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet)
print(cabinet[3]) # 대괄호를 통해서 value 가져오기
print(cabinet[100])
# print(cabinet[5]) # 없는 값을 출력 시 프로그램 종료

print(cabinet.get(3)) # get()을 통해 value 가져오기
print(cabinet.get(5)) # None 출력 
print(cabinet.get(5, "사물함 사용가능")) # 기본 출력 메세지 설정 가능

print(3 in cabinet) # in을 통해서 값을 포함했는지 확인 가능
print(5 in cabinet)

# Key 값은 문자열도 가능
cabinet_string = {"A-3":"강호동", "B-100":"이승기"}
print(cabinet_string)
cabinet_string["C-12"] = "규현"
print(cabinet_string)
# Key 값은 중복되지 않아 수정됨.
cabinet_string["C-12"] = "박명수"
print(cabinet_string)

# 삭제 가능
del cabinet_string["C-12"]
print(cabinet_string)

# key만 출력
print(cabinet_string.keys())

# value만 출력
print(cabinet_string.values())

# Key, value 쌍으로 출력
print(cabinet_string.items())

# 비우기
cabinet_string.clear()
print(cabinet_string)