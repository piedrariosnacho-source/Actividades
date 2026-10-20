precio = float(input("cuánto vale?:"))
unidades = int(input("cuántas unidades son?"))
porc_descuento = float(input("cuánto descuento tiene"))
IVA = 0.21

subtotal = precio * unidades
descuento = subtotal * (porc_descuento / 100)
total_IVA = (subtotal - descuento) * IVA
total = (subtotal - descuento) * IVA_total

print(f"el subtotal es:{subtotal:.2f}")
print(f"el descuento es:{descuento:.2f}")
print(f"el total_IVA es:{total_IVA:.2f}")
print(f"el total es:{total:.2f}")

envio_gratis = 100
tipo = "gratuito" if total >= 100 else "no gratuito"