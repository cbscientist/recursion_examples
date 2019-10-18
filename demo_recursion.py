def show_recursion(my_string, special_character='%', replacement_characters = ['0','1']):
    """
    This is a simple function intended to demonstrate
    a recursive algorithm.
    """

    if special_character in my_string:
        for new_character in replacement_characters:
            show_recursion(my_string.replace(special_character, new_character, 1))

    else:
        print(my_string)


if __name__=="__main__":
    show_recursion('%%whatsupdoc%')
    