def password_length():
    try:
        with open('password_list.txt', 'r') as password_list:
            password_length = len(str(password_list.readlines(1)[0]))-1
        return password_length
    except():
        generate()


def generate():
    password_floor = int(input('Input floor of the range: '))
    password_top = int(input('Input top of the range: '))

    try:
        with open('password_list.txt', 'w') as password_list:
            for password in range(password_floor, password_top+1):
                password_list.write(str(password) + '\n')
        print(f'Base from {password_floor} to {password_top} generated')
    except():
        print('Base generating failed')


if __name__ == "__main__":
    generate()
