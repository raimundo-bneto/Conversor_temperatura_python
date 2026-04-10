def celsius_para_fahrenheit(celsius) :
    resultado = (celsius * 9/5) + 32
    return resultado

def celsius_para_kelvin(celsius) :
    resultado = (celsius + 273.15)
    return resultado

continuar = "S"
while continuar == "S" :
        print ("Conversor de temperatura (Celsius para outras escalas)")
        celsius = float(input("Digite o valor de graus celsius: "))
        fahr = celsius_para_fahrenheit(celsius)
        kelv = celsius_para_kelvin(celsius)
        opcao = input("Digite F, para converter fahrenheit ou K, para converter kelvins: ").strip().upper()
        while opcao != "F" and opcao != "K":
             print ("Opção inválida")
             opcao = input("Digite F, para converter fahrenheit ou K, para converter kelvins: ").strip().upper()


        if opcao == "F":
            print(f"{celsius:.2f} °C são: {fahr:.2f} Fahrenheit")

        elif opcao == "K":
            print(f"{celsius:.2f} °C são: {kelv:.2f} Kelvin")

        continuar = input('Deseja realizar outra conversão? Se sim, digite "S", caso não queira, digite qualquer tecla: ').strip().upper()
        if continuar != "S" :
             print("Obrigado pela utilização!")




