"""
Este módulo calcula estadísticas descriptivas (media, mediana, moda, varianza y desviación estándar)
a partir de un archivo de datos.
"""

import sys
import argparse
import os
import time
from utils.file_processor import process_file


def compute_statistics(numbers):
    """Calcula la media, mediana, moda, varianza y desviación estándar de una lista de números."""
    n = len(numbers)
    mean = sum(numbers) / n

    sorted_numbers = sorted(numbers)
    median = sorted_numbers[n // 2] if n % 2 != 0 else (
        sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

    mode = max(set(numbers), key=numbers.count)

    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_dev = variance ** 0.5

    return mean, median, mode, variance, std_dev


def process_file_and_compute_statistics(file_path):
    """Procesa el archivo y calcula las estadísticas."""
    try:
        items = process_file(file_path)
        numbers = []
        for item in items:
            try:
                numbers.append(float(item))
            except ValueError:
                print(f"Warning: '{item}' is not a valid number and will be ignored.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except OSError as e:
        print(f"An OS error occurred: {e}")
        sys.exit(1)
    # except Exception as e:
    #     print(f"An unexpected error occurred: {e}")
    #     sys.exit(1)

    if not numbers:
        print("Error: No valid numbers found in the file.")
        sys.exit(1)

    return compute_statistics(numbers)


def main():
    """Función principal para analizar argumentos y calcular estadísticas."""
    parser = argparse.ArgumentParser(
        description="Compute descriptive statistics from a file containing numbers.")
    parser.add_argument('file_path', nargs='?', default='ComputeStatistics/data/test_file.txt',
                        help='Path to the file containing the list of items')
    args = parser.parse_args()

    file_path = args.file_path

    start_time = time.time()

    mean, median, mode, variance, std_dev = process_file_and_compute_statistics(file_path)

    end_time = time.time()
    elapsed_time = end_time - start_time

    results = (
        f"Mean: {mean}\n"
        f"Median: {median}\n"
        f"Mode: {mode}\n"
        f"Variance: {variance}\n"
        f"Standard Deviation: {std_dev}\n"
        f"Time Elapsed: {elapsed_time:.2f} seconds\n"
    )

    print("Descriptive Statistics:")
    print(results)

    # Ensure the directory exists
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
    os.makedirs(output_dir, exist_ok=True)

    # Save the results to the file in the data directory
    output_file_path = os.path.join(output_dir, 'StatisticsResults.txt')
    with open(output_file_path, "w", encoding="utf-8") as f:
        f.write(results)


if __name__ == "__main__":
    main()
