#!/usr/bin/env python

# FILE:2252_KKennedy_Lesson5#_InLab.py  
# NAME: CaesarCipherEncoderDecoder.py
# AUTHOR(s): Kevin Kennedy
# DATE: 07/16/2021
# PURPOSE: Encodes or decodes using the Caesar Cipher methodology.

lineBreak = "#"*60
print(lineBreak, "\n\n")

encoding_alphabet = []
def create_encoding_alphabet_list():
    """This function takes all letters of the alphabet and adds them to an empty
    list. It is specifically used for encoding a phrase.
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    for letter in letters:
        encoding_alphabet.append(letter)
    return encoding_alphabet

decoding_alphabet = []
def create_decoding_alphabet_list():
    """This function takes all letters of the alphabet and adds them to an empty
    list. It is specifically used for decoding a phrase.
    """
    # Had to reverse the order of the alphabet to solve an issue that I discuss
    # below in the list_of_numbers_decoding function.
    letters = "zyxwvutsrqponmlkjihgfedcba"
    for letter in letters:
        decoding_alphabet.append(letter)

list_of_numbers_encoding = []
def create_list_of_numbers_for_encoding():
    """This function will create a list of numbers from 1 to 26 to represent the
    number of letters in the alphabet. It is used specifically when encoding.
    """
    for number_of_letter in range(1, 27):
        list_of_numbers_encoding.append(str(number_of_letter))
    return list_of_numbers_encoding

list_of_numbers_decoding = []
def create_list_of_numbers_for_decoding():
    """This function will create a list of numbers from 26 to 1 to represent the
    number of letters in the alphabet. It is used specifically when decoding.
    """
    # Had an issue with the program seeing single digits in the higher letters
    # of the alphabet, i.e., instead of 12 (L), the program would see 1 (A) and
    # 2 (B). Reversing the numbers solved this issue.
    for number_of_letter in range(26, 0, -1):
        list_of_numbers_decoding.append(str(number_of_letter))
    return list_of_numbers_decoding

def introduction_statement():
    """This function prints introductory statements. It contains examples of
    encoding and decoding along with two rules for inputing a phrase.
    """
    print("Hello! This is a Ceaser Cipher encoding and decoding program!")
    print("This program does not accept capital letters or punctuation!")
    print("Encoding example: hello becomes 8-5-12-12-15.")
    print("Decoding example: 8-5-12-12-15 becomes hello.\n")
    
def encode_decode_validation():
    """The purpose of this function is to validate the user's input while 
    choosing if they would like to encode or decode. The program will only accept
    the words 'encode', 'Encode', 'decode', or 'Decode'.
    """
    user_input_is_valid = False
    while user_input_is_valid == False:
        encode_or_decode_choice = input("Please type 'encode' or 'decode': ").lower()
        if encode_or_decode_choice == "encode" or encode_or_decode_choice == "decode":
            user_input_is_valid = True
            return encode_or_decode_choice
        else:
            print(f"The input you entered, '{encode_or_decode_choice}', is not valid. Try again.")

def user_translate_again_validation():
    """This function is serves to validate user input when they're asked if they want 
    to translate another phrase. The accepted responses are 'Y', 'y', 'N', 'n'.
    """
    user_wants_continue = False
    while user_wants_continue == False:
        user_continue_response = input("\nDo you want to encode or decode again, Y/N? ").lower()
        if user_continue_response == "y" or user_continue_response == "n":
            user_wants_continue = True
            return user_continue_response
        else:
            print(f"The input you entered, '{user_continue_response}', is not valid. Try again.\n")

def decode_phrase():
    """This function decodes a user provided phrase. 
    """
    # Get phrase to be decoded. Replace spaces in phrase with periods, replace
    # hyphens with spaces. Replace all numbers with their corresponding letters.
    # Lastly, remove the previously placed spaces, and replace the periods with 
    # spaces. This is done to maintain the spacing of words.
    string_to_decode = input("Please input the string to be decoded: ")
    string_to_decode = string_to_decode.replace(" ", ".").replace("-", " ")
    decoded_string = string_to_decode.replace(list_of_numbers_decoding[0], decoding_alphabet[0])
    for index in range(1, len(list_of_numbers_decoding)):
        decoded_string = decoded_string.replace(list_of_numbers_decoding[index], decoding_alphabet[index])
    decoded_string = decoded_string.replace(" ", "").replace(".", " ")
    return decoded_string
    
def encode_phrase():
    """This function encodes a user provided phrase. 
    """
    string_to_encode = input("Please input the string to be encoded: ")
    string_with_hyphens = ""
    # Go through each character in the phrase to be encoded, remove all letters and
    # add a hyphen to the end of them. Take the all new letters/hyphens and place in
    # an empty string.
    for character in string_to_encode:
        if character in encoding_alphabet:
            string_with_hyphens += f"{character}-"
        else:
            string_with_hyphens += character

    # Go through the new phrase and replace each letter with the corresponding number.
    encoded_string = string_with_hyphens.replace(encoding_alphabet[0], list_of_numbers_encoding[0])
    for index in range(1, len(encoding_alphabet)):
        encoded_string = encoded_string.replace(encoding_alphabet[index], list_of_numbers_encoding[index])
    
    # create empty string variable. Split the converted phrase by spaces, remove the final
    # hyphen in each word and add to the previously created empty variable.
    final_string = ""
    for word in encoded_string.split():
        if word.endswith("-"):
            word = word[0:-1] + " "
            final_string +=  word
    return final_string
    
def main():
    introduction_statement()

    # Start outter while loop that allows the user to translate phrases as 
    # long as they would like to.
    user_wants_translation = True
    while user_wants_translation == True:
        
        # Ask user if they would like to do encoding or decoding, validate that
        # input. Then execute the appropriate functions based on that choice.
        encode_or_decode_choice = encode_decode_validation()
        if encode_or_decode_choice == "encode":
            encoding_alphabet = create_encoding_alphabet_list()
            list_of_numbers_encoding = create_list_of_numbers_for_encoding()
            encoded_string = encode_phrase()
            print(encoded_string)
        elif encode_or_decode_choice == "decode":
            decoding_alphabet = create_decoding_alphabet_list()
            list_of_numbers_decoding = create_list_of_numbers_for_decoding()
            decoded_string = decode_phrase()    
            print(decoded_string)
        
        # prompt user to see if they'd like to continue, if not exit out of 
        # the outer while loop, thus ending the program.
        user_continue_response = user_translate_again_validation()
        if user_continue_response == "n":
            user_wants_translation = False
            print("Thank you for using this program!")

# Makes sure program is not run when being imported into another module.
if __name__ == "__main__":
    main()

print("\n\n", lineBreak)

#Keep shell window/script open:
print(input('\n\nHit Enter to Close\n'))