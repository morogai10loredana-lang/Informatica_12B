import random
n=int(input('Cate valori sa aiba tuplul='))
t_n=tuple(random.randint(-100, 100) for i in range (n))
print('Tuplul generate:', t_n)

print('Primul element:', t_n[:1])

print('Ultimul element:', t_n[-1:])

print('Lungimea nr:', len(t_n))

print('Suma nr:', sum(t_n))

print('Maxim nr:', max(t_n))

print('Minim nr:', min(t_n))

print('Sortate crescator:', sorted(t_n))

print('Sortarea descrescator:', sorted(t_n, reverse=True))

print("Număr valori pozitive:", len([x for x in t_n if x > 0]))

print("Număr valori negative:", len([x for x in t_n if x < 0]))

pozitive=0
negative=0

for i in range(len(t_n)):
    if t_n[i] > 0:
        pozitive += 1
        
for i in range(len(t_n)):
    if t_n[i] < 0:
        negative += 1

print("Valori pozitive:", pozitive)
print("Valori negative:", negative)