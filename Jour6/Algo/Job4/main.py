#Job4

message = input("donne ton message : \n")
shift = 1

def cesar_cipher(message, shift):
    result = ""
    
    for char in message:

        if 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        
        elif 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        
        else:
            result += char
    
    return result

print("Message original :", message)
print("Message chiffré :", cesar_cipher(message, shift))