


#=============================================================================


INPUT_FILES = [
    "practice/input/a_example",
    "practice/input/b_little_bit_of_everything.in",
    "practice/input/c_many_ingredients.in",
    "practice/input/d_many_pizzas.in",
    "practice/input/e_many_teams.in"
]


OUTPUT_FILES = [
    "practice/output/a_example.out",
    "practice/output/b_little_bit_of_everything.out",
    "practice/output/c_many_ingredients.out",
    "practice/output/d_many_pizzas.out",
    "practice/output/e_many_teams.out"
]


#=============================================================================


def file_to_array(input_file):
    """Turns the input space-separated-file into a 2D array over line and space"""

    with open(input_file) as csv_file:
        csv_text = csv_file.read()

    array = csv_text.split("\n")
    for i in range(0, len(array)):
        array[i] = array[i].strip().split(" ")

    array = array[:-1]

    return array


def array_to_file(array, output_file):
    """Turns the output 2D array into a space-separated-file"""

    array_str = []

    for line in array:
        line_str = ""
        for word in line:
            line_str += str(word) + " "

        line_str = line_str.strip() + "\n"
        array_str.append(line_str)


    with open(output_file, "w") as output_file:
        output_file.writelines(array_str)


#=============================================================================


def algo(array):
    time = array[0][0]
    
    
    
    return 0


def main(input_file, output_file):
    array = file_to_array(input_file)

    result = algo(input_file)

    # array_to_file(result, output_file)
    
