"""
WeHelp BootCamp Assignemt - Week 4  Task 1~4
Purpose: Use flask to generate a web which need account and passcode, and calculate square
Update date: 2022/10/21
Authored by SC Siao
"""
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session

# Flask Preparation
app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
    )
app.secret_key="secret key"

admin_member_account="test"
admin_member_passcode="test"

# Home page
@app.route("/")
def index():
    return render_template("index.html") 

# Signin process
@app.route("/signin", methods=["POST"])
def signin():
    member_account=request.form["account"]
    member_passcode=request.form["passcode"]

    if member_account==admin_member_account and member_passcode==admin_member_passcode:    
        session["account"]=member_account
        return redirect("/member")
    elif member_account=="" or member_passcode=="":
        session["account"]="fail"
        return redirect("/error?message=請輸入帳號、密碼")# Specify url
    else:
        session["account"]="fail"
        return redirect("/error?message=帳號或密碼輸入錯誤")# Specify url

# Signin "Sueecee"
@app.route("/member")
def index_member():
    account_test=session.get("account","fail")
    if account_test==admin_member_account:
        return render_template("success.html")
    else:
        return redirect("/")

# Signin "Fail"
@app.route("/error")
def imdex_error():
    fail_message=request.args.get("message")    
    return render_template("error.html",error_message=fail_message)

# Signout
@app.route("/signout")
def action_signout():
    session["account"]="fail"
    return redirect("/")

# Square result
@app.route("/square/<input_number>")
def action_square(input_number):
    squ_num=int(input_number)*int(input_number)
    return render_template("calculate_square.html", ans_number=squ_num)

# Run app
if __name__ == '__main__':
    app.debug = True #Sync operator able
    app.run(port=3000)