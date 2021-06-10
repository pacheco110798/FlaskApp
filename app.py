from flask import Flask, render_template#----------------------->Import Flask class fro the framework and render_template for the views
app= Flask(__name__)

@app.route('/hello')#------------------------------->*use the route() decorator to tell Flask what URL should trigger our function.
def hello_world():
	return '<h1>Hello, World<h1>'
@app.route('/')
@app.route('/home')
def home_page():
	return render_template('home.html')
'''
@app.route('/about')
def about_page():
	return '<h2>This is my about page</h2>'
'''
@app.route('/about/<username>')
def about_page(username):
	return f'<h1>This is the abot page of {username}</h1>'

@app.route('/market')
def market_page():
	items = [
    {'id': 1, 'name': 'Tshirt', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Tshirt', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Hoodie', 'barcode': '231985128446', 'price': 150}
]
	return render_template('market.html',items=items)