# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

numbers = [4, 2, 5, 0, 1, 9]

def sort_list_imperative (numbers):
    flag = True
    while flag:
        flag = False
        for i in range(len(numbers) - 1):
            if numbers[i + 1] > numbers[i]:
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp
                flag = True
    print(numbers)

def sort_list_declarative (numbers):
    numbers.sort(reverse=True)
    print(numbers)


# sort_list_imperative(numbers)
sort_list_declarative(numbers)