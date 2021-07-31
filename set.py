# 집합 Set
# 중복 불가, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)

# set 생성방법
java = {"김띠또", "사띠또", "양띠또"}
python = set(["유띠또", "박띠또", "김띠또"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# 추가
python.add("최띠또")
print(python)

# 제거
java.remove("양띠또")
print(java)