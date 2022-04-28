from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def main():
   return render_template('index.html')


@app.route("/index")
def index():
   return render_template('index.html')

@app.route("/cart")
def cart():
    return render_template('cart.html')

@app.route("/groups")
def groups():
    return render_template('groups.html')


@app.route("/products")
def products():
   return render_template('products.html')

if __name__ == "__main__":
   app.run()
