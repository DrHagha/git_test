print('*' * 50)

str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print("Capitalize: ", str_o1.capitalize()) # 첫번째 시작 문자를 대문자로 바꿔주는 함수
print("endswith: ", str_o2.endswith("s")) # 마지막 문자가 무엇인지 체크할때 사용하는 함수
print("join str: ", str_o1.join(["I'm ", "!"])) # 리스트에 특정 구분자를 추가하여 문자열을 변환하는 함수
print("replace1: ",str_o1.replace("thon", ' Good'))
print("replace2: ", str_o3.replace("are", "was"))
print("sorted: ", sorted(str_o1)) # 문자열을 입력받아 기준에 맞게 정렬한 후 리스트 형태로 반환하는 함수
print("split: ", str_o4.split(' ')) # 특정 단어를 분리할때, 단어 단위나 문장 단위로 분리할 때 많이 사용하는 함
print("reversed1: ", reversed(str_o2))
print("reversed2: ", list(reversed(str_o2))) # list 형 변환

print('*' * 50)

im_str = "Good Boy!"

# 출력
for i in im_str:
	print(i)
 
print('*' * 50)
 
str_sl = "Nice Python"

# 슬라이싱 연습
print(str_sl[0:3]) # [start : end] []안에 시작과 끝 인덱스를 지정하면 해당 범위의 리스트를 잘라서 갖고온다.
# 주의할 점 end인덱스는 가져오려는 범위에 포함되지 않는다. 실제로 가져오려는 인덱스보다 1을 더 크게 지정한다.

print(str_sl[5:]) # str_sl[5:11]
print(str_sl[:len(str_sl)]) # str_sl[:11]이랑 같은것
print(str_sl[:len(str_sl)-1]) # str_sl[:10] 이니깐 0~9까지만 가져왔기때문에 'n'을 출력못함.
print(str_sl[1:9:2]) # [start:end:step] 몇개 단위로 점프(skip)하면서 가져올건지
print(str_sl[-5:]) # 음수가되면 오른쪽부터 출력된다.
print(str_sl[1:-2])
print(str_sl[::2]) # 처음부터 끝까지 2칸씩 간격으로 가져온다
print(str_sl[::-1]) # Nice Python이 역으로 출력된다.

# 중요 -> 음수는 오른쪽에서 왼쪽으로 일반적인 방향은 0부터 오른쪽으로

print('*' * 50)

im_str = "Good Boy!"
print(dir(im_str)) # __iter__가 있으면 시퀀스를 반복할 수 있다는 것!

