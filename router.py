from flask import Flask, jsonify, request
from utils import teams as t
from main import get_team, get_details
app = Flask(__name__)

@app.route('/pointstable', methods=['GET'])
def pointsTable():
    res = get_team()
    print(res)
    response = {"data":res}
    return jsonify(response)

@app.route('/<string:name>/details', methods=['GET'])
def details(name):
    res = get_details(name)
    print(res)
    response = {"data":res}
    return jsonify(response)



if __name__=='__main__':
    app.run(debug=True)