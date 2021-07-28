# list []

# 지하철 칸별로 10명, 20명, 30명
subway = [10, 20, 30]
print(subway)

# 조세호가 몇번째 칸에 타고 있는가?
subway = ["유재석", "조세호", "박명수"]
print(subway.index("조세호"))

# 정준하가 다음 정류장에서 다음칸에 탐
subway.append("정준하")
print(subway)

# 정형돈이 유재석/조세호 사이에 탐
subway.insert(subway.index("조세호"), "정형돈")
print(subway)

# 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# List에 일치하는 항목 개수 
subway.append("유재석")
print(subway.count("유재석"))


num_list = [5,2,4,3,1]
print(num_list)
# 리스트 정렬
num_list.sort()
print(num_list)

# 리스트 순서 뒤집기
num_list.reverse()
print(num_list)

# 리스트 비우기
# num_list.clear()
# print(num_list)

# 리스트 확장
subway.extend(num_list)
print(subway)