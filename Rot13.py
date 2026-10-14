'''
ROT13 is a simple letter substitution cipher that replaces a letter with the
letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13.

If there are nonletter characters in the string, they should be left as-is in
the output. Only letters from the ASCII alphabet should be shifted, like in
the original Rot13 "implementation".
'''

def rot13(message):
    
    rot_message = ""
    
    for char in message:
        
        if char.isalpha():
            
            unicode = ord(char)
            char_uni = unicode + 13
            
            if 65 <= unicode <= 90:
                if char_uni > 90:
                    char_uni = char_uni - 90 + 64
                    
            elif 97 <= unicode <= 122:
                if char_uni > 122:
                    char_uni = char_uni - 122 + 96
                    
            char = chr(char_uni)
            
        rot_message += char
        
    return rot_message

print(rot13('Test'))
