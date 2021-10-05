import string

# Generate list of number:
# import random
# x = [i for i in range(a, b, c)]
# random.shuffle(x)

n = [28, 94, 50, 15, 32, 66, 44, 29, 1, 55, 62, 39, 92, 98, 87, 74, 22, 23, 36, 45, 16, 86, 100, 46, 10, 11, 2, 9, 78, 95, 89, 76, 99, 68, 33, 91, 35, 25, 19, 27, 93, 69, 38, 64, 75, 85, 3, 42, 72, 60, 71, 31, 14, 96, 26, 54, 13, 6, 83, 34, 58, 20, 30, 51, 84, 65, 52, 70, 53, 5, 8, 61, 7, 4, 90, 77, 59, 17, 43, 24, 56, 82, 88, 79, 21, 73, 81, 48, 49, 57, 97, 40, 18, 37, 12, 41, 67, 80, 63, 47]
alphabet = string.printable
encryption_list = []
encrypt_msg = []
decryption_list = []
decrypt_msg = []

start = input('type "enc" for encryption or "dec" for decryption: ')

if start == 'enc':
    x = input('type your message: ')
    # encryption
    for i in x:
        encryption_list.append(n.index(alphabet.index(i)))
    print(encryption_list)
elif start == 'dec':
    y = input('input code one by one and type "ok" when you are done\n')
    # decryption
    while y != 'ok':
        encrypt_msg.append(y)
        y = input()
    for u in encrypt_msg:
        decryption_list.append(n[int(u)])
    for o in decryption_list:
        decrypt_msg.append(alphabet[o])
    print(decrypt_msg)
else:
    print('Error :(')
