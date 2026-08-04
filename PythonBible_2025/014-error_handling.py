



def calculadora():
    while True:
        try:
            num1 = float(input("Primer número: "))
            operacion = input("Operación (+ - * /): ")
            num2 = float(input("Segundo número: "))
            
            if operacion == '+':
                resultado = num1 + num2
            elif operacion == '-':
                resultado = num1 - num2
            elif operacion == '*':
                resultado = num1 * num2
            elif operacion == '/':
                if num2 == 0:
                    raise ZeroDivisionError("No se puede dividir por cero")
                resultado = num1 / num2
            else:
                raise ValueError(f"Operación '{operacion}' no válida")
            
            print(f"Resultado: {resultado}")
            break
            
        except ValueError as e:
            print(f"Error de valor: {e}. Intenta de nuevo.")
        except ZeroDivisionError as e:
            print(f"Error matemático: {e}. Intenta de nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}. Intenta de nuevo.")