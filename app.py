from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route for the root URL ("/") and a function to handle it
@app.route("/")
def hello_world():
    return "Hello, World!"

# Run the application if this script is executed
if __name__ == "__main__":
    print("hello")
    app.run()