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


def square_root(root):
    return print(f'\nThe root number is: {sqrt(root)}')


if __name__ == "__main__":
    print('\n***** Start *****')

    def main():

        # Checking which volume calculation the user wants
        print('\nVolume of a cylinder or cone? ( CYL for cylinder, CONE for cone. SQRT for square root. Case sensitive.)')
        which_volume = ask_for('\n: ', 'Wrong input', str).upper()

        if which_volume == 'CYL':
            user_height = ask_for('\nWhat is the height?: ',
                                  'Not an integer or decimal.', float)

            user_radius = ask_for('\nWhat is the radius?: ',
                                  'Not an integer or decimal.', float)
            cyl_volume(user_height, user_radius)

        if which_volume == 'CONE':
            user_height = ask_for('\nWhat is the height?: ',
                                  'Not an integer or decimal.', float)

            user_radius = ask_for('\nWhat is the radius?: ',
                                  'Not an integer or decimal.', float)
            cone_volume(user_height, user_radius)

        if which_volume == 'SQRT':
            print('\nWhat is the root?')
            root_num = ask_for('\n: ', 'Not a number', float)
            square_root(root_num)

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
