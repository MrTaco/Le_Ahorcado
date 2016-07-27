def nodeguiones (palabra):
	guiones=[]
	for letra in palabra:
		guiones.append("_")
	return guiones

def encuentraletras(opc, guiones,palabra):
	encontrado=False
	for i in range (len(palabra)):
		if palabra[i]==opc:
			return guiones[i].append(opc)
			return encontrado=True

def muneco(mun,q):
	for i in q:
		return muneco[i+1]