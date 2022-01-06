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
 
a = () # 이것이 바로 튜플이다
b = (1,) # 원소가 하나일때는 ,를 찍어줘야 튜플로 인식한다!
c = (11, 12, 13, 14)
d = (100, 1000,'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine')) # 튜플 안에 튜플도 중첩 선언이 가능하다

print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1]) # Captine으로 출력
print('e - ', e[-1][1]) # ('Ace', 'Base', 'Captine')에 첫번째이니깐 Base가 출력
print('e - ', list(e[-1][1])) # 튜플에서 리스트로 형변환

print('>>>>>')
#d[0] = 1500
print('d - ', d)

print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

print('>>>>>')
print('c + d - ', c + d)
print('c * 3 - ', c * 3)
#print("c[0] + 'hi' - ",c[0] + 'hi') # 튜플은 절대 never 수정,삭제가 안된다.
print("'Test' + c[0] - ", 'Test' + str(c[0])) # 따라서 수정하려면 형변환이 필요하다.

print('>>>>>')
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(5))
print('a - ', a.count(4))


print('>>>>>')
t = ('foo', 'bar', 'baz', 'qux')

# 1
(x1, x2, x3, x4) = t # 소괄호가 있어도 없어도 언패킹이 되지만, 관습상 소괄호를 해줘야한다~

# 출력확인
print(type(x1), type(x2), type(x3), type(x4))
print(x1)
print(x2)
print(x3)
print(x4)

# 2
(x1, x2, x3, x4) = ('foo', 'bar', 'baz', 'qux')

# 출력 확인
print(type(x1), type(x2), type(x3), type(x4))
print(x1)
print(x2)
print(x3)
print(x4)


print('>>>>>')

t2  = 1, 2, 3 # -> 따로 리스트나 자료형을 주지 않으면 자동으로 튜플로 팩킹이 된다.
t3 = 4, # -> 끝에 , 필수
x1, x2, x3 = t2

x4, x5, x6 = 4, 5, 6

# 출력 확인
print(t2)
print(t3)
print(x1,x2,x3)
print(x4,x5,x6)

print("*" * 50)

# key는 어떤 자료형이든 지정할수있다
a = {'name': 'Kim', 'phone': '01012345678', 'birth': '870124'} # {key : value}
b = {0: 'Hello python!'}
c = {'arr': [1, 2, 3, 4]} # key만 존재한다면 value는 어떠한 자료형태도 들어올 수 있다
d = {
	 'Name' : 'Niceman',
	 'City'   : 'Seoul',
	 'Age': '33',
	 'Grade': 'A',
	 'Status'  : True
}
e =  dict([
	 ( 'Name', 'Niceman'),
	 ('City', 'Seoul'),
	 ('Age', '33'),
	 ('Grade', 'A'),
	 ('Status', True)
])

f =  dict(
	 Name='Niceman',
	 City='Seoul',
	 Age='33',
	 Grade='A',
	 Status=True
)

# 출력
# 키에 해당하는 값을 가져올 때는 get 메소드를 가져오는 것이 안전하다
# Why? Error발생을 하지않고 None처리가 되기때문에
print('a - ', a['name'])  # 존재X -> 에러 발생
print('a - ', a.get('name'))  # 존재X -> None 처리
print('b - ', b[0])
print('b - ', b.get(0))
print('c - ', c['arr'])
print('c - ', c['arr'][3])
print('c - ', c.get('arr'))
print('d - ', d.get('Age'))
print('e - ', e.get('Grade'))
print('f - ', f.get('City'))


print("*" * 50)

# 바로 속성으로 접근해서 추가 또는 기존의 key가 있으면 수정이 되고 없으면 추가가 된다
a['address'] = 'seoul'
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# 또는 update() 함수 사용
a.update(birth = '910904')
print('a - ', a)
temp = {'address': 'Busan'}
a.update(temp)
print('a - ', a)

f.update(Age=36)
temp = {'Age': 27}
print('f - ', f)
f.update(temp)
print('f - ', f)

print("*" * 50)

print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())
print('a - ', list(a.keys())) # 리스트로 형 변환
print('b - ', list(b.keys()))
print('c - ', list(c.keys()))
print('d - ', list(d.keys()))

# 차후 배울 for 문으로도 출력 가능함
for key in a.keys():
	print(key)

print("*" * 50)

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print('d - ', d.values())
print('a - ', list(a.values()))
print('b - ', list(b.values()))
print('c - ', list(c.values()))
print('d - ', list(d.values()))
 
print("*" * 50)
 
print('a - ', a.items())
print('b - ', b.items())
print('c - ', c.items())
print('d - ', d.items())
print('a - ', list(a.items()))
print('b - ', list(b.items()))
print('c - ', list(c.items()))
print('d - ', list(d.items()))

print("-"*50)

print('a - ', a.pop('name')) # pop()함수는 리스트의 마지막에 있는 요소를 리턴하고 그 요소는 삭제하는 함수
print('a - ', a)
print('b - ', b.pop(0))
print('b - ', b)
print('c - ', c.pop('arr'))
print('c - ', c)
print('d - ', d.pop('City'))
print('d - ', d)

print("-"*50)

print('f - ', f.popitem()) # popitem()함수는 임의의 데이터(key,value)을 리턴하고 삭제 (데이터가 없으면 오류)
print('f - ', f.popitem()) # 추첨기 만들때 유용
print('f - ', f.popitem())
print('f - ', f.popitem())
print('f - ', f.popitem())

print("-"*50)

print('a - ', 'name' in a)
print('a - ', 'addr' in a)
