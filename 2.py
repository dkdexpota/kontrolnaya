class MyException(Exception):
    pass


def putin(funk):
    def put_in(v0,v1,t):
        funk(v0,v1,t)
        s=float(v0*t+((v1-v0)*t)/2)
        print(s)
    return put_in

@putin

def speed(v0,v1,t):
    a=float((v1-v0)/t)
    print(a)

try:
    v2=input()
    v3=input()
    t1=input()
    v0=int(v2)
    v1=int(v3)
    t=int(t1)
    if t<=0:
	    raise MyException('Время должно быть больше 0')
except ValueError:
    print('ВВедены данные неправильного типа')
except MyException:
    print('Время должно быть больше 0')
else:
    speed(v0,v1,t)



