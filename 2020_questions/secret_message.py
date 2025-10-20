def main():
    secret = input("Enter the secret message: ")
    string = input("Enter the string: ")
    
    secret_word(secret, string)




## two pointer algorithm to check if secret is in string
## I haven't learned or touched something like this since sophomore year
## so I also used alot of Google. tbh I need to do a lot more studying

def secret_word(secret, str):
    clean_secret = ""
    clean_str = ""
    for char in secret:
        if char.isalpha():
            clean_secret += char.lower()
    
    for char in str:
        if char.isalpha():
            clean_str += char.lower()
    
    secret_idx = 0
    string_idx = 0

    ## two pointer algo https://www.youtube.com/watch?v=QzZ7nmouLTI
    
    while secret_idx < len(clean_secret) and string_idx < len(clean_str):
        if clean_secret[secret_idx] == clean_str[string_idx]:
            secret_idx += 1
        string_idx += 1

    if secret_idx == len(clean_secret):

        print("Secret message is contained in string")

    else:
        print("Secret message is NOT contained in string")


main()
