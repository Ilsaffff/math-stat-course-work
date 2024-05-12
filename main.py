import numpy as np
from scipy.stats import chisquare


def read_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            values = line.strip().split()
            values = [float(value) for value in values[:-1]]
            data.append(values)
    return np.array(data)


def chi_square_test(data):
    chi_square_results = []
    for column in data.T:
        chi2_stat, p_val = chisquare(column)
        chi_square_results.append((chi2_stat, p_val))
    return chi_square_results


def display_results(chi_square_results):
    for i, (chi2_stat, p_val) in enumerate(chi_square_results):
        print(f"Столбец {i + 1}:")
        print(f"  - Статистика хи-квадрат: {chi2_stat}")
        print(f"  - p-значение: {p_val}")
        if p_val < 0.05:
            print("    * p-значение меньше 0.05, отвергаем нулевую гипотезу")
        else:
            print(
                "    * p-значение больше или равно 0.05, нет оснований отвергать нулевую гипотезу")
        print()


def main():
    file_path = "-0.15V_sp892.dat"
    data = read_data(file_path)
    chi_square_results = chi_square_test(data)
    display_results(chi_square_results)


if __name__ == "__main__":
    main()
