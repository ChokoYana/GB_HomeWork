
def import_directory():
    with open('directory.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            print(line)


def export_directory(new_line):
    with open('directory.txt', 'a', encoding='UTF-8') as file:
        file.writelines(' '.join(new_line) + '\n')

def find_info():
    name = input('search: ')
    with open('directory.txt', 'r', encoding='UTF-8') as file:
        find_list_info = list()
        for line in file:
            if name in line:
                find_list_info.append(line)
        print(*find_list_info)


def print_menu():
    print('Select an action:')
    print('1 - print derectory\n'
          '2 - add info\n'
          '3 - find info\n'
          '4 - delite str\n'
          '5 - change info')


def choise_user():
    user_num = int(input('Select an action: '))
    if user_num == 1:
        import_directory()
    elif user_num == 2:
        export_directory(print_export_name())
    elif user_num == 3:
        find_info()
    elif user_num == 4:
        delite_info()
    elif user_num == 5:
        change_info()
    else:
        choise_user()

def print_export_name():
    last_name = input('Last name: ').strip()
    first_name = input('First name: ').strip()
    phone_number = input('Number: ').strip()
    return (last_name, first_name, phone_number)

def delite_info():
    # name = input('what to replace?: ')
    # replace_info = input('what information to replace?: ')
    with open('directory.txt', 'r', encoding='UTF-8') as file:
        direct_lines = file.readlines()
        el = input('what to delite?: ')
        with open('directory.txt', 'w', encoding='utf-8') as pb:
            for line in direct_lines:
                if el not in line:
                    pb.write(line)
        print('Delited')

def change_info():
    with open('directory.txt', 'r', encoding='UTF-8') as file:
        direct_lines = file.readlines()
        el = input('what to replace?: ')
        replace_info = input('what information to replace?: ')

        with open('directory.txt', 'w', encoding='utf-8') as pb:
            for line in direct_lines:
                if el in line:
                    line = line.split()
                    for i in line:
                        new_line = i.replace(el, replace_info)
                        pb.writelines(new_line + ' ')

                else:
                    pb.writelines(str(line))




print_menu()
choise_user()


# def remove_string3(filename, string):
#
#     rst = []
#
#     with open(filename) as fd:
#         t = fd.read()
#         for line in t.splitlines():
#             if line != string:
#                 rst.append(line)
#
#     with open(filename, 'w') as fd:
#         fd.write('\n'.join(rst))
#         fd.write('\n') # with join we lose the last newline char