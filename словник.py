w = input("Введіть слово: ").replace(" ", "")

s = int(input("Введіть число через скільки буде братися буква: "))

t1 = ''.join(w[i] for i in range(1, len(w), 2))
t2 = ''.join(w[i] for i in range(1, len(w), 3))
t3 = ''.join(w[i] for i in range(2, len(w), 4))
t4 = ''.join(w[i] for i in range(3, len(w), 5))

if s == 1:
    print("Через одну букву: ", t1)
elif s == 2:
    print("Через дві букви: ", t2)
elif s == 3:
    print("Через три букви: ", t3)
else:
    print("Через чотири букви: ", t4)
