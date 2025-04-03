from datetime import datetime

def calcular_edad():
    print("Calculadora de Edad")
    print("Ingrese su fecha de nacimiento en formato dd/mm/aaaa")
    
    while True:
        try:
            fecha_nac_str = input("Fecha de nacimiento (dd/mm/aaaa): ")
            fecha_nac = datetime.strptime(fecha_nac_str, "%d/%m/%Y")
            hoy = datetime.now()
            
            # Calculamos la edad
            edad = hoy.year - fecha_nac.year
            
            # Ajustamos si aún no ha pasado el cumpleaños este año
            if (hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day):
                edad -= 1
                
            print(f"\nSu edad es: {edad} años")
            break
            
        except ValueError:
            print("Formato incorrecto. Por favor ingrese la fecha en formato dd/mm/aaaa.")

# Ejecutar el programa
if __name__ == "__main__":
    calcular_edad()