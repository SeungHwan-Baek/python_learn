#파일 읽기 readline
# f_name ="file.txt"  # 파일 예외처리
f_name ="Test_file.txt"
try:
    f = open(f_name, 'r')

    while True :
        l_data = f.readline()
        if not l_data :         # 읽은 라인이 없으면 종료
            break
        else :
            print(l_data)
except :
    print("파일이 없어요~")   # 파일 미존재 시 except