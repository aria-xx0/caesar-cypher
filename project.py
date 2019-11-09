def decrypt(cypher, letters, amount):
    decrypted_cypher = ""
    for letter in cypher:
        num = letters.index(letter) + 1
        num -= amount
        num = num % 27
        sub_letter = letters[num - 1]
        decrypted_cypher += sub_letter
    return decrypted_cypher

def encrypt(cypher, letters, amount):
    num_cypher = ""
    for letter in cypher:
        letter = letter.lower()
        num = letters.index(letter) + 1
        num += amount
        num = num % 27
        add_letter = letters[num - 1]
        num_cypher += add_letter
    return num_cypher

if __name__ == "__main__":

    cypher = input("What string do you want to encrypt? ")
    eord = input("Encrypt or decrypt? (e/d) ")
    amount = int(input("Encrypt by how many letters? "))

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    if eord == "e":
        print(encrypt(cypher, letters, amount))
    elif eord == "d":
        for amount in range(0, 27):
            print(decrypt(cypher, letters, amount + 1))
    else:
        print("Enter a damn e or d, not whatever the hell that was!")