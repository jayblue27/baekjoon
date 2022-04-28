# 백준 - 기타줄
# 기타에서 N개의 줄이 끊어짐
import math

# 입력
# 1. 기타줄의 개수 N과 기타줄 브랜드 M
N, M = map(int, input().split())

# 2. M개의 기타줄 패키지(6개) 가격, 낱개의 가격
# 함정.... 한 브랜드에서만 사라는 법은 없다.
tmp = 0
arr = []

# 각 브랜드에서 패키지 최소가, unit 최소가 찾은 뒤 최소값 찾기 계산한다.
# 각각의 최소값 찾기
package_arr = []
unit_arr =[]
for _ in range(M):
    package, unit = map(int, input().split())
    package_arr.append(package)
    unit_arr.append(unit)

package = min(package_arr)
unit = min(unit_arr)

# 계산 및 출력
# 줄수가 6개 미만이면 패키지 1개 사는게 싼지, 낱개로만 사는게 싼지 비교하면 되고
if N < 6:
    res = min(package, unit*N)
# 줄수가 6개이상이면 패키지로만 사는게 싼건지, 패키지랑 낱개를 섞어서 사는게싼건지,  낱개로만 싸는게 싼건지 비교
else:         
    res = min((package * math.ceil(N/6)), (package * (N//6)) + (unit * (N%6)) , unit*N)

print(res)