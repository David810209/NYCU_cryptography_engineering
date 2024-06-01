from pylfsr import LFSR
import numpy as np

def generate_keystream(L, length):
    keystream = []
    for _ in range(length):
        keystream.append(L.state[-1])
        L.next()
    return keystream

def encrypt_decrypt_with_keystream(input_text, keystream):
    output_text = ''
    keystream_index = 0
    for char in input_text:
        encrypted_chars = []
        for bit in format(ord(char), '08b'):
            keystream_bit = keystream[keystream_index]
            keystream_index += 1
            encrypted_bit = str(int(bit) ^ keystream_bit)
            encrypted_chars.append(encrypted_bit)
        encrypted_char = chr(int(''.join(encrypted_chars), 2))
        output_text += encrypted_char
    return output_text



state = [1,0,0,0,0,0,0,0]  
taps = [8,4,3,2]  # x^8 + x^4 + x^3 + x^2 + 1
L = LFSR(initstate=state, fpoly=taps)
plaintext = "ATNYCUWEARESTRIVINGTOBEAGREATUNIVERSITYTHATTRANSCENDSDISCIPLINARYDIVIDESTOSOLVETHEINCREASINGLYCOMPLEXPROBLEMSTHATTHEWORLDFACESWEWILLCONTINUETOBEGUIDEDBYTHEIDEATHATWECANACHIEVESOMETHINGMUCHGREATERTOGETHERTHANWECANINDIVIDUALLYAFTERALLTHATWASTHEIDEATHATLEDTOTHECREATIONOFOURUNIVERSITYINTHEFIRSTPLACE"

keystream = generate_keystream(L, len(plaintext) * 8)
ciphertext = encrypt_decrypt_with_keystream(plaintext, keystream)
print("Ciphertext:", ciphertext)

decrypted_text = encrypt_decrypt_with_keystream(ciphertext, keystream)
print("Decrypted text:", decrypted_text)

print("keystream:",''.join(str(i) for i in keystream))


