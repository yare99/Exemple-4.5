def animarme():
    nombre = input("Introdueix un nom: ")
    for letra in nombre:
        print("Dame una", letra.upper())
    print(nombre.upper())

def calcular():
    operacion = input("Introdueix una operació: ")
    try:
        resultado = eval(operacion)
        print("Resultat:", resultado)
    except:
        print("Operació invàlida")

while True:
    print("Menu:")
    print("1. Animarme")
    print("2. Calcular")
    print("3. Sortir")
    
    opcion = input("Selecciona una opció: ")

    if opcion == "1":
        animarme()
    elif opcion == "2":
        calcular()
    elif opcion == "3":
        break
    else:
        print("Opció invàlida. Torna a seleccionar una opció.")