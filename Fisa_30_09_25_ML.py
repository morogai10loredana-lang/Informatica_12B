x,y=int(input('a=')), int(input('b='))

def suma_ab (a,b):
    return a+b

def produs_ab(a,b):
    return a*b

def media_ab(a,b):
    return(a+b)/2

def max_ab(a,b):
    return max(a,b)

def min_ab(a,b): 
    return min(a,b)

def radacina_ab(a,b):
    return -b/a 

def cmmdc_ab(a,b):
    while b!=0: 
        a,b=b,a%b
    return a

def cmmmc_ab(a1,b1):
    return abs(a1*b1)//cmmdc_ab(a1,b1)

print('a) Suma numerelor=',suma_ab(x,y))
print('b) Produsul numerelor=',produs_ab(x,y))
print('c) Media a numerelor=', media_ab(x,y))
print('d) Maximul numerelor-',max_ab(x,y))
print('e) Minimul numerelor=',min_ab(x,y))
print('f)',x,'+',y,'=', suma_ab(x,y))
print('g)',x,'*',y,'=', produs_ab(x,y))
print('h) (,x,'+',y,)/2=', media_ab(x,y))
print('i) Rădăcina ecuației ax+b=0:', radacina_ab(x,y))
print('j) CMMDC=',cmmdc_ab(x,y))
print('k) CMMMC=', cmmmc_ab(x,y))