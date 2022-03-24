from  flask import Flask,render_template,redirect,request,url_for

app=Flask(__name__)

@app.route('/home', methods = ['GET','POST'])
def home():
    return render_template('content.html')


@app.route('/covid', methods =['GET', 'POST'])
def change():
    return render_template(covid.html)
    

if __name__ == '__main__':
    app.run(debug= True)