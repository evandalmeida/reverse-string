def reverse_string(string):

    reversed_string = ''

    while len(string) > 0:
        last_char = string[-1]

        reversed_string += last_char

        string = string[:-1]

    return reversed_string


print(reverse_string("")) # return (empty string)
print(reverse_string("hello")) # return "olleh"
print(reverse_string("Python")) # return "nohtyP"
print(reverse_string("12345")) # return "54321"