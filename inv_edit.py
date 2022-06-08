import json

json_file_path = 'inv.json'


def display_all():
    """This function is to display the entire product list only here for demo purposes"""
    import json

    # open file in read mode, read it, load it for later use
    with open(json_file_path, 'r') as f:
        inv_data = json.load(f)
    f.close()
    return inv_data


def check_out(product, n):
    """Takes items out of stock and moves them to items that are checked out"""
    # open our json and turn it into a dictionary
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    f.close()
    if data[product]['stock'] >= n:
        data[product]['out'] += n
        data[product]['stock'] -= n
    else:
        print("You cannot check out more than {n} {product}".format(n=data[product]['stock'], product=product))
    with open(json_file_path, 'w') as f:
        json.dump(data, f)
        f.close()


def check_in(product, n):
    """Checks items back into the stock"""
    with open(json_file_path, 'r') as f:
        data = json.load(f)
        f.close()
    if data[product]['out'] >= n:
        data[product]['stock'] += n
        data[product]['out'] -= n
    else:
        print("You only have {n} {product} out".format(n=data[product]['out'], product=product))
    with open(json_file_path, 'w') as f:
        json.dump(data, f)
        f.close()


def delete_prod(product):
    with open(json_file_path, 'r') as f:
        data = json.load(f)
        f.close()
    # if the product exists remove it from the dictionary
    if product in data.keys():
        data.pop(product)
        print('Item removed from inventory')
    else:
        print('Item does not exist')

    with open(json_file_path, 'w') as f:
        json.dump(data, f)
        f.close()

# tester here


if __name__ == '__main__':
    # tester here
    action, item, number = input("Enter action:").split()
    if action == 'out':
        check_out(item, int(number))
    elif action == 'in':
        check_in(item, int(number))
    elif action == 'delete':
        delete_prod(item)
    else:
        display_all()
