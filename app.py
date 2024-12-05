from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/spendings')
def spendings():
    return render_template('spendings.html')

@app.route('/assistant')
def assistant():
    return render_template('assistant.html')

@app.route('/account')
def account():
    return render_template('account.html')

if __name__ == '__main__':
    app.run(debug=True) 
    # from waitress import serve
    # serve(app, host='0.0.0.0', port=8080)