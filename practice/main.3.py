

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


# def pizza_set_size(pizza_list):
#     # pizza_list = pizza_list.copy()
#     # while c < len(pizza_list):
#     #     pizza_list[c] = pizza_list[c][1:]
#     #     c += 1

#     ingredients = set()
#     for pizza in pizza_list:
#         for ingr in pizza[1:]:
#             ingredients.add(ingr)

#     return len(ingredients)


def pizza_set_size_opt(pizza, ingredients=set()):
    new_ingredients = ingredients.copy()
    new_ingredients.update(pizza[1:])
    return len(new_ingredients), new_ingredients


def add_best_next_pizza_to_list(pizzas_with_id, pizza_list):
    
    
    fails_to_find_better_next_pizza = 0
    

    biggest_pizza_list_size = -1
    biggest_pizza_list = []
    
    best_ingredients = set()

    best_next_pizza = -1

    for pizza in pizzas_with_id:
        
        if fails_to_find_better_next_pizza > 10000:
            break
        
        # pizza_list_cpy = pizza_list.copy()
        # pizza_list_cpy.append(pizza)
        # pizza_list_size = pizza_set_size(pizza_list_cpy)
        
        pizza_list_size, new_ingredients = pizza_set_size_opt(pizza, best_ingredients)

        if biggest_pizza_list_size <= pizza_list_size:
            biggest_pizza_list_size = pizza_list_size
            
            biggest_pizza_list = pizza_list.copy()
            biggest_pizza_list.append(pizza)
            
            best_ingredients = new_ingredients
            
            best_next_pizza = pizza
            
        if best_next_pizza != -1:
            fails_to_find_better_next_pizza += 1

    pizzas_with_id.remove(best_next_pizza)

    return biggest_pizza_list


def get_pizza_list_ids(pizza_list):
    ids = []
    
    for pizza in pizza_list:
        ids.append(pizza[0])
        
    return ids


def encode_ingredients():
    pass
        

def algo(input_file, array):
    nb_pizzas,team2,team3,team4 = tuple(array[0])
    nb_pizzas = int(nb_pizzas)
    teams2 = int(team2)
    teams3 = int(team3)
    teams4 = int(team4)
    pizzas = array[1:]

    pizzas_and_id = pizzas.copy()

    for i in range(0, len(pizzas_and_id)):
        pizzas_and_id[i].insert(0, i)


    pizzas_and_id.sort(key=lambda x: x[1], reverse=True)
    
    for i in range(0, len(pizzas_and_id)):
        del pizzas_and_id[i][1]
    
    pizzas_with_id = pizzas_and_id

    # print(pizzas_with_id)
    # print(pizza_set_size(pizzas_with_id))

    print("============================ " + input_file)
    
    team_infos = ((4, teams4), (3, teams3), (2, teams2))
    
    output = []
    
    total_deliveries = 0
    pizzas_left = nb_pizzas
    
    for (team_size, teams_of_this_size) in team_infos:
        for i in range(0, teams_of_this_size):
            print(pizzas_left, str(pizzas_left / nb_pizzas * 100) + "%")
            
            pizza_list = []
            
            if pizzas_left < team_size:
                continue
            
            for j in range(0, team_size):
                pizza_list = add_best_next_pizza_to_list(pizzas_with_id, pizza_list)
                pizzas_left -= 1
                
            delivery = get_pizza_list_ids(pizza_list)
            delivery.insert(0, len(pizza_list))
            output.append(delivery)
            total_deliveries += 1
    
    output.insert(0, [total_deliveries])
    return output
    
    # pizza_list = []
    # pizza_list = add_best_next_pizza_to_list(pizzas_with_id, pizza_list)
    # pizza_list = add_best_next_pizza_to_list(pizzas_with_id, pizza_list)
    # pizza_list = add_best_next_pizza_to_list(pizzas_with_id, pizza_list)
    # pizza_list = add_best_next_pizza_to_list(pizzas_with_id, pizza_list)
    
    # print(pizza_list)
    # print(pizza_set_size(pizza_list))
    # print(get_pizza_list_ids(pizza_list))



def main2(input_file, output_file):
    array = file_to_array(input_file)

    result = algo(input_file, array)

    array_to_file(result, output_file)



for (input_file, output_file) in zip(INPUT_FILES[3:], OUTPUT_FILES[3:]):
# for (input_file, output_file) in zip(INPUT_FILES[3:], OUTPUT_FILES[3:]):
    main2(input_file, output_file)

# main2(INPUT_FILES[1], OUTPUT_FILES[1])
