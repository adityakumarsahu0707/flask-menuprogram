import subprocess as sp
from flask import Flask , render_template , request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return  render_template("welcome.html")

@app.route('/home')
def home():
    return render_template("lvm.html")

@app.route('/lvm-choice', methods=["GET"])
def lvm_choice():
    ch=request.args.get("choice")    
    if ch == '1':
        return("Your choice : " + ch + " : To view available storage devices")
    elif ch == '2':
        return("Your choice : " + ch + " : To view available partitions")
    elif ch == '3':
        return render_template("pv.html")
    elif ch == '4':
        return render_template("vg.html")
    elif ch =='5':
        return render_template("lv.html")
    else:
        return("Invalid choice try again!!")

@app.route('/pv')
def pv():
    return render_template("pv.html")

@app.route('/vg')
def vg():
    return render_template("vg.html")

@app.route('/lv')
def lv():
    return render_template("lv.html")

if __name__ == '__main__':
    app.run()
