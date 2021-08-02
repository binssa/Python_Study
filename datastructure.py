menu = {"커피", "우유", "주스"} # set
print(menu, type(menu))

menu = list(menu) # List로 변경
print(menu, type(menu))

menu = tuple(menu) # Tuple로 변경
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

from random import * 

# 1명은 치킨, 3명은 커피
id_list = list(range(1, 21)) # 1~20 까지 생성
print(id_list)
shuffle(id_list)
print(id_list)
winners = sample(id_list, 4)
print(winners)
print(" --- 당첨자 발표 --- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" ------------ ")