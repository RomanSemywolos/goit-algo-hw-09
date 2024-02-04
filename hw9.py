import timeit
import random

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    count_coins = {}

    # Проходимося по кожному номіналу монети в списку
    for coin in coins:
        # Визначаємо кількість монет даного номіналу, яку можна використати
        count = amount // coin

        # Якщо кількість монет більше 0, то додаємо їх до словника
        if count > 0:
            count_coins[coin] = count

        # Віднімаємо вартість використаних монет від суми
        amount -= count * coin

    # Повертаємо словник з кількістю монет кожного номіналу
    return count_coins


def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    # Визначаємо максимально можливу кількість монет заданого номіналу
    max_coins = amount // min(coins)

    # Створюємо список для зберігання мінімальної кількості монет для кожної суми
    min_coins = [max_coins] * (amount + 1)
    min_coins[0] = 0  # Базове значення для нульової суми

    # Створюємо список для зберігання значення номіналу монети для кожної суми
    selected_coins = [0] * (amount + 1)

    # Проходимося по кожному номіналу монет в наборі
    for coin in coins:
        # Проходимося по можливим сумам, які можна утворити за допомогою монет даного номіналу
        for i in range(coin, amount + 1):
            # Перевіряємо, чи можна скоротити кількість монет для утворення суми i
            if min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                selected_coins[i] = coin

    # Відновлюємо оптимальний розв'язок, використовуючи інформацію про використані монети
    result = {}
    while amount > 0:
        coin = selected_coins[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

def test_list():
    test_list = [113]
    while len(test_list) < 5:
        int = random.randrange(30, 1500)
        test_list.append(int)
    return test_list

test_group = test_list()

def main():
    i = 0
    while i < 5:
        print(f'Жадібний алгоритм для суми {test_group[i]}: {find_coins_greedy(test_group[i])}')
        print(f'Динамічний алгоритм для суми {test_group[i]}: {find_min_coins(test_group[i])}\n')
        i +=1
    
    result_greedy = []
    result_min = []

    for i in range(0, len(test_group)):
        result_greedy.append(timeit.timeit(lambda: find_coins_greedy(test_group[i]), number=1))
        result_min.append(timeit.timeit(lambda: find_min_coins(test_group[i]), number=1))

    print(f'Жадібний алгоритм, час для сум {test_group},\n {result_greedy}')
    print(f'Алгоритм динамічного програмування, час для сум {test_group},\n {result_min}')

if __name__ == '__main__':
    main()