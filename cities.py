first_city = 'Минск'
end = first_city[-1]
print(f'Первый город: {first_city}')
forbidden = ['ы', 'ь', 'ъ']

while True:
    answer = input(f'Введите город начинающийся с \'{end}\' ').casefold()

    if answer == 'сдаюсь':
        break

    for i in forbidden:
        answer = answer.replace(i, '')
    if answer[0] == end:
        end = answer[-1]
        continue
    else:
        print('Попробуйте ввести еще раз или введите \'сдаюсь\'\n')

print('End')
