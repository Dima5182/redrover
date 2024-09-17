n = int(input())
if n % 2 == 0:
    print("Четное число")
else:
    print("Нечетное число")

day = input()
if day == "суббота" or day == "воскресенье":
    print("Сегодня выходной!")
elif day == "среда":
    print("Мне сегодня к стоматологу в 15:30")
else:
    print("Сегодня обычный день.")

n = int(input())
text = input()
for i in range(n):
    print(text)

message = input()
counter = 0
for c in message:
    if c in "аеёиоуыэюя":
        counter = counter + 1
print(counter)

n = int(input())
sum = 0
while n >= 0:
    sum = sum + n
    n = int(input())
print(sum)
