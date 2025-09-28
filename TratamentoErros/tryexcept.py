try: 
    a = int(input("Digite um numerador: "))
    b = int(input("Digite um denominador: "))
    result = a / b
    print(result)
except ZeroDivisionError:
    print("Erro: Divisão por zero")
except ValueError:
    print("Erro: Digite um numero inteiro")
except Exception as erro:
    print(f"Erro: {erro}")
