def show_recursion(my_string, special_character="%", replacement_characters=["0", "1"]):
    """
    This is a simple function intended to demonstrate
    a recursive algorithm.
    """

    if special_character in my_string:
        for new_character in replacement_characters:
            show_recursion(my_string.replace(special_character, new_character, 1))

    else:
        print(my_string)


def alt_solution(my_string, special_character="%"):
    """
    This is a simple function showing an alternative solution 
    to the problem statement.
    """

    if special_character in my_string:
        count = my_string.count(special_character)
        num_combos = 2 ** count
        for combo in range(num_combos):
            # Doesn't get you right zeroes, would have to fill
            binary_version = bin(combo)
            binary_string = str(binary_version).replace("0b", "")
            for digit in binary_string:
                new_string = my_string.copy()  # deep copy
                new_string.replace(
                    digit
                )  # should replace 1 character, starting from left
            print(new_string)
    else:
        print(my_string)


if __name__ == "__main__":
    show_recursion("%%whatsupdoc%")
    alt_solution("%%whatsupdoc%")
