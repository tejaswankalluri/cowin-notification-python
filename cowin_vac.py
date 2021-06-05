import requests
import datetime
import time
import pytz

age = str(input("enter the age 18 or 45: "))
dose = str(input("enter the dose and 1 or 2: "))
pincode = str(input("enter your pincode : "))

timeZ_Kl = pytz.timezone('Asia/Kolkata')  # to get indian time
# storing everything into full date like ex: 20-05-2021
fulldate = datetime.datetime.now(timeZ_Kl).strftime("%d-%m-%Y")


def getrequest(url):  # to fetch the data from url
    try:
        res = requests.get(url=url)
        return res.json()
    except:
        return res.json().error


def sendemail():  # send mail if it finds any new vacine center at that pincode
    # use url from basin from if you want to create account https://usebasin.com/
    url = ''
    data = 'new vacine available at pincode: ' + \
        pincode + ' and Date ' + \
        str(fulldate) + ' ' + \
        str(datetime.datetime.now(timeZ_Kl).strftime("%I:%M:%S %p"))
    myobj = {'vacine': data}
    x = requests.post(url, data=myobj)
    return x.status_code


def checkAgeandDose(reslist, age, dose):
    for i in reslist:
        count = 0
        try:
            get_age = i.get("min_age_limit")
            get_dose = i.get("available_capacity_dose"+dose)
            if get_age == int(age) and int(get_dose) > 0:
                count = count + 1
        except:
            print("error on finding check age or availability of dose")
    if(count > 0):
        return True
    else:
        return False


cowin_url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=' + \
    pincode+'&date='+fulldate

temp = {}  # temp variale to store and comapre the request from cowin api

while True:
    getdata = getrequest(cowin_url)
    if temp == {} and getdata["sessions"] != [] and checkAgeandDose(getdata["sessions"], age, dose):
        temp = getdata
        sendemail()
    else:
        if temp != getdata and getdata["sessions"] != [] and checkAgeandDose(getdata["sessions"], age, dose):
            temp = getdata
            sendemail()
    print("completed!. again check in 15 min")

    time.sleep(900)  # 900 sec means 15 minutes
