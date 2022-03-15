import random
from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/step1")
def step1():
    return jsonify({"step":1,"message":"complete"})

@app.route("/step2", methods=['POST'])
def step2():
    r=random.randrange(3)
    return jsonify({"step":2,"message":"complete"}) if r>1 else jsonify({"step":2,"message":"failed"})

@app.route("/step3")
def step3():
    return jsonify({"step":3,"message":"complete"})

if __name__ == "__main__":
    app.run()