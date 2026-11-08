import random

# Список слов для игры
word_list = [
    'питон', 'разработчик', 'компьютер', 'алгоритм', 'программа',
    'сервер', 'база', 'синтаксис', 'функция', 'интерфейс'
]

def get_word():
    return random.choice(word_list).upper()

def display_hangman(tries):
    stages = [
        # 0 попыток (финал: голова, туловище, обе руки, обе ноги)
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # 1 попытка (осталась одна нога)
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # 2 попытки (туловище и обе руки)
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # 3 попытки (туловище и одна рука)
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # 4 попытки (только голова и туловище)
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # 5 попыток (только голова)
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # 6 попыток (начало: пустая виселица)
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)

    while not guessed and tries > 0:
        guess = input('Введите букву или слово целиком: ').strip().upper()

        # Защита от дурака: проверка, что введены только буквы
        if not guess.isalpha():
            print('Ошибка: ввод должен содержать только буквы!')
            continue

        # Обработка ввода одной буквы
        if len(guess) == 1:
            if guess in guessed_letters:
                print(f'Вы уже называли букву {guess}!')
            elif guess not in word:
                print(f'Буквы {guess} нет в слове.')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f'Отлично, буква {guess} есть в слове!')
                guessed_letters.append(guess)
                
                # Заменяем символы '_' на угаданную букву
                word_as_list = list(word_completion)
                for index, letter in enumerate(word):
                    if letter == guess:
                        word_as_list[index] = guess
                word_completion = ''.join(word_as_list)

                if '_' not in word_completion:
                    guessed = True

        # Обработка ввода слова целиком
        elif len(guess) == len(word):
            if guess in guessed_words:
                print(f'Вы уже называли слово {guess}!')
            elif guess != word:
                print(f'Слово {guess} неверное.')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print(f'Длина введенного слова не совпадает с загаданным ({len(word)} букв)!')
            continue

        print(display_hangman(tries))
        print(word_completion)

    if guessed:
        print('Поздравляем, вы угадали слово! Вы победили!')
    else:
        print(f'К сожалению, попытки закончились. Загаданное слово было: {word}')

# Основной цикл запуска игры
while True:
    secret_word = get_word()
    play(secret_word)
    again = input('Сыграем еще раз? (д/н): ').strip().lower()
    if again not in ('д', 'да', 'y', 'yes'):
        print('Спасибо за игру!')
        break