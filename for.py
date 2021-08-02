for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no2 in range(0, 5):
    print("대기번호 : {0}".format(waiting_no2))


customers = ["일리", "이리", "삼리", "사리"]
for customer in customers:
    print("{0}님 준비 완료되었습니다.".format(customer))



students = ["iron man", "thor", "i am groot"]
students = [len(name) for name in students]
print(students)

from random import *
taxi_customer = [randint(5, 51) for i in range(0,50)]
count = 0
for i in range(1, 51):
    use_time = randint(5, 51)
    if use_time >= 5 and use_time <=15:
        available = "O"
        count += 1
    else :
        available = " "
    print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(available, i, use_time))
print("총 탑승 가능한 손님은 {0} 명입니다.".format(count))
print(taxi_customer)