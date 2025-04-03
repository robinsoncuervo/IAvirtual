def celsius_a_fahrenheit(celsius):
    """
    Convierte grados Celsius a Fahrenheit.
    Fórmula: (Celsius * 9/5) + 32
    """
    return (celsius * 9/5) + 32

def main():
    print("Conversor de Celsius a Fahrenheit")
    try:
        celsius = float(input("Introduce los grados Celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print(f"{celsius}°C son {fahrenheit}°F")
    except ValueError:
        print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    main()