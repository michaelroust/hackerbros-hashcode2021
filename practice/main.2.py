

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

pizza_list_copy = []

pizza_ordered = []

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

def get_pizza_list(array):
    array = array[1:]

    for i in range(0, len(array) - 1):
        pizza = array[i].copy()
        pizza[0] = i
        pizza_list_copy.append(pizza)

def get_pizza_ordered_by_weight(array):
    array = array[1:]

    for i in range(0, len(array) - 1) :
        pizza_ordered.append([i, array[i][0]])

    pizza_ordered.sort(key=lambda tup: tup[1], reverse=True)

def compute_res(team2,team3,team4,pizzas):
    counter = 0
    nb_teams = [team2,team3,team4]
    team_members = 1
    index  = 2
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
                tmp_res.append(pizza_ordered[counter][0])
                counter+=1
            result.append(tmp_res)
            quantity_of_team_nb -=1
        index -=1

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
    
    
def find_biggest_pizza(pizzas):
    biggest_pizza_id = -1
    biggest_pizza_size = -1
    
    pizza_id = 0
    for pizza in pizzas:
        pizza_size = int(pizza[0])
        
        if (biggest_pizza_size < pizza_size):
            biggest_pizza_id = pizza_id
            biggest_pizza_size = pizza_size
        
        pizza_id += 1
            
    return (biggest_pizza_id, biggest_pizza_size)
    
    
def pizza_set_size(pizza_list):
    print(pizza_list)
    
    c = 0
    while c < len(pizza_list):
        pizza_list[c] = pizza_list[c][1:]
        c += 1
    
    ingredients = set()
    for pizza in pizza_list:
        for ingr in pizza:
            ingredients.add(ingr)
            
    print(ingredients)
            
    return len(ingredients)

    
def algo(array):
    nb_pizzas,team2,team3,team4 = tuple(array[0])
    nb_pizzas = int(nb_pizzas)
    teams2 = int(team2)
    teams3 = int(team3)
    teams4 = int(team4)
    pizzas = array[1:]
    
    pizzas_with_id = []
    
    for i in range(0, len(pizzas) - 1):
        pizza_with_id = pizzas[i].copy()
        pizza_with_id[0] = i
        pizzas_with_id.append(pizza_with_id)
    
    
    (biggest_pizza_id, biggest_pizza_size) = find_biggest_pizza(pizzas)
    
    biggest_pizza = pizzas_with_id[biggest_pizza_id]
    pizza_list = [biggest_pizza]
    
    pizzas_with_id.remove(biggest_pizza)
    
    # print(pizza_list)

    biggest_pizza_list_size = -1
    biggest_pizza_list = []

    team_size = 4
    for i in range(2, team_size):
        
        for j in range(0, len(pizzas_with_id) - 1):
            pizza_list_cpy = pizza_list.copy()
            pizza_list_cpy.append(pizzas_with_id[j])
            
            pizza_list_size = pizza_set_size(pizza_list_cpy)
            if biggest_pizza_list_size < pizza_list_size:
                biggest_pizza_list_size = pizza_list_size
                biggest_pizza_list = pizza_list_cpy

    
    print(pizza_set_size(biggest_pizza_list))
    
    # print(find_biggest_pizza(pizzas))
    # print(pizza_set_size([pizzas[2], pizzas[3]]))
    
    # for pizza in array:
    # 
    
    


def main2(input_file, output_file):
    array = file_to_array(input_file)
    get_pizza_list(array)


    # array_to_file(result, output_file)


def main(input_file,output_file):
    array = file_to_array(input_file)
    get_pizza_ordered_by_weight(array)
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
