import requests
import datetime
import time
import pytz

age = str(input("enter the age 18 or 45: "))
dose = str(input("enter the dose and 1 or 2: "))
pincode = str(input("enter your pincode : "))


# checking the age, dose and pincode
if int(age) == 18 or int(age) == 45:
    print("age =", age)
else:
    print("enter the correct age")
    exit()
if int(dose) == 1 or int(dose) == 2:
    print("dose =", dose)
else:
    print("enter the correct dose")
    exit()
if int(pincode) > 100000 and int(dose) < 999999:
    print("pincode=", pincode)
else:
    print("enter the correct pincode")
    exit()


timeZ_Kl = pytz.timezone('Asia/Kolkata')  # to get indian time
# storing everything into full date like ex: 20-05-2021
fulldate = datetime.datetime.now(timeZ_Kl).strftime("%d-%m-%Y")


def getrequest(url):  # to fetch the data from vacine url
    try:
        res = requests.get(url=url)
        if res.status_code != 200:
            return False
        else:
            return res.json()
    except:
        return False

# send mail if it finds any new vacine center at that pincode


def sendemail():
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
        try:
            get_age = i.get("min_age_limit")
            get_dose = i.get("available_capacity_dose"+dose)
            if get_age == int(age) and int(get_dose) > 0:
                # count = count + 1
                return True
        except:
            print("error on finding check age or availability of dose")
            return False
    return False


cowin_url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=' + \
    pincode+'&date='+fulldate

temp = {}  # temp variale to store and comapre the request from cowin api

while True:
    getdata = getrequest(cowin_url)
    if getdata != False:
        if temp == {} and getdata["sessions"] != [] and checkAgeandDose(getdata["sessions"], age, dose):
            temp = getdata
            sendemail()
        else:
            if temp != getdata and getdata["sessions"] != [] and checkAgeandDose(getdata["sessions"], age, dose):
                temp = getdata
                sendemail()
    print("updated!. again check in 15 min")

    time.sleep(900)  # 900 sec means 15 minutes
