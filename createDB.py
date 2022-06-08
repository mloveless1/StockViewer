import json


def create_inv_json():
    # create dict here
    """In case we need to create the json file again"""

    inventory = {'chairs': {'category': 'chairs', 'price': 1.25, 'stock': 200, 'out': 0},
                 'long tables': {'category': 'tables', 'price': 8.00, 'stock': 17, 'out': 0},
                 'rounds': {'category': 'tables', 'price': 8.00, 'stock': 15, 'out': 0},
                 'kiddiec': {'category': 'chairs', 'price': 0.75, 'stock': 50, 'out': 0},
                 'kiddiet': {'category': 'tables', 'price': 8.00, 'stock': 10, 'out': 0},
                 }

    # turn dict to json format
    js = json.dumps(inventory)

    # open json file
    writer = open('inv.json', 'w')

    writer.write(js)  # write to file here
    writer.close()  # close file
    print('File written')


def create_order_json():
    """Function to create our orders database"""

    orders = {"0": {"items": [10,17,15], "date": "06-05-22"}, "1": {"items": [10,0,15,50,10]}, "date": "06-05-22"}

    # turn dict to json format
    js = json.dumps(orders)

    # open json file
    writer = open('orders.json', 'w')

    writer.write(js)  # write to file here
    writer.close()  # close file
    print('File written')


if __name__ == "__main__":
    print("DB created")
    create_order_json()