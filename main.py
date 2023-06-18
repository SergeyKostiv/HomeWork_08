# Создать телефонный справочник возможностью добавления записей и чтения. 
# Пользователь также может ввести фамилию, 
# тогда программа должны вывести на экран все записи с этой фамилий. 
# Также пользователь может добавлять новых людей в справочник в режиме экспорт.
    

def imput():
    # добавляет строку в справочник
    with open('phone.txt', 'a', encoding='utf-8') as file:
        file.write(input('Введите новую строку: '+'\n'))
    

def export():
    # ищет информацию в справочнике
    with open('phone.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('Введите для поиска?: ')
        for i in book:
            if temp in i:
                print(i)

while True:
    mode = input('Выберите режим работы справочника' + '\n'
                  +'1-поиск, 2-добавление в файл, 3-выход: ')
    # if mode == '1':
    #     print(show_dir)
    if mode == '1':
        export()
    elif mode == '2':
        imput()
    elif mode == '3':
        break
    else:
        print('No mode')