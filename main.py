#создаем метод print_string_n_times
def print_string_n_times(string, n):
    if n > 0:
        print(string)
        print_string_n_times(string, n-1)

input_string = input("Введите строку: ")
num_times = int(input("Введите количество повторений: "))

#вызываем метод print_string_n_times
print_string_n_times(input_string, num_times)