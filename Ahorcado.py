from lista_palabras import lista_palabras
from funciones import nodeguiones, encuentraletras, muneco
import random
numero = random.randint(0, 999)
palabra=(lista_palabras(numero))
print(palabra)
guiones=nodeguiones(palabra)
contar=0
encontrado=False
jugar="si"
estado="perdido"
print ("Bienvenido: escoja las letras que cree que le pertenecen a la palabra e ingreselas.")
print (guiones)
while jugar=="si":
	win=False
	while win==False:
		opc=input("Ingrese Letra: ")
		print (guiones)
		encuentraletras(opc,guiones,palabra,encontrado)
		print(encontrado)
		if encontrado==False:
			print (muneco(contar))
			contar=contar+1
		if contar==7:
			win=True
		if list(palabra)==guiones:
			win=True
			estado="ganador"
	print("Usted ha "+ estado)		
	jugar=input("Desea seguir jugando si/no: ")