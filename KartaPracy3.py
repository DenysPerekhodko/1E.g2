# print(list(range(10)))
# print(list(range(5)))
# print(list(range(2,10)))
# print(list(range(12,10,-1)))
# print(list(range(1,10,2)))

# for i in range(10):
#   print(i*2, end="\t")

# l = [0,1,2,3,4,5,6]
# print(l[1:6:2])

# for i in range(10, 22):
#   print(i, end=" ")

#for i in range(15, 31): print( )
# Ankieta
# User wprowadza dwie liczby. 
# Sprawdz czy druga jest 
# o ponad 30% większa niż pierwsza
# WE: p, q
# WY: TAK/NIE

# p, q = int(input()), int(input())
# if (1.3*p > q):
#     print("TAK")
# else:
#     print("NIE")

# pętla liczb dwucyfrowych od 10 do 21

# pętla liczb dwucyfrowych nieparzystych od 15 do 31  
#for i in range(15,32): print(i)
# pętla liczb dwucyfrowych malejąco (step ujemny)
#for i in range(99,9,-1): print(i)
# pętla liczb dwucyfrowych malejąco (step dodatni)
#for i in range(10,100): print(i)
# pętla liczb 3-cyfrowych podzielnych przez 20
#for i in range(100,1000,20): print(i, end=" ")
#for i in range(5,50,1): print(i*20, end=" ")
#print(list(range(15,31)))
#zad1
# i=int(input())
# for n in range(i):
# print(n**3+3)
#zad2
#for i in range(100,1000,15): print(i, end=" ")
#zad3
# n=int(input())
# for i in range(1,n+1):
#   if n%i==0:
#     print(i,end=" ")
#zad4
# s=0
# for i in range(10,100):
#   s=s+i
# print(s)
#zad5
 # n=int(input())
 # print(n*(n+1)//2)
# for i in range(n-1):
#   x=int(input())
#   s=s-x
# print("nie podałeś:",s)  
#zad6
# n=int(input())
# a=0
# b=1
# print(a, end=",")
# print(b, end=",")
# for i in range(n-2):
#   a, b=b , a+b
#   print(b, end=" ")
for i in range(99,1001,371):
    print(i)
