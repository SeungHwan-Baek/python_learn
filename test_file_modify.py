# 파일 수정
f_name = "Test_file.txt"

print("***수정 전 출력***")
f = open(f_name,'r')
l_data= f.readlines()
for data in l_data:
    print(data)
f.close()

print("***라인 추가***")
f = open(f_name,'a')
f.write("무궁화 삼천리 화려 강산\n")
f.write("대한 사람 대한 으로 길이 보전하세")
f.close()

# 수정한 파일 출력
print("***수정 후 출력***")
f = open(f_name,'r')
l_data= f.readlines()
for data in l_data:
    print(data)
f.close()
