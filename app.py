from flask import Flask, request, render_template, redirect
import inv_edit as inv
import order_edit as orders
import pandas as pd

app = Flask(__name__)


@app.route("/", methods=("POST", "GET"))
def display_all():
    """Endpoint to show all the items in our inventory and forms to interact with the data"""
    # pull inventory data
    inv_data = inv.display_all()

    # turns our json data into a dataframe for easy viewing
    df = pd.DataFrame.from_dict(inv_data, orient='index')
    # for the overview of the stock we do not need to see what items are checked out. So pop the data.
    df.pop('out')

    # list for dropdown boxes with our product names since they differ from our keys
    selections = []
    # list with the keys of our json file/database which will be the product ID number of each item
    keys = inv_data.keys()
    # the names of our items into our selections list so that we can list them in a dropdown box
    for i in inv_data:
        selections.append(inv_data[i]['name'])
    # render our table into HTML, pass our lists and dataframes
    if request.form.get("actions") == 'checkout':
        inv.check_out(request.form.get("items"), request.form.get("amount"))

    print(request.form.get("amount"))
    return render_template('display_all.html', keys=keys, selections=selections, tables=[df.to_html()],
                           titles=df.columns.values)


@app.route("/update")
def update_inventory():
    """Endpoint to handle our inventory actions"""
    if request.args.get("actions") == 'checkout':
        inv.check_out(request.args.get("item"), int(request.args.get("amount")))
    elif request.args.get("actions") == 'checkin':
        inv.check_in(request.args.get("item"), int(request.args.get("amount")))
    elif request.args.get("actions") == 'delete':
        inv.delete_prod(request.args.get("item"))
    return redirect("/")


@app.route("/stock_by_date")
def show_stock():
    """Endpoint to view the stock by the date inputted by the user invalid input will just redirect for now"""
    user_date = request.args.get('date')
    df = orders.view_stock_by_date(user_date)

    if df is not None:
        return render_template('stock_by_date.html', tables=[df.to_html()],
                               titles=df.columns.values, date=user_date)
    else:
        return redirect("/")
