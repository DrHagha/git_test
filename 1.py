# example
print('Python Start!') # '',""이 두개를 많이 사용한다.
print("Python Start!")
print('''Python Start!''') # 잘 사용하진 않지만 기초문법이니깐 알아두자!
print("""Python Start!""")

print('P', 'Y', 'T', 'H', 'O', 'N', sep= '')
print('010', '7777', '1234', sep='-')
print('python', 'google.com', sep='@')

print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

print("python" + "hello")

print('%s %s' % ('one','two')) # s는 문자열 d는 숫자이다.
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
print(f'{"one"} {"two"}') # 최근에 개발된 방법이다.

print('%10s' % ('nice')) # %10s의 의미는 10개의 자리수를 의미 출력해보면 앎
print('%-10s' % ('nice') + "hi") # 음수인 경우 오른쪽부터 공백을 채우고 난 뒤 나머지 입력한 텍스트로 채워진다.
print('%.5s' % ('pythonstudy')) # 점을 붙이면 내가 원하는 자릿수만큼 왼쪽부터 다섯 글자만 절삭해서 출력한다.

print('{:>10}'.format('nice'))
print('{:10}'.format('nice')) # > 기호가 생략되면 오른쪽을 공백으로 채운다.
print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice')) # 중앙정열은 ^표시를 해주면 알아서 위치시킨다.

print('%d %d' % (1,2))
print('{} {}'.format(1,2))
print('%4d' % (42))
print('{:4d}'.format(42))

print('%f' % (3.14343434343)) #이때 %f를 %d로 바꾸면 소숫점 아래 숫자가 생략되고 3만 출력된다.
print('{:f}'.format(3.14343434343))
print('%06.2f' % (3.141592653589793)) # 총 자릿수는 6이고 6개중에 정수부는 1자리기 때문에 나머지를 0으로 채워주고 소수부 2자리이니깐 2개가 나온것. --> 003.14
print('{:06.2f}'.format(3.141592653589793))


n = 700 #변수의 값을 할당한다.
print(n)
print(type(n)) #type함수는 변수 n에 있는 값의 자료형을 보여준다.

x = y = z = 700
print(x, y, z)

# 기본선언
var = 75

# 재선언
var = "Change Value"

# 출력
print(var)
print(type(var))

n = 777
print(n, type(n))

m = 400
print(m, n)
print(type(m), type(n))

t = type(n)

print(type(t))

m = 800
n = 800

print(id(m))
print(id(n))
print(id(m)==id(n))