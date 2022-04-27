from flask import Flask, json, jsonify, request
app = Flask(__name__)

todos = []

@app.route('/todos', methods = ['GET','POST'])
def handle_todos():
    if request.method == 'GET':
        return jsonify(todos)

    if request.method == 'POST':
        todos.append(json.loads(request.data))
        return jsonify(todos)

@app.route('/todos/<int:position>', methods = ['DELETE'])
def delete_todos(position):
    todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug = True)
