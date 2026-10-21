
def palindromo(x):
    original = x
    inv = 0

    while x > 0:
        r = x % 10
        x = x // 10
        inv = (inv * 10) + r

    return original == inv


numero = int(input("Ingresa un numero: "))

if numero >= 0:
    if palindromo(numero):
        print("El numero es palindromo")
    else:
        print("El numero no es palindromo")
else:
    print("Ingresa un numero no negativo")
