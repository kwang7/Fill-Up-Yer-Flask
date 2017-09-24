#Kelly Wang
#SoftDev1 pd7
#HW04: Fill Up Yer Flask
#2017-09-25

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "What should cost less: a gallon of gas or a gallon of milk?"

@app.route("/yes")
def goodbye_world():
    return "Capitalism is a plague to society."

@app.route("/no")
def farewell_world():
    return "Trick question!! I can't drive and I'm lactose intolerant."

if __name__ == "__main__":
    app.debug = True
    app.run()
    
