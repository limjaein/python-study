# 주요 사용 클래스는 permutations, combinations
from itertools import permutations
from itertools import product
from itertools import combinations
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(permutations(data, 2))
print(result)

# permatations 와 같이 순열이지만 중복 허용의 경우
# product 를 사용한다
result = list(product(data, repeat=2))
print(result)

result = list(combinations(data, 2))
print(result)

# combinations 와 같이 조합이지만 중복 허용의 경우
# combinations_with_replacement 를 사용한다
result = list(combinations_with_replacement(data, 2))
print(result)