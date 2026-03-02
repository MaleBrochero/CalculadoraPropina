## Calculadora de propina y total a pagar
nombre_cliente= input("Por favor ingrese su nombre ")
precio_comida = float(input("Ingrese el valor a pagar incluyendo decimal ejemplo: 14.85 "))

if precio_comida < 20 :
    total=precio_comida+(precio_comida*0.10)
    print( nombre_cliente , "su total a pagar es " ,total)

elif precio_comida >= 20 and precio_comida <= 50 :
    total=precio_comida+(precio_comida*0.15)
    print( nombre_cliente , "su total a pagar es " ,total)

else:
    total=precio_comida+(precio_comida*0.20)
    print( nombre_cliente , "su total a pagar es " ,total)