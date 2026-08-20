print('=' * 55)
n = int(input('Digite um número (999 para encerrar): '))
s = 0
d = 0

if n == 999:
    print(f"Nenhum número foi digitado.")
else:
    while True:
        s += n
        d += 1
        n = int(input('Digite mais um número (999 para encerrar): '))
        if n == 999:
            break

    if d == 1:
        print('=' * 55)
        print(f"Foi digitado {d} número e soma total é {s}.")
        print('=' * 55)
    else:
        print('=' * 55)
        print(f"Foram digitados {d} números e soma total deles é {s}.")
        print('=' * 55)