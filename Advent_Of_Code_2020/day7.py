import re
outer_search = re.compile("^[a-z ]+(?= bags)")
inner_search = re.compile("\d+[a-z ]+(?= bag)")

def build_bags(data_in):
    bags = {}
    for line in data_in:
        new_bag = Bag()
        new_bag.color = outer_search.findall(line)[0]
        new_bag.contains = {}
        try:
            new_bag.contained_by = set().union(bags[new_bag.color].contained_by)
        except KeyError:
            new_bag.contained_by = set()
        bags[new_bag.color] = new_bag
        contained_bags = inner_search.findall(line)
        for contained_bag in contained_bags:
            split_bag = contained_bag.split(" ", 1)
            new_bag.contains[split_bag[1]] = int(split_bag[0])
            try:
                bags[split_bag[1]].contained_by.add(new_bag.color)
            except KeyError:
                inside_bag = Bag()
                inside_bag.color = split_bag[1]
                inside_bag.contained_by = set()
                inside_bag.contained_by.add(new_bag.color)
                bags[inside_bag.color] = inside_bag
    return bags

def part_one(bags, bag_color):
    list_of_contained_by = list(bags[bag_color].contained_by)
    for color in list_of_contained_by:
        new_additions = list(bags[color].contained_by)
        for add_color in new_additions:
            if add_color not in list_of_contained_by:
                list_of_contained_by.append(add_color)
    return len(list_of_contained_by)

def part_two(bags, bag_color):
    total_contained = sum(bags[bag_color].contains.values())
    contained = bags[bag_color].contains.keys()
    for contained_bag in contained:
        total_contained += part_two(bags, contained_bag) * bags[bag_color].contains[contained_bag]
    return total_contained

class Bag:
    color = ""
    contained_by = set()
    contains = {}

with open("input7.txt" , "r") as f:
	data = f.read().split("\n")

all_bags = build_bags(data)

print("Part One: " + str(part_one(all_bags, "shiny gold")))
print("Part Two: " + str(part_two(all_bags, "shiny gold")))