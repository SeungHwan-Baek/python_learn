#파일 읽기 readlines
# f_name ="file.txt"  # 파일 예외처리
f_name ="Test_file.txt"
try:
    f = open(f_name, 'r')

    l_data = f.readlines()      # 라인전체 읽어서 리스트에 넣음
    print("l_data type is ",type(l_data))
    for data in l_data:
        print(data)

except :
    print("파일이 없어요~")     # 파일 미존재 시 except