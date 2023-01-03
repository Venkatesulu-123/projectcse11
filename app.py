from flask import Flask,render_template,request,redirect
import sqlite3
app = Flask(__name__)

# --------------------------------indexpage---------------------------
@app.route('/')
def index():
    return render_template('index.html')

# --------------------------------registerpage---------------------------
@app.route('/register',methods=['POST','GET'])
def register():
    if request.method == "POST":
# sqlite"C:\Users\91630\Desktop\project in github\finalproject-master\app_data.db"
        connection = sqlite3.connect("C:\\Users\\91630\\Desktop\\project in github\\finalproject-master\\app_data.db")
        cursor = connection.cursor()

#Html form
        name=request.form['name']
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        confirmpassword=request.form['confirmpassword']
        data=[name,username,email,password,confirmpassword]
        #print(name,username,email,password,confirmpassword)
        if(password == confirmpassword):
                    query="INSERT INTO registerdata(name,username,email,password,confirmpassword) VALUES (?,?,?,?,?)"
                    cursor.execute(query,data)
                    connection.commit()
                    return redirect('/login')
        else:
            return "password not matched"
    return render_template('register.html')

# --------------------------------loginpage---------------------------
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
# sqlite
        connection = sqlite3.connect("C:\\Users\\91630\\Desktop\\project in github\\finalproject-master\\app_data.db")
        
        cursor = connection.cursor()

#Html form
        username=request.form['namelogin']
        password=request.form['passwordlogin']

       # print(username,password)
#query
        query = "SELECT username,password FROM registerdata where username='"+username+"' and password='"+password+"'"
        cursor.execute(query)

        results = cursor.fetchall()

#validation
        if len(results) == 0:
            return "userid and password is incorrect"
        else:
            return redirect("/home")
    return render_template('login.html')

# --------------------------------homepage---------------------------
@app.route('/home')
def home():
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)