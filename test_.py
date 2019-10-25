
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    os.system('python GuiForSetting.py')

if __name__ == "__main__":
    app.run()

