#Wersja1
# n = int(input())
# for i in range(2,n):
#   if n % i == 0:
#     print("l. nie jest pierwsza")
#     exit(0)
# print("l. jest pierwsza")

#Wersja2
# n = int(input())
# for i in range(2,n):
#   if n % i == 0:
#     flaga = False
# if flaga == True:
#   print("Liczba jest pierwsza")
# else:
#   print("iczba nie jest pierwsza")

#Wersja3
# def czyPierwsza(n):
#   flaga=True
#   for i in range (2,n):
#     if n%i==0:
#       flaga=False
#   return flaga
# print()

#Wersja4
# from math import sqrt
# n=int(input())
# for i in range(2,n):
#   if n%i==0:
#     print("Liczba nie jest pierwsza")
#     exit(0)
# print("liczba jest pierwsza")