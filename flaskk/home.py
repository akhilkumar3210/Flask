from flask import Flask,render_template,request,redirect
import sqlite3

app=Flask(__name__)

@app.route('/')
def sample():
    return "Welcome To Home"

@app.route('/index',methods=['GET','POST'])
def Index():
    con=sqlite3.connect("hm.db")
    try:
        con.execute("create table student(name text,age int)")
    except:
        print('Created table')
    
    if request.method=='POST':
        name=request.form['name']
        age=request.form['age']
        con.execute("insert into student(name,age)values(?,?)",(name,age))
        con.commit()
        return redirect('index')
    return render_template('index.html')

@app.route('/nex')
def Next():
    return render_template('next.html')
app.run()

"{{ url_for(  'static' , filename=