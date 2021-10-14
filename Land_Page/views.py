from django.shortcuts import render, HttpResponse
from . send_otp import sendOtp
from django.views.decorators.csrf import csrf_exempt
from random import randint
import mysql.connector as conn
from datetime import date

'''Establishing Connection between database (final_task) with object (conn)'''
conn = conn.connect(host='localhost', user = 'root', passwd = 'Gaurav@123', database = 'final_task')
cur = conn.cursor()

def login(request):
    return render(request, 'LogIn.html')

@csrf_exempt
def signup(request):
    return render(request, 'SignUp.html')

@csrf_exempt
def send_otp(request):
    mobileNo = request.POST.get('mobile_no')
    password = request.POST.get('password')

    global temp_mobileNo
    global temp_password
    temp_mobileNo = mobileNo
    temp_password = password

    '''Renerating random otp'''
    global generateOtp
    generateOtp = randint(1000, 9999)

    '''otp is sent through function sendOtp'''
    if ((len(mobileNo) == 10) and (password != '')):
        sendOtp(generateOtp, mobileNo)

        return render(request, 'otp.html')
    else:
        return render(request, 'SignUp.html')

@csrf_exempt
def verifyOtp(request):
    receivedOtp = request.POST.get('otp')
    receivedOtp = int(receivedOtp)


    if receivedOtp == generateOtp:

        '''mobile no, password and otp added to database ignoring NULL values'''
        param1 = ("INSERT IGNORE INTO table_1(id, mobile_no, otp, expire_time, created_time, password) VALUES(%s,%s,%s,%s,%s,%s)")
        param2 = (temp_mobileNo, temp_mobileNo, receivedOtp, None, None, temp_password)

        cur.execute(param1, param2)
        conn.commit()

        return render(request, 'LogIn.html')
    else:
        return render(request, 'otp.html')

@csrf_exempt
def login_request(request):
    if 'Proceed_LogIn' in request.POST:
        received_mobileNo = request.POST.get('received_mobile_no')
        received_password = request.POST.get('received_password')
        try:
            received_mobileNo = int(received_mobileNo)
            query = "select * from table_1 where mobile_no = %s"
            data = cur.execute(query, (received_mobileNo,))
            received_data = cur.fetchall()

            '''accessing mobile no and password from database to authenticate login'''
            if (received_data[0][1] == received_mobileNo and received_data[0][5] == received_password and received_mobileNo != 0 and received_password != 0):
                return render(request, 'Profile.html')

            else:
                return render(request, 'LogIn.html')
        except:
            return render(request, 'LogIn.html')


@csrf_exempt
def uploadProfile(request):

    '''Profile data'''
    id = request.POST.get('id1')
    mo_no = request.POST.get('mobileNo')
    dob = request.POST.get('dob')
    email = request.POST.get('email')
    name = request.POST.get('name')
    status = request.POST.get('status')
    img = request.POST.get('img')
    created_date = date.today()

    if (status is 'Y' or status is 'y'):
        status = True
    elif(status is 'N' or status is 'n'):
        status = False

    try:
        '''Inserting Profile data into database table 2'''
        param1 = ("INSERT IGNORE INTO table_2(id, cust_name, DOB, email, mobile_no, status,created_date, img) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)")
        param2 = (id, name, dob, email, mo_no, status, created_date, img)

        cur.execute(param1, param2)
        conn.commit()

        return HttpResponse('Your Profile is created Succesfully')

    except:
        return render(request, 'Profile.html')


@csrf_exempt
def complete(request):
    return HttpResponse('Profile Uploaded Succesfully')