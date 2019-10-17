def demo_recursion(my_string, special_character='%'):
    """
    This is a simple function intended to demostrate
    a recursive algorithm.
    """

    if special_character in my_string:
        show_recursion(my_string.replace(special_character, '1', 1))
        show_recursion(my_string.replace(special_character, '0', 1))

    else:
        print(my_string)


if __name__=="__main__":
    show_recursion('%%whats%%updoc%')
    