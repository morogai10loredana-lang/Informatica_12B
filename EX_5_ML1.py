a = float(input("Introdu a: "))
b = float(input("Introdu b: "))
c = float(input("Introdu c: "))
d = float(input("Introdu d: "))

i = int(input("Introdu i: "))
j = int(input("Introdu j: "))
k = int(input("Introdu k: "))
m = int(input("Introdu m: "))

sir = input("Introdu un sir de caractere: ")

x = int(input("Introdu un numar x: "))
y = int(input("Introdu un numar y: "))

def suma(a, b, c, d):
    return a + b + c + d

def media(i, j, k, m):
    return (i + j + k + m) / 4

def minim(a, b, c, d):
    return min(a, b, c, d)

def nr_vocale(sir):
    vocale = "aeiouAEIOU"
    return sum(1 for ch in sir if ch in vocale)

def nr_consoane(sir):
    vocale = "aeiouAEIOU"
    return sum(1 for ch in sir if ch.isalpha() and ch not in vocale)

def radacina(a, b):
    if a == 0:
        raise ValueError("Ecuație imposibilă")
    return -b / a

def cel_mai_mic_divizor(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i

def cmmdc(a, b):
    return math.gcd(a, b)

def cmmmc(a, b):
    return abs(a * b) // math.gcd(a, b)

def ultima_cifra(n):
    return abs(n) % 10

def nr_cifre(n):
    return len(str(abs(n)))

def cifra_superioara(n):
    return int(str(abs(n))[0])

def nr_aparitii(sir, c):
    return sir.count(c)



print("a) Suma =", suma(a, b, c, d))
print("b) Media =", media(i, j, k, m))
print("c) Minim =", minim(a, b, c, d))
print("d) Nr vocale =", nr_vocale(sir))
print("e) Nr consoane =", nr_consoane(sir))
print("f) Rădăcina ecuației ax+b=0, x =", radacina(a, b))
print("g) Cel mai mic divizor al lui", x, "=", cel_mai_mic_divizor(x))
print("h) CMMDC =", cmmdc(x, y))
print("i) CMMMC =", cmmmc(x, y))
print("j) Ultima cifră a lui", x, "=", ultima_cifra(x))
print("k) Nr cifre în", x, "=", nr_cifre(x))
print("l) Cifra superioară a lui", x, "=", cifra_superioara(x)) , c = input("Introdu un caracter: ")
print("m) Apariții ale caracterului", c, "în șir =", nr_aparitii(sir, c))