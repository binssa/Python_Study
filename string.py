python = "Python is Amazing"
print(python.lower()) # 소문자 변환
print(python.upper()) # 대문자 변환
print(python[0].isupper()) # 해당 문자 대문자인지 확인
print(len(python)) # 길이
print(python.replace("Python", "JAVA")) # 문자 대체
print(python)
index = python.index("n") # 위치 검색
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java")) # 없을 경우 -1 반환
# print(python.index("Java")) # 없을 경우 프로그램 종료

print(python.count("n"))