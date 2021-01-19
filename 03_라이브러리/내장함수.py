# 내장 함수
# 별도의 import 명령어 없이 사용 가능
# imput(), print(), sum(), min(), max(), eval(), sorted()

result = [1, 2, 3, 4, 5]
str = "(1 + 2) * 3"

print(sum(result))
print(min(result))
print(max(result))
print(eval(str))

# sorted() 함수 보다는 iterable 객체에 내장된 sort() 함수를 사용함
# 이 경우 바로 내부 값이 변경됨s