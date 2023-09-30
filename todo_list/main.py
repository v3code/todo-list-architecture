from todo_list.app import app
from flask import jsonify
# import todo_list.task.routes

# Domains

# 1. Users
# 2. Tasks
# 3. Workspace
@app.route('/', methods=['GET'])
def index():
    return jsonify({'hello': 'world'})


def main():
    app.run(debug=True, port=8888)


if __name__ == '__main__':
    main()
