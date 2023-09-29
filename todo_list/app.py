from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'hello': 'world'})


def main():
    app.run(debug=True, host='0.0.0.0', port=8888)


if __name__ == '__main__':
    main()
