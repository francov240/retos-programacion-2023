"""
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
"""

def prime_fibo_odd():
    number = input("Enter your number:")
    number = int(number)
    is_prime = True
    is_fibo = True
    is_odd = True
    if number % 2 != 0:
        is_prime = False
    

fibo_list = [0, 1]
n = 1
def fibo_generator(fibo_list, n): ##Hace falta pasar por referencia la lista y el 
    while(n < 100):
        fibo_list = fibo_list.append([n-1]+[n])
        n = n + 1
        print(fibo_list)
        print(n)
        fibo_generator(fibo_list, n)

fibo_generator(fibo_list, n)
