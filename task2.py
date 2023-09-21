# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле



def sort_list_declarative(numbers):
      sorted_numbers = sorted(numbers, reverse=True)
      print(sorted_numbers)  # вывод отсортированного списка
      return sorted_numbers

numbers = [1, 2, 4, 6, 7, 9]
sort_list_declarative(numbers)