
def ceaser_cipher(string_to_encode, shift):

    alphabet = ""
    string_to_encode = string_to_encode.lower()
    print(string_to_encode)
    string_to_encode = "$".join(string_to_encode.split())
    for i in range(ord("a"), ord("z")+1):
        alphabet += chr(i)

    shift = shift % len(alphabet)
    encoded_string = ""
    for ch in string_to_encode:
        if ch == "$":
            encoded_string += " "
            continue
        encoded_string += alphabet[(alphabet.index(ch) + shift) % len(alphabet)]

    return encoded_string


def ceaser_cipher_decoder(string_to_decode):
    alphabet = ""
    string_to_decode = string_to_decode.lower()
    string_to_decode = "$".join(string_to_decode.split())

    for i in range(ord("a"), ord("z")+1):
        alphabet += chr(i)

    decoded_strings = []
    for i in range(len(alphabet)):
        decoded_strings.insert(i, "")
        for ch in string_to_decode:
            if ch == "$":
                decoded_strings[i] += " "
                continue
            decoded_strings[i] += alphabet[(alphabet.index(ch) + i) % len(alphabet)]

    return decoded_strings



