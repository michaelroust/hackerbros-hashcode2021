

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


def compute_res(team2,team3,team4,pizzas):
    counter = 0
    nb_teams = [team2,team3,team4]
    team_members = 1
    index  = 0
    result = []
    tot_teams = 0
    while counter < pizzas and index < len(nb_teams):
        team_members +=1
        quantity_of_team_nb = nb_teams[index]
        while quantity_of_team_nb > 0 and  pizzas - counter >= team_members:
            tmp_res = []
            tmp_res.append(team_members)
            tot_teams +=1
            for i in range(team_members):
                tmp_res.append(counter)
                counter+=1
            result.append(tmp_res)
            quantity_of_team_nb -=1
        index +=1

    result.insert(0, [tot_teams])  
    return result  




def calculate_score(result,pizza_list):
    tot_teams = result[0]
    array = result[1:]
    score = 0
    for i in range(len(array)):
        ingredients_set = set()
        nb_pizzas = array[i][0]
        tmp_res = array[i][1:]
        for pizza_nb in tmp_res:
            pizza = pizza_list[pizza_nb]
            for ingredient in pizza:
                ingredients_set.add(ingredient)
        score += len(ingredients_set)**2
    return score
    


def main(input_file,output_file):
    array = file_to_array(input_file)
    pizzas,team2,team3,team4 = tuple(array[0])
    pizzas = int(pizzas)
    team2 = int(team2)
    team3 = int(team3)
    team4 = int(team4)
    array = array[1:]
    number_ing = []
    list_ing = []
    for subarray in array:
        number_ing.append(subarray[0])
        list_ing.append(subarray[1:])
    result = compute_res(team2,team3,team4,pizzas)
    print(calculate_score(result,list_ing))
    array_to_file(result, output_file)




for (input_file, output_file) in zip(INPUT_FILES, OUTPUT_FILES):
    main(input_file, output_file)
