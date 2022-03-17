def reader(file, encoding):

    cook_book = {}
    keys = ['ingredient_name', 'quantity', 'measure', ]

    with open(file, encoding=encoding) as file:

        lines = []

        for line in file:
            line = line.strip()
            if line:
                lines.append(line)
            continue

        lines = iter(lines)

        for line in lines:
            cook_book[line] = []
            num = next(lines)

            for x in range(int(num)):
                ingreds = (next(lines))
                ingrid = ingreds.split('|')
                y = zip(keys, ingrid)
                put_ingreds = {k: v for (k, v) in y}
                cook_book[line].append(put_ingreds)
                continue

            continue

        return cook_book


def get_shop_list_by_dishes(dishes, person_count: int):
    needed_ingredients = {}
    cb = reader('recipes.txt', 'utf-8')
    if type(dishes) == str:
        for x in cb[dishes]:
            needed_ingredients[x['ingredient_name']] = {'measure': x['measure'],
                                                        'quantity': int(x['quantity']) * person_count}

    if type(dishes) == list:
        for y in dishes:
            for x in cb[y]:
                needed_ingredients[x['ingredient_name']] = {'measure': x['measure'],
                                                            'quantity': int(x['quantity']) * person_count}



    return needed_ingredients


print(get_shop_list_by_dishes('Омлет', 2))
print(get_shop_list_by_dishes('Омлет', 3))
print(get_shop_list_by_dishes(['Омлет', 'Омлет'], 1))
print(get_shop_list_by_dishes(['Омлет', 'Омлет', 'tort'], 2))




