from functions import sum_ignore_non_numbers, is_triangle, average, common_strings

items = [1, 2, 'Hey', None, 4.3]
sum_ignore_non_numbers(items)

is_triangle(2, 4, 9)
is_triangle(3, 4, 5)

average(1, 2, 3, 4, 5, 6, 7, 8)
average()

fruits_1 = ['banana', 'APPLE', 'watermelon', 'cherry']
fruits_2 = ['Mango', 'apple', 'orange', 'cherry']

common_strings(fruits_1, fruits_2)

text = input("Введите текст:").lower()
final_text = ''
for i in range(len(text)):
    if i % 2 == 0:
        final_text = final_text + text[i].upper()
    elif i % 2 != 0:
        final_text = final_text + text[i]
print(final_text)
