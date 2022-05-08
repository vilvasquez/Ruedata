
#Importo ASCII Text Libreria
from optparse import Option
from termcolor import cprint , colored
from pyfiglet import figlet_format,Figlet

# ascii texto
f = Figlet(font='slant')
print(f.renderText('walther vasquez'))


print('''
**********************
*Solucion Fibonacci * 
**********************
'''
)

# Soluciono la secuencia de Fibonacci 

def fibonacci(n):
	if n == 1 or n == 0:
		return n + 0 or n + 1

	else:
		return fibonacci(n-2) + fibonacci(n-1)

numero = int(input("Ingrese el numero 10: "))

if numero < 0:
	print("Numero no valido")
	
	i = 0

print("Sucesión de fibonacci")

for i in range(0, numero):
	print(fibonacci(i))