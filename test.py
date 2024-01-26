from flask import Flask, request, redirect, render_template, url_for
import sqlite3
import json

app = Flask(__name__)





@app.route('/')
def index():
    return render_template('index.html')



#@app.route('/Display/')
#def display():
    #return render_template('Display.html',information="a test message")

@app.route('/Display/')
def display():
    with sqlite3.connect("test.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM information ORDER BY ID DESC LIMIT 1")
        row = cur.fetchone()  # 获取结果中的一行数据
        return render_template('Display.html', information=row[1])

@app.route('/Trans/', methods=['POST'])
def trans():
    data = request.json  # 获取传输的JSON数据
    json_string = json.dumps(data)
    with sqlite3.connect("test.db") as conn:
        cur=conn.cursor()
        cur.execute("INSERT INTO information (content) VALUES (?)",(json_string,))
        conn.commit()
        return redirect(url_for("index"))

@app.route('/add/')
def add():
    #provide result and return the target html file
    return render_template("add_track.html")

@app.route('/add/track',methods=['POST'])
def add_track():
    if request.method=='POST':
        #get the input value
        question=request.form['question'] 

        
        return render_template('result.html', question=question, answer=question)
        

@app.route('/Function3/')
def Function3():
    return render_template('Function3.html')



# === Do not modify or add code after this line ===
def main():
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    main()
