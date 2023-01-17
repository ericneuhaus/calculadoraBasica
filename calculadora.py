import os #Usando apenas para limpar a tela

while True:
    os.system("cls")
    str_num1 = input("Digite o primeiro número: ") #Solicita primeiro número

    if str_num1.isnumeric():
        int_num1 = int(str_num1) #Converte a entrada do usuário que é do tipo "str" para "int"
        str_num2 = input("Digite o segundo número: ") #Solicita o segundo número

        if str_num2.isnumeric():
            int_num2 = int(str_num2) #Converte a entrada do usuário que é do tipo "str" para "int"
            operador = input("digite o operador: ") #Solicita o operador
            os.system("cls")

            if operador == "+":
                print(int_num1 + int_num2)
            elif operador == "-":
                print(int_num1 - int_num2)
            elif operador == "/":
                print(int_num1 / int_num2)
            elif operador == "*":
                print(int_num1 * int_num2)
            else:
                print("Operador inválido!")


            sair = input("Digite 's' para sair ")
            
            if sair == "s" or sair == "S":
                break