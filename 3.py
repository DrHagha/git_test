a = []
b = list()
c = [70, 70, 70, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f  = [3, 'foobar', 3, 3, 'bark', False, 3.14159]

print('>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1]) # e에서 -1은 ['Ace', 'Base', 'Captine'] 이 중에서 1번이니깐 Base가 출력
# 중첩된 리스트에 접근할 때는 첫번째 리스트 안에서 그 리스트에 접근한 후 중첩된 리스트의 인덱스 번호를 입력해줘야
# 정확한 값이 출력이 된다!
# 문자열 -> list 타입 변환
print('e - ', list(e[-1][1]))

print('>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

print('>>>>>>')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
print("'Test' + c[0] - ", 'Test' + str(c[0]))

print('>>>>>>')

c = [70, 75, 80, 85]

print(c == c[:3] + c[3:]) 
# a[x:y]는 x부터 y-1번째까지 포함. 즉, c[:3]는 0부터 2번째까지
print(c)
print(c[:3])
print(c[3:])

# 기본적인 수정 방법
c = [70, 75, 80, 85]

print('>>>>>>')

c[0] = 4
print('c - ', c)

c[1] = ['a', 'b', 'c'] # 슬라이싱에서 범위를 지정 하나의 원소로 들어간다 # [['a', 'b', 'c']]
print('c - ', c)

c[1:2] = ['a', 'b', 'c'] 
print('c - ', c)

c[1:3] = []
print('c - ', c)

# List 함수를 활용한 수정 방법
a = [5, 2, 3, 1, 4]
print('a - ', a)

a.append(6) # append 함수는 마지막 끝부분에 데이터를 삽입할 때 쓰는 함수
print('a - ', a)

a.sort() # sort 함수는 리스트에 들어있는 데이터를 오름차순으로 정렬을 해주는 함수
print('a - ', a)

a.reverse() # reverse 함수는 리스트에 들어있는 데이터를 내림차순으로 정렬해주는 함수
print('a - ', a)

print('a - ', a.index(5))

# insert(index 번호, 내가 추가할 값)는 리스트의 index 번호에 위치한 내가 원하는 값을 삽입하는 함수

# Phython에서는 숫자를 0부터 시작한다

a.insert(2, 7)
print('a - ', a)

# 삭제 방법
a = [5, 2, 3, 1, 4]

del a[3] # 삭제

print('a - ', c)

a.remove(2) # remove(x)는 리스트에서 첫 번째로 나오는 x를 삭제하는 함수

print('a - ', a)
print('a - ', a.pop()) # pop()함수는 리스트의 마지막에 있는 요소를 돌려주고 그 요소는 삭제하는 함수
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4)) # count(x)함수는 리스트 안에 x가 몇 개가 중복되어 있는지 찾을 때 또는 있는지 없는지를 확인할 때

ex = [8, 9]
a.extend(ex)
print('a - ', a)

# 차후 배울 while 문으로 모든 리스트 삭제
while a:
	data = a.pop()
	print(data)