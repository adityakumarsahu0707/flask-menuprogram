import subprocess as sp
import os
from flask import Flask , render_template , request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return  render_template("welcome.html")

@app.route('/home')
def home():
    return render_template("lvm.html")

@app.route('/output', methods=["GET"])
def lvm_choice():
    pv = '0'
    vg = '0'
    lv = '0'
    pv=request.args.get("pv-value")
    vg=request.args.get("vg-value")
    lv=request.args.get("lv-value")
    if pv == "1":
      output = sp.getoutput("pvdisplay ")
      return "<pre> " + output +"</pre>"
    elif pv == "2":
      return render_template("pv-cre.html")
    elif pv == "3":
      return render_template("pv-del.html")
    elif vg == "1":
      output = sp.getoutput("vgdisplay ")
      return "<pre>" + output +"</pre>"
    elif vg == "2":
      return vg
    elif vg == "3":
      return vg
    elif lv == "1":
      output = sp.getoutput("lvdisplay ")
      return "<pre> " + output +"</pre>"
    elif lv == "2":
      return lv
    elif lv == "3":
      return lv
    elif lv == "4":
      return lv
    elif lv == "5":
      return lv
    else:
      return " Wrong Input Please Retry"
@app.route('/pv/')
def pv():
    return render_template("pv.html")

@app.route('/pv-create/')
def pvcreate():
    disk=request.args.get("pv-disk-name")
    output=sp.getstatusoutput("echo y | pvcreate " + disk)
    if output[0]==0:    
      return "<b> Persistent Volume Created Successfully!!</b>"
    else:    
      return "<b> !!Something went Wrong!!</b>"
@app.route('/pv-delete/')
def pvdelete():
    disk=request.args.get("pv-disk-name")
    output=sp.getstatusoutput("pvremove -f " + disk)
    if output[0]==0:    
      return "<b> Persistent Volume Deleted Successfully!!</b>"
    else:    
      return "<b> !!Something went Wrong!!</b>"

@app.route('/vg/')
def vg():
    return render_template("vg.html")

@app.route('/vg-create/')
def vgcreate():
    disk=request.args.get("vg-disk-name")
    pv=request.args.get("pv-name")
    output=sp.getstatusoutput("vgcreate " + disk + ' ' + pv)
    if output[0]==0:    
      return "<b> Volume Group Created Successfully!!</b>"
    else:    
      return "<b> !!Something went Wrong!!</b>"
@app.route('/vg-delete/')
def vgdelete():
    disk=request.args.get("vg-disk-name")
    output=sp.getstatusoutput("vgremove -f " + disk)
    if output[0]==0:    
      return "<b> Volume Group Deleted Successfully!!</b>"
    else:    
      return "<b> !!Something went Wrong!!</b>"

@app.route('/lv/')
def lv():
    return render_template("lv.html")

@app.route('/lv-create/')
def lvcreate():
    val=request.args.get("choice")
    return render_template("pv.html")


if __name__ == '__main__':
    app.run()
