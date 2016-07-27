from lista_palabras import lista_palabras
from funciones import nodeguiones, encuentraletras, muneco
import random
numero = random.randint(0, 999)
palabra=(lista_palabras(numero))
print(palabra)
guiones=nodeguiones(palabra)
print (guiones)
q=1
jugar="si"
mun=["(°°) \n"+"/"+" | "+"\ \n"+ "   |\n"+ " /"+" \ "]
print (mun)
print ("Bienvenido: escoja las letras que cree que le pertenecen a la palabra e ingreselas.")
while jugar=="si":
	win=False
	while win==False:
		opc=input("Ingrese Letra: ")
		encuentraletras(opc, guiones,palabra)
		print(encontrado)
		if encontrado==False:
			q=q+1
			print muneco(mun,q)
	jugar=input("Desea seguir jugando si/no: ")