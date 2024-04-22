import capsolver, requests, time, os

# เอาจากหน้า dashbord 

server_id = 0 # server id from mc4
email = "" # email for mc4
password = "" # password for mc4
capsolver.api_key = "" # https://www.capsolver.com/
jar = requests.cookies.RequestsCookieJar() 

###########################

def login():
    solution = capsolver.solve({
        "type":"ReCaptchaV2TaskProxyLess",
        "websiteKey":"6Ld0O7wUAAAAAEQp_racvtgzC7zq7IUm7jtFP5XY",
        "websiteURL":"https://mc4.in/"
    })

    reqlogin = requests.post("https://mc4.in/api/login", headers={"User-Agent": solution['userAgent']}, data={
        "email": email,
        "password": password,
        "g-recaptcha-response": solution['gRecaptchaResponse']
    })

    try:
        unformat = reqlogin.headers['set-cookie']
        cookie = unformat.split(";")
        return cookie[0]
    except:
        return False

cc = login()

if cc:
    solution = capsolver.solve({
            "type":"ReCaptchaV2TaskProxyLess",
            "websiteKey":"6Ld0O7wUAAAAAEQp_racvtgzC7zq7IUm7jtFP5XY",
            "websiteURL":"https://mc4.in/"
    })

    print("(!) Login Success")

    req = requests.post("https://mc4.in/v2/mcjava/apirenewfree", headers={"Cookie": cc, "User-Agent": solution['userAgent']}, data={
        "id": server_id,
        "g-recaptcha-response": solution['gRecaptchaResponse']
    })

    if req.status_code == 200:
        print(f"(!) Renew Success : ServerIds {server_id}")
    else:
        print(f"(-) Error : ServerIds {server_id} : {req.text}")

    while True:
        solution = capsolver.solve({
            "type":"ReCaptchaV2TaskProxyLess",
            "websiteKey":"6Ld0O7wUAAAAAEQp_racvtgzC7zq7IUm7jtFP5XY",
            "websiteURL":"https://mc4.in/"
        })

        req = requests.post("https://mc4.in/v2/mcjava/apirenewfree", headers={"Cookie": cc}, data={
            "id": server_id,
            "g-recaptcha-response": solution
        })

        if req.status_code == 200:
            print(f"(!) Renew Success : ServerIds {server_id} : wait 60 min to renew Again :)")
        else:
            print(f"(-) Error : ServerIds {server_id} : {req.text}")
            os.system("pause")
        
        time.sleep(3590)
else:
    print("(-) login error program Stoped")
