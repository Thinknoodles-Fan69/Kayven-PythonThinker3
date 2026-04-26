
def caesar_shift_character(char, key, mode):
    if mode == "encrypt":
        shifted_no = ((ord(char)- 32 ) + key)% 95 + 32
        shifted_letter = chr(shifted_no)
        return shifted_letter
    elif mode == "decrypt":
        shifted_no = ((ord(char) - 32) - key)% 95 + 32
        shifted_letter = chr(shifted_no)
        return shifted_letter



# mode = input("What mode do you want to use(encrypt/decrypt): ")
# key = int(input("What is the shift key used: "))
# char = input("Give me a character: ")
# print(caesar_shift_character(char, key, mode))



def caesar_shift_sentence(sentence, key, mode):
    if mode == "encrypt":
        encrypted_sentence = ""
        for char in sentence:
            if char == " ":
                encrypted_sentence += " "
            else:
                shifted_no = ((ord(char)- 32 ) + key)% 95 + 32
                shifted_letter = chr(shifted_no)
                encrypted_sentence += shifted_letter
        return encrypted_sentence
    elif mode == "decrypt":
        decrypted_sentence = ""
        for char in sentence:
            if char == " ":
                decrypted_sentence += " "
            else:
                shifted_no = ((ord(char) - 32) - key)% 95 + 32
                shifted_letter = chr(shifted_no)
                decrypted_sentence += shifted_letter
        return decrypted_sentence



# mode = input("What mode do you want to use(encrypt/decrypt): ")
# key = int(input("What is the shift key used: "))
# sentence = input("Give me a sentence: ")
# print(caesar_shift_sentence(sentence, key, mode))




# def caesar_shift_list(sentences, key, mode):
#     if mode == "encrypt":
#         encrypted_list = []
#         for item in sentences:
#             encrypted_sentence = ""
#             for char in item:
#                 if char == " ":
#                     encrypted_sentence += " "
#                 else:
#                     shifted_no = ((ord(char)- 33 ) + key)% 95 + 33
#                     shifted_letter = chr(shifted_no)
#                     encrypted_sentence += shifted_letter
#             encrypted_list.append(encrypted_sentence)
#         return encrypted_list
#     elif mode == "decrypt":
#         decrypted_list = []
#         for item in sentences:
#             decrypted_sentence = ""
#             for char in item:
#                 if char == " ":
#                     decrypted_sentence += " "
#                 else:
#                     shifted_no = ((ord(char)- 33 ) - key)% 95 + 33
#                     shifted_letter = chr(shifted_no)
#                     decrypted_sentence += shifted_letter
#             decrypted_list.append(decrypted_sentence)
#         return decrypted_list



# mode = input("What mode do you want to use(encrypt/decrypt): ")
# key = int(input("What is the shift key used: "))

# sentences = []
# sentence = input("Add a sentence to the list: ")
# while sentence != "end":
#     sentences.append(sentence)
#     sentence = input("Add a sentence to the list: ")


# print(caesar_shift_list(sentences, key, mode))



def caesar_shift_file(input_filename, output_filename, key, mode):
    with open(input_filename, "r") as infile:

        with open(output_filename, "w") as outfile:
            for line in infile:
                shifted_line = caesar_shift_sentence(line.strip(), key, mode)
                outfile.write(shifted_line + "\n")
    
caesar_shift_file("in.txt", "0_out.txt", 7, "encrypt")

for i in range(-95, 96):
    caesar_shift_file("0_out.txt", f"0_out{i}.txt", "i", "decrypt")