import bcrypt
import hashlib
import sqlite3
import uuid
from datetime import datetime

from django.shortcuts import render


# Create your views here.
def loadhomepage(request):
    return render(request, "home.html")
def loadhome(request):
    return render(request, "home.html")
def loadsignup(request):
    return render(request, "signup.html")
def loadcontact(request):
    return render(request, "contact.html")
def loadabout(request):
    return render(request, "about.html")
def loadlogin(request):
    return render(request, "login.html")
def profileinfopro(request):
    return render(request, "profile_provider.html")
def profileinfoseek(request):
    return render(request, "profile_seeker.html")
def homepro(request):
    return render(request, "dash_provider.html")
def homeseek(request):
    return render(request, "dash_seeker.html")
def loadseetingseek(request):
    return render(request, "dash_seeker.html")
def loadsettingspro(request):
    return render(request, "profile_provider.html")
def upload(request):
    return render(request, "upload_job.html")
def loadjp(request):
    return render(request, "loginjp.html")
def loadjs(request):
    return render(request, "loginjs.html")
def loadcomplain(request):
    return render(request, "complain_seeker.html")
def notificationpro(request):
    return render(request, "notification_provider.html")
def notificationseek(request):
    return render(request, "notification_seeker.html")
def loadfeedback(request):
    return render(request, "feedback_seeker.html")
def viewcomplain(request):
    return render(request, "view_complain.html")
def viewfeedback(request):
    return render(request, "view_feedback.html")
def jobinfo(request):
    return render(request, "views_job.html")
def loadcontactcode(request):
    return render(request, "contact.html")
def searchjob(request):
    return render(request,"searchjob.html")
def settingseeker(request):
    return render(request, "setting_seeker.html")

def signupaction(request):
    try:
        fullname = request.POST['fln']
        email = request.POST['mail']
        contact = request.POST['num']
        gender = request.POST['gen']
        dateofbirth = request.POST['dob']
        address = request.POST['adr']
        country = request.POST['country']
        jobpost = request.POST['post']
        userid = request.POST['uid']
        salt = bcrypt.gensalt()
        pwd = request.POST['pwd']
        password = bcrypt.hashpw(pwd.encode(),salt)
        print(password)
        # password = request.POST['pwd']
        cnt = sqlite3.connect("db.sqlite3")
        operation = cnt.cursor()
        sql = "insert into usertable values (?,?,?,?,?,?,?,?,?,?)"
        values = (fullname, email, contact, gender, dateofbirth, address, country, jobpost, userid, password)
        operation.execute(sql, values)
        cnt.commit()
        cnt.close()
        if jobpost == 'JOB PROVIDER':
            return render(request, "dash_provider.html")
        elif jobpost == 'JOB SEEKER':
            return render(request, "dash_seeker.html")
    except Exception as error:
        print(error)
        return render(request, "home.html")


def loginjsaction(request):
    userid = request.POST['uid']
    # salt = uuid.uuid4().hex
    pwd = request.POST['pwd']
    # password =hashlib.sha512(pwd+salt).hexdigest()

    cnt = sqlite3.connect("db.sqlite3")
    operation = cnt.cursor()
    sql = "select * from usertable where userid=? and password=?"
    values = (userid, pwd)
    result = operation.execute(sql, values)
    if result.fetchone():
        return render(request, "dash_seeker.html")
    else:
        return render(request, "login.html", {'uid': userid, 'pwd': password})


def loginjpaction(request):
    userid = request.POST['uid']
    password = request.POST['pwd']

    cnt = sqlite3.connect("db.sqlite3")
    operation = cnt.cursor()
    sql = "select * from usertable where userid=? and password=?"
    values = (userid, password)
    result = operation.execute(sql, values)
    if result.fetchone():
        return render(request, "dash_provider.html")
    else:
        return render(request, "login.html", {'uid': userid, 'pwd': password})


