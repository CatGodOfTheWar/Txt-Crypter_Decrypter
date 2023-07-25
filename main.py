INDEX = 0


def crypt(data, password):
    global INDEX
    data = list(data)
    for char in data:
        if (INDEX + 1) == len(password):
            INDEX = 0
        add = ord(password[INDEX])
        if (ord(char) + add) < 256:
            result = ord(char) + add
        else:
            result = ((ord(char) + add) % 255)
        with open("Data_entry.txt", "a") as new_data:
            new_data.write(chr(result))


def decrypt(data, password):
    global INDEX
    data = list(data)
    for char in data:
        if (INDEX + 1) == len(password):
            INDEX = 0
        add = ord(password[INDEX])
        result = ord(char) - add
        with open("Data_entry.txt", "a") as new_data:
            new_data.write(chr(result))


def main():
    with open("Data_entry.txt", "r") as file:
        data = file.read()
    password = input("Insert the password: ")
    command = input("Choose the command(crypt/decrypt): ").lower()
    with open("Data_entry.txt", "w") as _:
        pass
    if command == "crypt":
        crypt(data, password)
    else:
        decrypt(data, password)


if __name__ == '__main__':
    main()
