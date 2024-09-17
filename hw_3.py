numbers = []
for i in range(101):
    if i % 2 == 0 and i % 3 == 0:
        numbers.append(i)
print(numbers)

numbers2 = [i for i in range(101) if i % 2 == 0 and i % 3 == 0]
print(numbers2)

items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
numbers = []
for i in items:
    if type(i) is int or type(i) is float:
        numbers.append(i)
print(sum(numbers))

messages = []
flag = True
while flag == True:
    n = input()
    messages.append(n)
    if len(messages) > 5:
        del messages[0]
    if n == 'Пока':
        print('ну ладно, пока!')
        print(messages)
        break

numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
numbers2 = set(numbers)
numbers3 = list(numbers2)
print(sorted(numbers3))

numbers = [15, 3, 8, 42, 3, 23, 8, 7, 42, 1, 9, 23, 15, 5, 9, 4, 6, 1]
numbers2 = []
for i in numbers:
    if i not in numbers2:
        numbers2.append(i)
print(sorted(numbers2))

age = 16
admin = True

if age >= 18 or admin == True:
    print("Доступ разрешен!")
else:
    print("Доступ запрещен!")

products = {
"apple": {"quantity": 10, "price": 100},
"banana": {"quantity": 20, "price": 50},
"orange": {"quantity": 15, "price": 80},
"grape": {"quantity": 8, "price": 120},
"milk": {"quantity": 12, "price": 90},
"bread": {"quantity": 30, "price": 40}
}

for product in products.values():
    product["price"] = product["price"] * 1.2
del products["milk"]
products["salt"] = {"quantity": 7, "price": 12}
sum = 0
for product in products.values():
    sum = sum + (product["price"] * product["quantity"])

print(sum)

keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education',
'company', 'salary']

values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890',
'Reading', 'Masters in Computer Science', 'TechCorp', 90000]

dictionary = {}
for i in range(len(keys)):
    dictionary[keys[i]] = values[i]

print(dictionary)

str1 = '2__234йшDGмёшSDFжкъrrrщзнSDF78юкйфуSDFшёью$#2Sшжйи3%узфsdf34нкфыvvя'
str2 = ""

cipher = {
"а": "щ", "б": "д", "в": "ю", "г": "ф", "д": "з", "е": "м", "ё": "р",
"ж": "т", "з": "п", "и": "я", "й": "с", "к": "н", "л": "э", "м": "к",
"н": "л", "о": "ё", "п": "ж", "р": "ц", "с": "б", "т": "у", "у": "в",
"ф": "о", "х": "и", "ц": "х", "ч": "г", "ш": "е", "щ": "й", "ъ": "ы",
"ы": "ч", "ь": "ш", "э": "ъ", "ю": "а", "я": "ь"
}

for char in str1:
    if char in cipher:
        str2 = str2 + cipher[char]
print(str2)

new_cipher = {}

for key, value in cipher.items():
    new_cipher[value] = key

message = input()
encrypted_message = ""

for c in message:
    if c in new_cipher:
        encrypted_message += new_cipher[c]

print(encrypted_message)

text = """Doc: Запомни! Согласно моей теории, ты помешал знакомству
своих родителей.
Если они не встретятся, то не влюбятся, не поженятся, и у них не будет детей.
Поэтому твой старший брат исчезает с фотографии. Затем очередь твоей
сестры,
и если ты все не исправишь, ты будешь следующим.
Marty: Тяжелый случай.

Doc: Вес тут совершенно ни при чем. """
count = {}
for c in text.lower():
    if c in 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя':
        count.setdefault(c, 0)
        count[c] = count[c] + 1
print(count)
max_number = max(count.values())
print(max_number)
for key, value in count.items():
    if max_number == value:
        print(key)
        break