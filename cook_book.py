def get_cook_book():
    cook_book    = {}
    current_dish = ''
    ingredient   = []
    num_rows     = 0
    with open('cook_book.txt') as f:
        for idx, l in enumerate(f): 
            if len(l.strip()) > 0 and l.strip().find('|') == -1 and not l.strip().isdigit() and not l.strip().isnumeric():
                cook_book[l.strip()] = []
                current_dish = l.strip()
                cook_book[current_dish] = []
            elif l.strip().isnumeric():
                num_rows = l.strip()
            elif l.strip().find('|') != -1:
                ingredient = l.strip().split('|')
                cook_book[current_dish].append({'ingredient_name': ingredient[0].strip(), 'quantity': ingredient[1].strip(), 'measure': ingredient[2].strip() }) 
    return cook_book


def print_cook_book(cook_book):
    for key in cook_book.keys():
        print('\nБлюдо: ', key)
        for item in cook_book[key]:
           print(item) 


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = get_cook_book()
    shop_list = {}
    for dish in dishes:
      if dish in cook_book.keys():
         for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in shop_list.keys():
                shop_list[ingredient['ingredient_name']]['quantity'] += person_count*int(ingredient['quantity'])  
            else:
                shop_list[ingredient['ingredient_name']] = {'quantity': person_count*int(ingredient['quantity']), 'measure': ingredient['measure'] }
    return shop_list


cook_book = get_cook_book()
shop_list = get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)
print(shop_list)
#print_cook_book(cook_book)