from flask import Flask,render_template,request
from test import connect_with_blockchain

app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/handleclick',methods=['post'])
def cal():
    a=int(request.form['text'])
    c,w=connect_with_blockchain()
    h=c.functions.reverseDigits(a).transact()
    w.eth.waitForTransactionReceipt(h)
    r=c.functions.getResult().call()
    return render_template('index.html', v = r)
    


if __name__ == '__main__':
    app.run(debug=True)