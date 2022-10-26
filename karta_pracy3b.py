#zad1
print("Pn\tBt\tSr\tCzw\tPi\tSob\tNd\t")
j = 1
print("\t", end = "")
for i in range(1,31):
    print(i, end="\t")
    j+=1
    if j == 7:
        print()
        j = 0
print()

#zad2

#n=(int(input()))
#for i in range(n):
#    if n%2 !=1:
#        print(i**2)
#    else:
#        print()

#zad3

#for i in range(1000,10001):
#    if i % 379 == 0:
#        print(i)
#zad4
#for i in range(100, 1001):
#    if i % 5 == 0 or i % 6 ==0 or i % 11 == 0:
#        print(i)

#zad5

#n = int(input())
#suma = 0
#for i in range(1,n+1):

#    liczba = int(input())
#    suma += liczba

#print(suma)

#zad6

#k = int(input())
#su = 0
#for i in range(2,(k*2)+2,+2):
#    su += i
#print(f'suma:{su}')

#zad7

#k = int(input())
#su = 0
#for i in range(10,(k * 2 + 2)+2,+2):
#    su += i
#print(f"sum:{su}")

#zad8

#Kwotastart = int(input())
#LInwest = int(input())
#KwotaEnd = 0 
#for i in range(0, LInwest * 12):
#    KwotaEnd = Kwotastart * 0.06 * (1/12)
#    Kwotastart += KwotaEnd
#print(f"wartosc:{Kwotastart}")

#zad9

#IlLiczb = int(input())
#j = 21
#su = 0
#for a in range(0,IlLiczb+1):
#    for b in range(0,a,j):
#        print(j)
#        su += j
#        j += 100
#print(f'suma = {su}')

#zad10

#from math import sqrt
#for i in range(1,1000):
#    if i % 10 == sqrt(i):
#        print(i)
#    elif i % 100 == sqrt(i):
#        print(i)
    
