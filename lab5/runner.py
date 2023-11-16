from functions import RectangleArt

def get_length_input(shape_name):
    while True:
        length = input(f"Enter the {shape_name} length (must be a number greater than or equal to 4): ")
        try:
            length = int(length)
            if length < 4:
                print("Error: Length must be greater than or equal to 4.")
            else:
                return length
        except ValueError:
            print("Error: Please enter a valid number.")

def get_color_input():
    while True:
        color_option = input("Do you want to use one or three colors for the shape? (1-only one or 3- three different): ")
        if color_option not in ["1", "3"]:
            print("Error: Incorrect selection. Please choose the correct option.")
        else:
            break
    if color_option == "1":
        color_choice = input(f"Choose a color for the shape from the list {list(RectangleArt.VALID_COLORS)}: ")
        if color_choice not in RectangleArt.VALID_COLORS:
            print("Error: Incorrect color selection. Please choose the correct option.")
        return [color_choice]
    elif color_option == "3":
        return ['BLUE', 'MAGENTA', 'RED']

def get_alignment_input():
    while True:
        alignment = input("Select alignment (left, center, right): ")
        if alignment not in ["left", "center", "right"]:
            print("Error: Incorrect alignment. Please choose the correct option.")
        else:
            return alignment

def get_manipulation_input(rectangle_art):
    while True:
        manipulate_choice = input("Do you want to change your figure? (yes or no): ").lower()
        if manipulate_choice == "yes":
            manipulation_type = input("Enter the type of change: 1-scale, 2-reverse_scale_figure: ")
            if manipulation_type in ["1", "2"]:
                scale_factor = float(input("Enter the scale factor: "))
                if manipulation_type == "1":
                    rectangle_art.scale_figure(scale_factor)
                elif manipulation_type == "2":
                    rectangle_art.reverse_scale_figure(scale_factor)
                rectangle_art.draw_combined_rectangles()
            else:
                print("Error: Invalid change type.")
        else:
            break

def main():
    console_length = 400

    while True:
        print("Menu:")
        print("1. Draw a cube")
        print("2. Draw a parallelepiped")
        print("3. Exit")

        choice = input("Please select an option: ")

        if choice == "3":
            break
        if choice not in ["1", "2"]:
            print("Error: Incorrect selection. Please choose the correct option.")
            continue

        length = get_length_input("shape")

        if choice == "2":
            width = get_length_input("parallelepiped width")

        colors = get_color_input()

        if choice == "1":
            rectangle_art = RectangleArt(length, length, *colors)
        elif choice == "2":
            rectangle_art = RectangleArt(length, width, *colors)

        alignment = get_alignment_input()
        print(f"{alignment.capitalize()} alignment:")
        rectangle_art.align_art(alignment, console_length)

        get_manipulation_input(rectangle_art)

        convert_2D = input("Want to turn 3D art into 2D? (yes or no): ").lower()
        if convert_2D == "yes":
            rectangle_art.convert_to_2d()

        save_choice = input("Do you want to save the generated ASCII art to a file? (yes or no): ").lower()
        if save_choice == "yes":
            file_name = input("Enter a file name to save the ASCII art: ")
            rectangle_art.save_to_file(file_name)

        continue_choice = input("Do you want to continue drawing? (yes or no): ").lower()
        if continue_choice != "yes":
            break

if __name__ == '__main__':
    main()
