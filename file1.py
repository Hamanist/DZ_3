questions = ["My name ___  Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

user = input('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать!\n- ').lower()

questions_len = len(questions)
question_count = 0
attempts = 3
balls = 0
if user == 'ready':

    for i in range(len(questions)):
        user = input(f'Вопрос {questions[i]}\nОтвет - ').lower()
        while True:

            if user == answers[i]:
                print('Ответ верный!\n')
                balls += 3
                question_count += 1
                break

            else:
                attempts -= 1
                if attempts > 0:
                    balls -= 1
                    print(f'Осталось попыток: {attempts}, попробуйте еще раз!')
                    user = input(f'Вопрос {questions[i]}\nОтвет - ').lower()
                else:
                    print(f'Увы, но нет. Верный ответ: {answers[i]}\n')
                    break

    procent = question_count * 100 / 3
    print(f'Вот и всё! Вы ответили на {questions_len} вопросов из {question_count} верно, вы набрали {balls} баллов.')
else:
    print('Кажется, вы не хотите играть. Очень жаль.')