def profileprovider(request):
    userid = request.POST['uid']
    password = request.POST['pwd']
    cnt = sqlite3.connect("db.sqlite3")
    operation = cnt.cursor()
    sql = "select * from usertable where userid=? and password=?"
    values = (userid, password)
    result = operation.execute(sql, values)
    if result.fetchone():
        sql = "delete from usertable where userid=? and password=?"
        values = (userid, password)
        operation.execute(sql, values)
        cnt.commit()
        return render(request, "home.html")
    else:
        return render(request, "profile_provider.html", {'uid': userid, 'pwd': password})


def profileseeker(request):
    userid = request.POST['uid']
    password = request.POST['pwd']
    cnt = sqlite3.connect("db.sqlite3")
    operation = cnt.cursor()
    sql = "select * from usertable where userid=? and password=?"
    values = (userid, password)
    result = operation.execute(sql, values)
    if result.fetchone():
        sql = "delete from usertable where userid=? and password=?"
        values = (userid, password)
        operation.execute(sql, values)
        cnt.commit()
        return render(request, "home.html")
    else:
        return render(request, "profile_seeker.html", {'uid': userid, 'pwd': password})


def uploadaction(request):
    userid = request.POST['uid']
    jobid = request.POST['jid']
    contactNo = request.POST['num']
    jobtype = request.POST['typ']
    jobdescription = request.POST['des']
    labour = request.POST['lbr']
    status = request.POST['status']
    location = request.POST['loc']
    cnt = sqlite3.connect("db.sqlite3")
    operation = cnt.cursor()
    sql = "insert into jobdetail values (?,?,?,?,?,?,?)"
    values = (userid, jobid, contactNo, jobdescription, labour, status, location, jobtype)
    operation.execute(sql, values)
    cnt.commit()
    cnt.close()
    return render(request, "dash_provider.html")


def complain(request):
    userid = request.POST['uid']
    jobid = request.POST['jid']
    complaindes = request.POST['com']
    cnt = sqlite3.connect("db.sqlite3")
    operation = cnt.cursor()
    sql = "insert into complain values (?,?,?,?,?)"
    values = (userid, jobid, complaindes, "under process", datetime.now())
    operation.execute(sql, values)
    cnt.commit()
    cnt.close()
    return render(request, "complain_seeker.html")


def feedback(request):
    userid = request.POST['uid']
    jobid = request.POST['jid']
    feedback = request.POST['fed']
    cnt = sqlite3.connect("db.sqlite3")
    operation = cnt.cursor()
    sql = "insert into feedback values (?,?,?,?)"
    values = (userid, jobid, feedback, datetime.datetime.now())
    operation.execute(sql, values)
    cnt.commit()
    cnt.close()
    return render(request, "feedback_seeker.html")

def complainactcode(request):
    cnt = sqlite3.connect("db.sqlite3")
    operation = cnt.cursor()
    sql = "select * from complain"
    result = operation.execute(sql)
    records = result.fetchall()
    return render(request, "view_complain.html", {'list': records})


def feedbackurl(request):
    cnt = sqlite3.connect("db.sqlite3")
    operation = cnt.cursor()
    sql = "select * from feedback"
    result = operation.execute(sql)
    records2 = result.fetchall()
    return render(request, "view_feedback.html", {'list2': records2})


def jobinfourl(request):
    cnt = sqlite3.connect("db.sqlite3")
    operation = cnt.cursor()
    sql = "select * from jobdetail"
    result = operation.execute(sql)
    records3 = result.fetchall()
    return render(request, "views_job.html", {'list3': records3})

def contacturl(request):
    FULLNAME = request.POST['fnm']
    MAILID = request.POST['mail']
    ADDRESS = request.POST['add']
    COUNTRY = request.POST['cnt']
    cnt = sqlite3.connect("db.sqlite3")
    operation = cnt.cursor()
    sql = "insert into contact values (?,?,?,?)"
    values = (FULLNAME, MAILID, ADDRESS, COUNTRY)
    operation.execute(sql, values)
    cnt.commit()
    cnt.close()
    return render(request,"home.html")
