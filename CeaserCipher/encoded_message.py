import string
# importing english alphabets in the lower case
lower = string.ascii_lowercase

# importing english alphabets in the upper case
upper = string.ascii_uppercase
str = input("Enter the string to be encoded. ")

#the shift that is given to the encoded message
shift = int(input("Enter the shift "))

def encrypted_msg(msg, shift):

    if shift > 0:
        rev_lower = lower[shift::] + lower[0:shift]
        rev_upper = upper[shift::] + upper[0:shift]

    if shift < 0:
        rev_lower = lower[shift::] + lower[:len(lower)-1]
        rev_upper = upper[shift::] + upper[:len(upper) - 1]

    if shift == 0:
        rev_lower = lower
        rev_upper = upper


    # the variable that will store the encoded message
    ceaser = ""

    # reversing the lower and upper for better implementation of the code

    for char in range(len(str)):
        for char_ in range(len(lower)):
            if str[char] == lower[char_]:
                ceaser += rev_lower[char_]
            if str[char] == upper[char_]:
                ceaser += rev_upper[char_]
            if str[char] == " ":
                ceaser += " "
                break
            if str[char] not in lower and str[char] not in upper:
                ceaser += str[char]
                break

    return ceaser

print(encrypted_msg(str, shift))