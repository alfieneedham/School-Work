key = "AQACS"
plaintext = "Computer Science"
keyLength = len(key)

def schedule_key():
    s = []
    j = 0
    for i in range(256):
        s.append(i)
    for i in range(256):
        j = (j + s[i] + (ord(key[i % keyLength]))) % 256
        s[i], s[j] = s[j], s[i]
    return s

def generate_OTP(s):
    i = 0
    j = 0
    PSRNum = []

    while True:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        PSRNum.append((s[(s[i] + s[j]) % 256]))

        if not generate_ciphertext(PSRNum):
            break

def generate_ciphertext(num):
    pass