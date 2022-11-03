"""

***| Blueprint: API and sign up/in/out route |***

WeHelp BootCamp Assignemt - Week 7  Task
Update date: 2022/11/03
Authored by SC Siao
"""

from flask import Blueprint
from flask import request
from flask import redirect
from flask import render_template
from flask import session
import mysql.connector
import json


# Separate program
api_w7 = Blueprint(
    "api_w7",
    __name__,
    static_folder="static",
    static_url_path="/",
    template_folder="templates"
)

# Change data to front-end SPEC form
def search_data_form(sql_result):
    print(">>",sql_result)
    if sql_result!=[]:
        process_result={
            "data":{
                "id":sql_result[0][0],
                "name":sql_result[0][1],
                "username":sql_result[0][2]
            }
        }
    else:
        process_result={
            "data":None
        }
        print("go else")
    print("??",process_result)
    return process_result

# MySQL connect and input/output
def get_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123",
        database="website",
        charset="utf8"
)

def query_data_read(sql_command):
    conn=get_connect()
    try:
        cursor=conn.cursor()
        cursor.execute(sql_command)
        return cursor.fetchall()
    finally:
        conn.close()

def query_data(sql_command,input):
    conn=get_connect()
    try:
        cursor=conn.cursor()
        cursor.execute(sql_command,input)
        return cursor.fetchall()
    finally:
        conn.close()

def insert_or_update_data(sql_command,input):
    conn=get_connect()
    try:
        cursor=conn.cursor()
        cursor.execute(sql_command,input)
        conn.commit()
        return cursor.fetchall()
    finally:
        conn.close()

# Home page
@api_w7.route("/")
def index():
    return render_template("index.html") 

# Signup process
@api_w7.route("/signup", methods=["POST"])
def signup():
    # Get information from user input
    member_signup_name=request.form["signupName"]
    member_signup_account=request.form["signupAccount"]
    member_signup_password=request.form["SignupPassword"]

    # Check if the user input is OK or not from MySQL
    sql_member_data="SELECT name,username FROM member WHERE name=%s or username = %s"
    member_verify=(member_signup_name,member_signup_account)
    member_datas=query_data(sql_member_data,member_verify)
    if len(member_datas)!=0:
        for member_datas_ls in member_datas:
            if member_datas_ls[0]==member_signup_name:
                name_check=1
            else:
                name_check=0
            if member_datas_ls[1]==member_signup_account:
                account_check=1
            else:
                account_check=0
    else:
        account_check=0
        name_check=0

    # Excute the signup or show the error
    if name_check==0 and account_check==0 and member_signup_name!="" and member_signup_account!="" and member_signup_password!="":
        sql_command="INSERT INTO member (name, username, password) VALUES (%s,%s,%s)"
        session["name"]=member_signup_account
        session["account"]=member_signup_account
        session["password"]=member_signup_account
        member_input=(member_signup_account,member_signup_account,member_signup_account,)
        insert_or_update_data(sql_command,member_input)
        return redirect("/")
    elif name_check!=0:
        return redirect("/error?message=姓名有人取過啦，要不要去認親")
    elif account_check!=0:
        return redirect("/error?message=帳號有人取過啦，很沒創意喔")
    elif member_signup_name=="" or member_signup_account=="" or member_signup_password=="":
        return redirect("/error?message=姓名、帳號、密碼  請勿留空")
    else:
        session["account"]="fail"
        return redirect("/error?message=帳號已經被註冊")

# Signin process
@api_w7.route("/signin", methods=["POST"])
def signin():
    # Get information from user input
    member_account=request.form["account"]
    member_password=request.form["password"]

    # Check if the user identifition from MySQL
    sql_member_data="SELECT id,name,username,password FROM member"
    sql_member_datas=query_data_read(sql_member_data)
    target_member_account=member_account
    target_member_password=member_password
    member_or_not=0
    password_right_or_not=0
    for verify in sql_member_datas:
        if target_member_account==verify[2]:
            print(verify[2])
            member_or_not=1
            if target_member_password==verify[3]:
                password_right_or_not=1
                member_id=verify[0]
                membert_name=verify[1]   
    
    # Excute the signin or show the error
    if  member_or_not==1 and password_right_or_not==1 and member_account!="" and member_password!="":    
        session["account"]=member_account
        session["member_id"]=member_id
        session["name"]=membert_name
        return redirect("/member")
    elif member_account=="" or member_password=="":
        session["account"]="fail"
        return redirect("/error?message=請輸入帳號、密碼")# Specify url
    else:
        session["account"]="fail"
        return redirect("/error?message=帳號或密碼輸入錯誤")# Specify url

# Leave a content
@api_w7.route("/content", methods=["POST"])
def index_content():
    member_content=request.form["memberContent"]
    sql_member_id=str(session.get("member_id","fail")) # need specify type to string
    sql_member_content_command="INSERT INTO message (member_id, content) VALUES (%s,%s)"
    content_input=(sql_member_id,member_content)
    insert_or_update_data(sql_member_content_command,content_input)
    return redirect("/member")

# Signin "Sueecee"
@api_w7.route("/member")
def index_member():
    # Get the user information from cookie
    account_cookie=session.get("account","fail")
    name_cookie=session.get("name","fail")
    
    # Excute the render and show the message from MySQL databases
    if account_cookie!="fail":
        sql_show="SELECT member.name, message.content FROM member INNER JOIN message ON member.id=message.member_id;"
        data_show=query_data_read(sql_show)
        return render_template("success.html",member_name=name_cookie,member_connect_HTML=data_show)
    else:
        return redirect("/")

# Signin "Fail"
@api_w7.route("/error")
def imdex_error():
    fail_message=request.args.get("message")    
    return render_template("error.html",error_message=fail_message)

# Signout
@api_w7.route("/signout")
def action_signout():
    session["account"]="fail"
    return redirect("/")

# member Search API
@api_w7.route("/api/member", methods=["GET"])
def member_search():
    account_cookie=session.get("account","fail")
    name_cookie=session.get("name","fail")
    if account_cookie=="fail" or name_cookie=="fail":
        print("Fail method")
        data=[]
        data=json.dumps(search_data_form(data))        
    else:
        username=request.args.get("username")
        username=str(username)
        sql="""
        SELECT id,name,username
        FROM member WHERE username=%s;
        """
        sql_username=(username,)
        # print(sql_username)
        data=query_data(sql,sql_username)
        data=json.dumps(search_data_form(data))
        print("User "+account_cookie+" is searchong "+username+"'s name.")
    return data

# member Rename
@api_w7.route("/api/member", methods=["PATCH"])
def member_rename():
    account_cookie=session.get("account","fail")
    name_cookie=session.get("name","fail")

    if account_cookie=="fail" or name_cookie=="fail":
        print("Fail method")
        data=json.dumps({"error":True})
    else:
        req_name=request.get_json()
        rename=req_name["name"]
        sql="""
        UPDATE member 
        SET name= %s
        WHERE username= %s;
        """
        sql_var=(rename,account_cookie)
        insert_or_update_data(sql,sql_var)
        print("Name has been renamed from "+name_cookie+" to "+rename)
        session["name"]=rename
        data=json.dumps({"ok":True})
    return data