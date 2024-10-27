import json


def create_new_encyrption():
    name = input("Name of the encyrption: ")
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    encyrption = {}
    for char in charset:
        while 1:
            new_val = input("New value for {}: ".format(char))
            if new_val in encyrption.values():
                print("Value already used, please choose another one.")
                continue
            break
        encyrption[char] = new_val
    print("Operation completed.")
    with open(f"{name}.json", "w") as f:
        json.dump(encyrption, f)

def encyrpt_text():
    encyription = input("Give json file name: ")
    with open(f"{encyription}", "r") as f:
        encyrption = json.load(f)
    text = input("Text to encyrpt: ")
    encyrpted_text = ""
    for char in text:
        encyrpted_text += encyrption[char]
    print("Encyrpted text: ", encyrpted_text)

def decrypt_text():
    encyription = input("Give json file name: ")
    with open(f"{encyription}", "r") as f:
        encyrption = json.load(f)
    text = input("Text to decrypt: ")
    decrypted_text = ""
    for char in text:
        for key, val in encyrption.items():
            if val == char:
                decrypted_text += key
    print("Decrypted text: ", decrypted_text)

def main():
    while 1:
        print("1. Create new encyrption")
        print("2. Encyrpt text")
        print("3. Decrypt text")
        print("4. Exit")
        choice = input("Choice: ")
        if choice == "1":
            create_new_encyrption()
        elif choice == "2":
            encyrpt_text()
        elif choice == "3":
            decrypt_text()
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")

main()

