"""
enunciado
"""

edad = input("Introduce tu edad: ")
edad = int(edad)

if edad < 4:
    print("El precio de la entrada es 0")
elif 4 <= edad <= 18: #edad >= 4 and edad <= 18:
    print("El precio de la entrada es 5€")
else:
    print("El precio de la entrada es 10€")