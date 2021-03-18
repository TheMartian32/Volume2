from math import pi
from math import sqrt


def ask_for(prompt, error_msg=None, _type=None):
    """ While the desired prompt is not given, it repeats the prompt. """
    while True:
        inp = input(prompt).strip()
        if not inp:
            if error_msg:
                print(error_msg)
            continue

        if _type:
            try:
                inp = _type(inp)
            except ValueError:
                if error_msg:
                    print(error_msg)
                continue

        return inp


def cyl_volume(height=float, radius=float):
    """
    Finds the volume of a RIGHT cylinder

    Args:
        height (float, optional): height of the cylinder. Defaults to float.
        radius (float, optional): radius of the cylinder. Defaults to float.

    Returns:
        float: returns the volume of the cylinder based off of the height and radius
    """
    print('\nThe volume is:')
    volume = pi*radius**2*height
    print(volume)
    return volume


def cone_volume(height, radius):
    print('\nThe volume is:')
    volume = pi*radius**2*height/3
    print(volume)
    return volume


def hypotenuse(a, b):
    return print(f'\nThe hypotenuse of the triangle or C is: {sqrt(a**2+b**2)}')


if __name__ == "__main__":
    print('\n***** Start *****')

    def main():

        # Checking which volume calculation the user wants
        print('\n Input the type of calculation ( CYL for cylinder, CONE for cone. SQRT for square root. HYPOTEN for hypotenuse)')
        which_calc = ask_for('\n: ', 'Wrong input', str).upper()

        if which_calc == 'CYL':
            user_height = ask_for('\nWhat is the height?: ',
                                  'Not an integer or decimal.', float)

            user_radius = ask_for('\nWhat is the radius?: ',
                                  'Not an integer or decimal.', float)
            cyl_volume(user_height, user_radius)

        if which_calc == 'CONE':
            user_height = ask_for('\nWhat is the height?: ',
                                  'Not an integer or decimal.', float)

            user_radius = ask_for('\nWhat is the radius?: ',
                                  'Not an integer or decimal.', float)
            cone_volume(user_height, user_radius)

        if which_calc == 'SQRT':
            print('\nWhat is the root?')
            root_num = ask_for('\n: ', 'Not a number', float)
            print(f'The square root is: {sqrt(root_num)}')

        if which_calc == 'HYPOTEN':
            print('\nWhat is A and B?')
            a = ask_for(': ', 'not a number', float)
            b = ask_for(': ', 'not a number', float)
            hypotenuse(a, b)

    # * Calling main function
    main()

    repeat = ''
    while True:
        #  Asks to repeat the script.
        print(
            '\nTyping Y will loop over the script, typing N will quit it.')
        repeat = ask_for('\n: ', _type=str).lower()

        if repeat[0] == 'y':
            main()
            continue

        if repeat[0] == 'n':
            break

    print('\n***** End *****')
