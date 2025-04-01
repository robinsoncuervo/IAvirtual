import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_fft(signal, num_samples=1000):
    """
    Aproxima la Transformada Rápida de Fourier (FFT) mediante el método de Monte Carlo.
    
    Parameters:
        signal (np.array): Señal de entrada.
        num_samples (int): Número de muestras aleatorias para la aproximación.
    
    Returns:
        np.array: Aproximación de la FFT de la señal.
    """
    n = len(signal)
    indices = np.random.randint(0, n, size=num_samples)  # Selección aleatoria de índices
    fft_values = np.zeros(n, dtype=complex)
    
    for k in range(n):
        sum_value = 0
        for i in indices:
            sum_value += signal[i] * np.exp(-2j * np.pi * k * i / n)
        fft_values[k] = sum_value / num_samples  # Promedio de las muestras seleccionadas
    
    return fft_values

# Ejemplo de uso
n_points = 256
x = np.linspace(0, 2*np.pi, n_points)
signal = np.sin(5 * x) + 0.5 * np.sin(20 * x)  # Señal de prueba

# FFT estándar
fft_standard = np.fft.fft(signal)

# FFT Monte Carlo
fft_mc = monte_carlo_fft(signal, num_samples=500)

# Visualización
plt.figure(figsize=(12, 6))
plt.plot(np.abs(fft_standard), label='FFT Estándar', linestyle='--')
plt.plot(np.abs(fft_mc), label='Monte Carlo FFT', linestyle=':')
plt.legend()
plt.xlabel('Frecuencia')
plt.ylabel('Magnitud')
plt.title('Comparación de FFT Estándar vs Monte Carlo FFT')
plt.show()