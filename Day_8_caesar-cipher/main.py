import  art
in_caesar = False
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


print(art.logo)
while not in_caesar:


    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt , or type exit to quit\n")
    print(direction)
    if direction.casefold() == 'exit':
        in_caesar = True
        break

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction,text,shift)
    in_caesar_prompt = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if in_caesar_prompt =='no':
        in_caesar = True












