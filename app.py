from flask import Flask,render_template,request
import pickle
import numpy as np



model = pickle.load(open('iris.py','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/view',methods = ['GET','POST'])
def view():
    S_length = request.form['S_length']
    S_width = request.form['S_width']
    P_length = request.form['P_length']
    P_width = request.form['P_width']
    arr = np.array([[S_length,S_width,P_length,P_width]])
    predict = model.predict(arr)
    print(predict)
    return render_template('view.html', data=predict)

if __name__ =="__main__":
    app.run(debug=True)