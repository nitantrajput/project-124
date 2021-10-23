from flask import Flask , jsonify , request 
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Doda'
if(__name__ == '__main__'):
    app.run(debug = True)    
