from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'messgae' : 'Hello World'
    })

if __name__ == '__main__':
    app.run()




# '/api/v1/details'
# '/api/v1/healthz'