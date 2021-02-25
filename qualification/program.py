


#=============================================================================


INPUT_FILES = [
    "qualification/input/a.txt",
    "qualification/input/b.txt",
    "qualification/input/c.txt",
    "qualification/input/d.txt",
    "qualification/input/e.txt",
    "qualification/input/f.txt"
]


OUTPUT_FILES = [
    "qualification/output/a.out",
    "qualification/output/b.out",
    "qualification/output/c.out",
    "qualification/output/d.out",
    "qualification/output/e.out",
    "qualification/output/f.out"
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


def parse(array):
    time = int(array[0][0])
    nb_intersections = int(array[0][1])
    nb_streets = int(array[0][2])
    nb_cars = int(array[0][3])
    nb_score_per_car = int(array[0][4])

    streets = array[1:1+nb_streets]

    for i in range(0, len(streets)):
        streets[i] = [int(streets[i][0]), int(streets[i][1]), streets[i][2], int(streets[i][3])]

    paths = array[1+nb_streets:]

    for i in range(0, len(paths)):
        paths[i][0] = int(paths[i][0])


    return time, nb_intersections, nb_streets, nb_cars, nb_score_per_car, streets, paths


#streets: id_start id_end name time
def orderByIntersection(streets,nb_intersections):
    list_of_streets_per_intersection = []
    for i in range(nb_intersections):
        list_of_streets_per_intersection.append([])

    for street in streets :
        list_of_streets_per_intersection[street[1]].append(street)

    #or i in range(nb_intersections):
     #   print(list_of_streets_per_intersection[i])

    return list_of_streets_per_intersection


def compute_schedule_trivial():
    return 1


def streets_to_out_intersection_dict(streets):
    streets_to_inters_dict = {}

    for street in streets:
        street_name = street[2]
        street_out_inter = street[1]

        streets_to_inters_dict[street_name] = street_out_inter

    return streets_to_inters_dict


def group_street_visits(nb_intersections, street_visits_dict, streets_to_inters_dict):
    intersections = [0 for _ in list(range(0, nb_intersections))]

    for (street_name, street_visits) in street_visits_dict.items():
        intersection_id = streets_to_inters_dict[street_name]

        intersections[intersection_id] += street_visits

    return intersections




def compute_street_visits(streets, paths):
    nb_visits_per_street = {}

    for street in streets:
        nb_visits_per_street[street[2]] = 0

    for path in paths:
        for i in range(path[0]):
            nb_visits_per_street[path[i + 1]] += 1

    return nb_visits_per_street
# (cars_passing_street/sum_cars_passing_streets_in_intersection * cycle)



def assign_weights(intersection_id, nb_visits_per_street, intersection_visits, street_name, list_of_streets_per_intersection):

    tot_cars_in_intersection = 1 if intersection_visits[intersection_id] < 1 else intersection_visits[intersection_id]

    nb_visits = nb_visits_per_street[street_name]

    weight = (nb_visits/tot_cars_in_intersection)*len(list_of_streets_per_intersection[intersection_id])

    if weight < 1:
        weight = 1

    return int(weight)



def create_output(streets, paths, list_of_streets_per_intersection, nb_intersections):
    output = []
    output.append([nb_intersections])

    nb_visits_per_street = compute_street_visits(streets, paths)
    intersection_visits = group_street_visits(nb_intersections, nb_visits_per_street, streets_to_out_intersection_dict(streets))

    for i in range(nb_intersections):
        #output.append([i])
        #output.append([len(list_of_streets_per_intersection[i])])

        # output.extend()

        sub_output = [[i]]
        sub_output.append([0])

        tmp_array = []

        counter = 0
        for j in range(len(list_of_streets_per_intersection[i])):
            # output.append([list_of_streets_per_intersection[i][j][2], compute_schedule_trivial()])

            weight = assign_weights(i, nb_visits_per_street, intersection_visits, list_of_streets_per_intersection[i][j][2], list_of_streets_per_intersection)

            if weight > 0:
                counter += 1
                sub_output.append([list_of_streets_per_intersection[i][j][2], weight])

        sub_output[1] = [counter]

        output.extend(sub_output)

    return output



def main(input_file, output_file):
    array = file_to_array(input_file)

    (time, nb_intersections, nb_streets, nb_cars, nb_score_per_car, streets, paths) = parse(array)

    ordered_streets = orderByIntersection(streets, nb_intersections)

    # nb_visits_per_street = compute_street_visits(streets, paths)

    output = create_output(streets, paths, ordered_streets, nb_intersections)

    array_to_file(output, output_file)




# main(INPUT_FILES[0], OUTPUT_FILES[0])

for (input_file, output_file) in zip(INPUT_FILES, OUTPUT_FILES):
    main(input_file, output_file)

