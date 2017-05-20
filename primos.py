# -*- coding: utf-8 -*-

def prime_count(number):
    list_primes = ''
    flag_prime = False
    if number < 2:
        flag_prime = False
    elif number == 2:
        flag_prime = True
    elif number > 2 and number % 2 == 0:
        flag_prime = False
    else:
        for i in range(3, number):
            if number % i == 0:
                flag_prime = False

    flag_prime = True
    list_primes += str(number) + '---'
    return list_primes


def run():
    number = int(input('Escribe un número: '))
    result = prime_count(number)
    print('Los ${} numeros primos son: ${}'.format(number,result))


if __name__ == '__main__':
    run()