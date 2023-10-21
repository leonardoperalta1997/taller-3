Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> numero1 = int(input("Introducir primer numero: "))
... numero2 = int(input("Introducir segundo numero: "))
... numero3 = int(input("Introducir tercer numero: "))
... print("")
... 
... if numero1 < numero2 and numero1 < numero3:
...     menor = numero1
... elif numero2 < numero1 and numero2 < numero3:
...     menor = numero2
... else:
...     menor = numero3
... 
