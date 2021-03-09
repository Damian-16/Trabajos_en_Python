def conversor(tipo_pesos,valor_dolar):
    pesos = input("¿Cuantos Pesos "+tipo_pesos+"  tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares= round(dolares,2)
    dolares = str(dolares)
    print("Tienes $ "+ dolares + " dólares")

def run():

    menu = """
    Bienvenido al conversor de monedas ❤💲

    1 - Pesos colombianos
    2 - Pesos argentinos
    3 - Pesos mexicanos
    4 - Pesos bolivianos
    Elige una opción:"""


    opcion = int(input(menu))

    if opcion == 1:
        conversor("colombianos",3875)

    elif opcion == 2:
        conversor("argentinos",190)
    elif opcion == 3:
        conversor("mexicanos",24)
    elif opcion == 4:
        conversor("bolivianos",6.96)

    else:
        print('Ingresa una opcion Correcta')


if __name__ == '__main__':
    run()