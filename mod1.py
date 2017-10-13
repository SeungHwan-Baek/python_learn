# 구구단 Class

class  Gugudan:
    num1    = 0
    num2    = 0

    # 생성자
    def __init__(self):
        self.num1 =0
        self.num2 =0

    # 곱셈 출력 함수
    def show_Multiple(self,num1, num2):         # self는 선언시에만 있고 실제 입력 안함.
        for i in range(num2):
            i += 1
            print(num1,"*",i,"=",num1*i)


# 곱하기 함수
def f_Multi(num1, num2):
    return num1 *num2