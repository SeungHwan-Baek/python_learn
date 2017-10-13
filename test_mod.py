# 모듈 호출 test
import mod1                 # mod1.py 모듈을 호출
from mod1 import Gugudan    # mod1.py 모듈의 Gugudan 객체 직접 호출
from mod1 import f_Multi    # mod1.py 모듈의 f_Multi 매소드 호출

print("mod1.Gugudan()")
c = mod1.Gugudan()          # mod1.Gugudan() 객체 생성
c.show_Multiple(3,10)       # mod1.show_Multipl(3,10) 매소드 실행


print("\nGugudan()")
d = Gugudan()               # mod1을 붙일 필요가 없다.
d.show_Multiple(3,10)


print("\nf_Multi()")
num1 = 3
num2 = 4
print(num1,"*",num2,"=",f_Multi(3,4))
