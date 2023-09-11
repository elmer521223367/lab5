import matplotlib.pyplot as plt

def main():
    print("Bienvenido al Laboratorio de Suma Acumulativa")
    
    while True:
        try:
            num_count = int(input("Ingrese la cantidad de números que desea sumar (entero positivo): "))
            if num_count > 0:
                break
            else:
                print("Por favor, ingrese un entero positivo.")
        except ValueError:
            print("Por favor, ingrese un entero positivo válido.")
    
    cumulative_sum = 0
    cumulative_sums = []
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']  # Lista de colores
    
    for i in range(num_count):
        while True:
            try:
                num = float(input(f"Ingrese el número {i+1}: "))
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        cumulative_sum += num
        cumulative_sums.append(cumulative_sum)
    
    print("Suma acumulativa:")
    for i, sum in enumerate(cumulative_sums):
        print(f"Número {i+1}: {sum}")
    
    plt.bar(range(1, len(cumulative_sums) + 1), cumulative_sums, color=colors[:len(cumulative_sums)])
    plt.xlabel("Número de entrada")
    plt.ylabel("Suma acumulativa")
    plt.title("Suma Acumulativa")
    plt.show()

if __name__ == "__main__":
    main()
