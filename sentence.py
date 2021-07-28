sentence = '문자열입니다.'
print(sentence)
sentence2 = "큰따옴푶문자열입니다"
print(sentence2)

sentence3 = """
여러줄의 문자열입니다,
이렇게 작성하고있어요.
"""
print(sentence3)

jumin = "990120-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[:2]) # 0번째부터 2번째 직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리(뒤부터): " + jumin[-7:])
###
# PYTHON project https://www.youtube.com/watch?v=8ext9G7xspg&ab_channel=freeCodeCamp.org