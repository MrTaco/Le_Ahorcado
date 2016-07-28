def nodeguiones (palabra):
	guiones=[]
	for letra in palabra:
		guiones.append("_")
	return guiones

def encuentraletras(opc, guiones,palabra,encontrado):
	for i in range (len(palabra)):
		if list(palabra[i])==opc:
			encontrado=True
			return guiones[i].append(opc)
			return encontrado
	return encontrado

def muneco(contar):
	mun=["(*.*) \n"+"/"+" | "+"\ \n"+ "  |\n"+ " /"+" \ "]
	for i in range(contar):
		return mun[i]