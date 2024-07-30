cook_book = {}
with open('recept.txt', encoding='utf-8') as f:

    for line in f:
            dish = line.strip()
            ingredients_count = int(f.readline())
            ingredients = []
            for i in range(ingredients_count):
                ingredient = f.readline().strip()
                ingredient_name,quantity, measure = ingredient.split("|")
                ingredients.append({
                    'ingredient_name': ingredient_name, 
                    'quantity': quantity, 
                    'measure': measure
                })

            cook_book[dish] = ingredients
            f.readline().strip()

#print(cook_book)
# 2 задание
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = int(ingredient['quantity']) * person_count
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity

            else:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}


    return shop_list

#print(get_shop_list_by_dishes(['Омлет'],1))
#3 задание
names =  ['1.txt','2.txt','3.txt']
f_list = []
for name in names:
    with open(name, encoding='utf-8') as f:
            l_1 = f.readlines()
            num_lines = len(l_1)
            f_list.append([num_lines, name, l_1])

f_list.sort()

with open('task.txt', 'w', encoding='utf-8') as f:
    
    for i in f_list:
        
        f.write(f'{i[1]}\n')
        f.write(f'{i[0]}\n')
        f.write(''.join(i[2]) + '\n')