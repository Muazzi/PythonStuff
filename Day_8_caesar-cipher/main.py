
def caesar(direction,text,shifts ):
    new_word = []
    x = direction.casefold()
    match x:
        case "encode":
            for c in text:
                new_word.append(ord(c) + shifts)
            res = [chr(c) for c in new_word]
            encoded_text = ''.join(res)
            print(f"The encoded text is {encoded_text}")
        case "decode":
            for c in text:
                new_word.append(ord(c) - shifts)
            res = [chr(c) for c in new_word]
            encoded_text = ''.join(res)
            print(f"The decoded text is {encoded_text}")


while True:

print( art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))










caesar(direction,text,shift)












