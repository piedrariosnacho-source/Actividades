producto = 170
pagado = 0

while pagado < producto:
	moneda = int(input("Introduce una moneda de 10, 20, 50 o 100 centimos: "))

	if moneda == 10 or moneda == 20 or moneda == 50 or moneda == 100:
		pagado = pagado + moneda
		print(f"Quedan {producto - pagado} monedas")
	else:
		print("moneda no aceptada")

	if pagado >= producto:
		cambio = pagado - producto
		print("Producto entregado")
		print("cambio:", cambio)
		break
