# 입출력

# 문자열 한줄 입력
# input()

# 띄어쓰기로 구분하여 각각 정수 자료형 데이터로 저장
list_data = list(map(int, input().split()))
print(str)

# 세가지 정수를 동시에 받는다면
n, m, k = map(int, input().split())
print(n)

# input() 은 속도가 느리기 때문에, 입력 개수가 많은 경우엔 사용하지 않음
# 입력 개수가 많을 경우, sys.stdin.readline() 함수를 이용
# 이 함수를 사용할 땐 rstrip() 함수를 꼭 호출해야함 ; 엔터 공백 문자를 제거하기위
import sys
input = sys.stdin.readline().rstrip()
print(input)

# 정수 출력 시 더하기 연산자로 문자열처럼 더할 수 없음
# print(2 + "입니다") X
num = 2
print(str(num) + "입니다.")