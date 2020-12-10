from collections import defaultdict

test_data="""light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

def load_data():
    with open("aoc20-07-data.txt", "r") as f:
        data = f.read().splitlines() 
    print("Loaded lines:", len(data))
    return data

data = load_data()
#data = test_data.split('\n')

contain = defaultdict(list)
included = defaultdict(list)

for line in data:
    main_bag, content = line.replace('.','').replace('bags','bag').split(' contain ')
    if content!='no other bag':
        bags = content.split(', ')
        for el in bags:
            index = el.find(' ')
            count = int(el[:index])
            bag_name = el[index+1:]
            contain[main_bag].append((count, bag_name))
            included[bag_name].append(main_bag)


def get_roots(included, bag):
    roots=set()
    nodes = included[bag]
    for el in nodes:
        roots = roots.union(get_roots(included, el))
    roots.add(bag)
    return roots

def count_bags(contain, bag):
    result = 1
    nodes = contain[bag]
    for el in nodes:
        result += el[0] * count_bags(contain, el[1])

    return result

print('-----')
print('Result 1 = ',len(get_roots(included,'shiny gold bag')) - 1)
print('Result 2 = ',count_bags(contain,'shiny gold bag') - 1)
