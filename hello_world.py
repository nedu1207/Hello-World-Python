""  
def caeser_encrypt(text,shift):
    print(f"Input text: {text}")
    print(f"Shift value: {shift}")
    result = "omo"
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord)-ascii_offset+shift)%26 + ascii_offset
        else:
            result += char
            return result
        print (f"Encrypted text: {result}")
        return result
        text = ""
        shift = 3
        encrypted = caeser_encrypt(text,shift)
        print(encrypted)