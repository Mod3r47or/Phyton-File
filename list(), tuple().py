apple_tree_yields = 150, 210, 90, 120, 140, 190, 130, 150, 110, 210, 150

# Объявите функцию reversed_sort(), 
# которая вернёт отсортированный по убыванию кортеж.
def reversed_sort(apple_tree_yields):
    sorted_apple = sorted(apple_tree_yields, reverse=True)
    apple_tuple = tuple(i.split(",") for i in sorted_apple)
    return apple_tuple
# Присвойте этой переменной значение, 
# которое вернёт функция reversed_sort()
result = reversed_sort(apple_tree_yields)
# Напечатайте:
print(result[0]) #аибольшее значение из кортежа result,
print(result[1])  # второй элемент из кортежа result,
print(result[2])  # третий элемент из из кортежа result.

def print_pack_report(starting_value):
    # Дополните функцию
    for cake in range(1, starting_value, -1):
        if starting_value % 5 == 0 and starting_value % 3 == 0:
            print(f'{cake} - расфасуем по 3 или по 5')
        elif starting_value % 5 == 0 and starting_value % 3 != 0:
            print(f'{cake} - расфасуем по 5')
        elif starting_value % 5 != 0 and starting_value % 3 == 0:
            print(f'{cake} - расфасуем по 3')
        else:
            print(f'{cake} - не заказываем!')

print_pack_report(31)