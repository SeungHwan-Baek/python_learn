#파일 읽기
# f_name ="file.txt"  # 파일 예외처리
f_name ="Test_file.txt"
try:
    f = open(f_name, 'r')
    data = f.read()
    print(data)
except :
    print("파일이 없어요~")   # 파일 미존재 시 except