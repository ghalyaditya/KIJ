from operator import xor

from pip._vendor.distlib.compat import raw_input

text = raw_input("Fill The Text: ")
result = [None] * 4
arr_text = [None] * len(text)

def encrypt(plaintext,password):
    asciikey = [None] * len(password)
    for i in range(0,len(password)):
        asciikey[i] = ord(password[i])

    key0 = [None] * 4
    key1 = [None] * 4
    j = 0
    for i in range(0,len(asciikey)):
        if i <= 3:
            key0[i] = asciikey[i]
        else:
            key1[j] = asciikey[i]
            j = j + 1

    recur = len(plaintext)/4
    empty = 4 - (len(plaintext)%4)
    if empty > 0:
        recur = recur + 1

    asciitext = [None] * (recur*4)
    for i in range(0,len(asciitext)):
        if i < len(plaintext):
            asciitext[i] = ord(plaintext[i])
        else:
            asciitext[i] = ord(' ');

    diisi = (recur*4)

    x = 0
    for i in range(0,recur):
        for j in range(0,4):
            asciitext[x] = xor(asciitext[x], key0[j])
            x = x + 1

    #print asciitext
    #print key1
    x = 0
    ResultEncrypt = [None] * len(asciitext)
    for i in range(0,recur):
        for j in range(0,4):
            ResultEncrypt[x] = asciitext[x] + key1[j]
            x = x + 1

    ResultEncrypted = [None] * (len(ResultEncrypt) - empty)
    for i in range(0,len(ResultEncrypted)):
        ResultEncrypted[i] = chr(ResultEncrypt[i])

    return ResultEncrypted


def decrypt(ResultEncryption, password):
    asciikey = [None] * len(password)
    for i in range(0, len(password)):
        asciikey[i] = ord(password[i])

    key0 = [None] * 4
    key1 = [None] * 4

    j = 0
    for i in range(0, len(asciikey)):
        if i <= 3:
            key0[i] = asciikey[i]
        else:
            key1[j] = asciikey[i]
            j = j + 1

    recur = len(ResultEncryption) / 4
    left = len(ResultEncryption) % 4
    SizeEncrypt = ((4*recur) + left)
    asciiEncrypt = [None] * SizeEncrypt
    for i in range(0, len(asciiEncrypt)):
        asciiEncrypt[i] = ord(ResultEncryption[i])

    for i in range(0,SizeEncrypt):
        asciiEncrypt[i] = asciiEncrypt[i] - key1[i%4]

    ResultDecrypt = [None] * len(asciiEncrypt)
    for i in range(0,SizeEncrypt):
        ResultDecrypt[i] = xor(asciiEncrypt[i],key0[i%4])

    ResultDecrypted = [None] * len(ResultDecrypt)
    for i in range(0,len(ResultDecrypted)):
        ResultDecrypted[i] = chr(ResultDecrypt[i])

    return ResultDecrypted

key = 'ichimaru'

for i in range(0,len(text)):
    arr_text[i] = text[i]

encrypted = encrypt(arr_text,key)
print("Encryption result from " + text + ":" + str(encrypted))

decrypted = decrypt(encrypted,key)
print("Decryption result from" + str(encrypted) + ":" + str(decrypted))
