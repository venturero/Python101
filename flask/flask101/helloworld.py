#this code will get this output: Not Found

from flask import Flask

app = Flask(__name__)


if __name__ =="__main__":
    app.run(debug=True)
