


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

def algo(array):

    time, nb_intersections, nb_streets, nb_cars, nb_score_per_car, streets, paths = parse(array)

    print(parse(array))

    return 0


def compute_schedule_table(streets_per_intersection, total_time, nb_cars):
    table = []
    for intersection in streets_per_intersection:
        avg_cars_per_intersection = nb_cars // len(streets_per_intersection) +1
        seconds = total_time // avg_cars_per_intersection // len(intersection)
        table.append(seconds)

        # seconds = len(intersection)
        return table



def compute_schedule_better(street_visits):
    pass


def compute_street_visits(ordered_streets, paths):
    pass

    # [
    #     [intesection_id , ["street_name", times_visited], [...],],
    #     [intesection_id , ["street_name", times_visited], [...],],
    # ]





def compute_schedule_2(nb_intersections, paths):
    pass
    


def create_output(list_of_streets_per_intersection, nb_intersections, table):
    output = []
    output.append([nb_intersections])

    for i in range(nb_intersections):
        output.append([i])
        output.append([len(list_of_streets_per_intersection[i])])
        for j in range(len(list_of_streets_per_intersection[i])):
            output.append([list_of_streets_per_intersection[i][j][2], table[i]])

    return output



def main(input_file, output_file):
    array = file_to_array(input_file)

    (time, nb_intersections, nb_streets, nb_cars, nb_score_per_car, streets, paths) = parse(array)

    ordered_streets = orderByIntersection(streets, nb_intersections)
    table = compute_schedule_table(ordered_streets, time, nb_cars)
    output = create_output(ordered_streets, nb_intersections, table)

    array_to_file(output, output_file)


# main(INPUT_FILES[0], OUTPUT_FILES[0])

for (input_file, output_file) in zip(INPUT_FILES, OUTPUT_FILES):
    main(input_file, output_file)

