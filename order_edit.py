# imports
import json
from datetime import date
import pandas as pd

# today's date, so I don't have to type the entire function again
today = str(date.today().strftime("%m-%d-%y"))
# paths to our json files that are used so that I don't have to type them anymore
order_json_file_path = 'orders.json'
inv_json_file_path = 'inv.json'


def view_stock_by_date(user_date=today):
    """To view the stock by the date inputted by the user, by default it will be current day's date"""
    # Order JSON opened and read here
    with open(order_json_file_path, 'r') as order_file:
        order_data = json.load(order_file)
    order_file.close()
    # Inventory JSON opened and read here
    with open(inv_json_file_path, 'r') as inv_file:
        inv_data = json.load(inv_file)
    inv_file.close()

    # Initialize list to create a matrix holding all of our order quantities
    items_data = []
    # Iterates through our order data
    for i in order_data:
        # if this records contains the date requested, add the quantities of the order to another list
        if user_date == order_data[i]['date']:
            items_data.append(order_data[i]['items'])
    # if no records were found return nothing
    if not items_data:
        return None
    # got through each list in the array
    for order in items_data:
        # Counter here to be used as a key for the inv_data
        # Starts with chairs or 0
        count = 0
        # go through each element in the list
        for item in order:
            # update the quantities for each item according to what item we are on in the list
            # so, every element with the index of 0 will update the inventory data at key 0 or chairs
            # converted count to string because the number is our key, so it needs to be a string
            inv_data[str(count)]['out'] += item
            inv_data[str(count)]['stock'] -= item
            # increment our counter, so we can update quantities for the elements at index + 1
            count += 1
    # since we found the records we wanted and have updated our inventory accordingly, we will now return our DF
    # cont. for easy viewing in our webpage
    df = pd.DataFrame.from_dict(inv_data, orient='index')
    return df


if __name__ == "__main__":
    view_stock_by_date()
