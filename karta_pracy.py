

#a = int(input())
#b = int(input())

#if ((a+b)%2) == 0:
#    print("liczba jest parzysta")
#else:
#    print("liczba nie jest parzysta")

#zad2
#a = int(input())
#b = int(input())
#from math import sqrt
#if ((a+b)/2) < sqrt(a*b):
#    print("Tak")
#else:
#    print("Nie")

#zad3
#a = int(input())
#b = int(input())
#c = int(input())
#print((a+b+c)/3)
#if a == b or b == c or a == c:  
#    if a == b:  
#        print("Tak a = b")
#    if b == c:
#        print("Tak b = c")
#    if a == c: 
#        print("Tak a = c")
#else:
#    print("nie")
#zad4
#a = int(input())
#b = int(input())
#c = int(input())
#d = int(input())
#if a < b and a < c and a < d:
#    print("a jest najmniesze")
#elif b < a and b < c and b < d:
#    print("b jest najmniesze")
#elif c < a and c < b and c < d:
#    print("c jest najmniesze")
#elif d < a and d < b and d < c:
#    print("d jest najmniesze")
#zad5
#a = int(input())
#b = int(input())
#c = int(input())
#if a - b < c < a + b and b - c < a < b + c and a - c < b < a + c: 
#    print("Tak")
#else:
#    print("Nie")
#zad6
a = int(input())
b = int(input())
c = int(input())
if a + b > c and b + c > a and c + a > b:
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        print("prosto-")
    elif a**2 + b**2 < c**2 or b**2 + c**2 < a**2 or a**2 + c**2 < b**2:
        print("rozwarto-")
    elif a**2 + b**2 > c**2 or b**2 + c**2 > a**2 or a**2 + c**2 > b**2:
        print("ostro-")
else:
    print("z podanych bokow nie da sie utworzyc trojkata")




