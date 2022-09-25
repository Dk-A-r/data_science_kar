"""
    Игра "Угадай число": программа сама
    загадывает и угадывает
    """

import numpy as np

def random_predict (number = np.random.randint(1, 101)) -> int:
    """
    Рандомно угадывает число

    Args:
    number(optional): Случайное число

    Returns:
    int: число попыток
"""

    count = 0

    list_numbers = list(range(1, 101))

    while True:
        count += 1
        predict_number = int(np.mean(list_numbers))

        half = round(int(len(list_numbers))/2)

        if number == predict_number:
            break
        elif predict_number<number:
            list_numbers = list_numbers[half:]
        else:
            list_numbers = list_numbers[:half]
        if len(list_numbers) == 0:
            break
    print(f'Найденный номер равен {number}, для отгадывания' + 
          f' потребовалось {count} попыток')
    return(count)

random_predict()



    
