'''
I have used Fast2SMS website to send otp sms. This code is available on their
official website devolopement api section. Code Is simple and Self explanatory
'''
import requests

def sendOtp(otp, mobile_no):

    url = "https://www.fast2sms.com/dev/bulkV2"

    payload = f"variables_values={otp}&route=otp&numbers={mobile_no}"
    headers = {
        'authorization': "498NPSIKx5BEZvyRAUGmHz32dJWCkFwbD67jgnel10QTXVphofOGMn2xJAbN7TC3E8rXIiPsUg45wpzY",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)


