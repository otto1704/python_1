def verificar_temp(temp):
    if temp < 20:
        return "Máquina Fria"
    elif temp >= 20 and temp <= 30:
        return "Temperatura Normal"
    elif temp >= 31 and temp <= 40:
        return "Máquina Quente"
    else:
        return "Perigo: Superaquecimento!"

print ("Monitor iniciado. Digite 0 para desligar.")

while True:
    try: 
        temp_atual = int(input("Digite a temperatura: "))
        if temp_atual == 0:
            print ("Monitor Desligado")
            break

        resultado = verificar_temp(temp_atual)

        print (resultado)
    except ValueError:
        print ("Erro: Digite apenas números inteiros!")
