import requests
import re
import json
from urllib.parse import urlsplit, parse_qs

s = requests.Session() 
loginurl = "https://www.playsuisse.ch/api/sso/login?x=x&locale=de&redirectUrl=https%3A%2F%2Fwww.playsuisse.ch%2F"
r = s.get(loginurl);
x = re.search("^var SETTINGS(.*)", r.text,flags=re.MULTILINE) 
settings_str=  x.group()[len("var SETTINGS = "):-2]
settings = json.loads(settings_str)
login_endpoint = "https://login.srgssr.ch/srgssrlogin.onmicrosoft.com/B2C_1A__SignInV2/SelfAsserted?tx="+settings['transId']+"&p=B2C_1A__SignInV2";
print(login_endpoint)
r = s.post(login_endpoint,                  headers={          "X-CSRF-TOKEN": settings['csrf']  } ,
                  data={"request_type":"RESPONSE","signInName":"christian@kuendig.info","password":"@SV?:zPkQWEm}5q"}    )

loginconfirmed_url="https://login.srgssr.ch/srgssrlogin.onmicrosoft.com/B2C_1A__SignInV2/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token="+settings['csrf']+"&tx="+settings['transId']+"&p=B2C_1A__SignInV2&diags="
print(loginconfirmed_url)
r = s.get(loginconfirmed_url,allow_redirects=True)
print( r.status_code)
print(r.headers)
print(r.history[0])
print()
print(parse_qs(urlsplit(r.history[1].headers['location']).query)['id_token'])
'''
await fetch("https://login.srgssr.ch/srgssrlogin.onmicrosoft.com/B2C_1A__SignInV2/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=czJoNk5ZL0dUUUtkQ2xHcXFQMjMvV05DNERwWVdhT09STEMyaEEwSi81dTd3RGRncUFWM2dTOGVrZW9hVm10M2hGS0MxT3ovQTY2Sjk1ODVublNLVEE9PTsyMDI0LTAxLTI2VDIwOjQ3OjAzLjQ4OTI5ODRaO1ZwRzRCWUdLTEpFaGV0elVmUUpqZWc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoyfQ==&tx=StateProperties=eyJUSUQiOiJiNDJjM2I0OS02NmRjLTRhYmItOWI3MS1jNGM1ZmZiYmIzYjIifQ&p=B2C_1A__SignInV2&diags=%7B%22pageViewId%22%3A%22e54cb831-cdce-47cc-a39e-fbb8bb0874c6%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1706302023%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fsrgssrlogin.akamaized.net%2Fsrgssr-login%2Fpages%2Fplaych%2Fde%2Fsignin.html%22%2C%22acST%22%3A1706302023%2C%22acD%22%3A174%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1706302023%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1706302023%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1706302023%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1706302023%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1706302023%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1706302030%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1706302029%2C%22acD%22%3A394%7D%5D%7D", {
    "credentials": "include",
    "headers": {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Sec-GPC": "1",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1"
    },
    "referrer": "https://login.srgssr.ch/srgssrlogin.onmicrosoft.com/oauth2/v2.0/authorize?p=b2c_1a__signinv2&state=%7B%22locale%22%3A%22de%22%2C%22redirectUrl%22%3A%22https%3A%2F%2Fwww.playsuisse.ch%2F%22%2C%22policy%22%3A%22b2c_1a__signinv2%22%7D&client_id=ba121867-0b6f-498f-9d72-3940630bab46&nonce=defaultNonce&redirect_uri=https%3A%2F%2Fwww.playsuisse.ch%2Fapi%2Fsso-redirect%2Flogin&scope=openid+offline_access+https%3A%2F%2Fsrgssrlogin.onmicrosoft.com%2Fuserinfo%2Femail+https%3A%2F%2Fsrgssrlogin.onmicrosoft.com%2Fuserinfo%2Fresidency+https%3A%2F%2Fsrgssrlogin.onmicrosoft.com%2Fuserinfo%2Flanguage&response_type=code&entity_id=playch&ui_entity=playch&ui_locales=de",
    "method": "GET",
    "mode": "cors"
});

await fetch("https://login.srgssr.ch/srgssrlogin.onmicrosoft.com/B2C_1A__SignInV2/SelfAsserted?tx=StateProperties=eyJUSUQiOiJiYWRjMzJlMi03YjMyLTQ2MzYtODQ3ZS02MGRiYzMzM2U5YjgifQ&p=B2C_1A__SignInV2", {
    "credentials": "include",
    "headers": {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-CSRF-TOKEN": "TThqaVV1YnA4UEtDckVnd3B5L05oRmVFYnFVeC9qeFhoQllqanRWdmxYTjJCdm9OY3o5dk1vT1pLa0JmYTBtNk5BR3VsQ3BvZTZwaytQR1FzOERxUUE9PTsyMDI0LTAxLTI2VDIwOjI4OjQwLjczNjY0MjRaO1RITm9NUjlMWjdQUUpTc3JIaXZ2Z0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoyfQ==",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Sec-GPC": "1",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    },
    "referrer": "https://login.srgssr.ch/srgssrlogin.onmicrosoft.com/oauth2/v2.0/authorize?p=b2c_1a__signinv2&state=%7B%22locale%22%3A%22de%22%2C%22redirectUrl%22%3A%22https%3A%2F%2Fwww.playsuisse.ch%2F%22%2C%22policy%22%3A%22b2c_1a__signinv2%22%7D&client_id=ba121867-0b6f-498f-9d72-3940630bab46&nonce=defaultNonce&redirect_uri=https%3A%2F%2Fwww.playsuisse.ch%2Fapi%2Fsso-redirect%2Flogin&scope=openid+offline_access+https%3A%2F%2Fsrgssrlogin.onmicrosoft.com%2Fuserinfo%2Femail+https%3A%2F%2Fsrgssrlogin.onmicrosoft.com%2Fuserinfo%2Fresidency+https%3A%2F%2Fsrgssrlogin.onmicrosoft.com%2Fuserinfo%2Flanguage&response_type=code&entity_id=playch&ui_entity=playch&ui_locales=de",
    "body": "request_type=RESPONSE&signInName=christian%40kuendig.info&password=%40SV%3F%3AzPkQWEm%7D5q",
    "method": "POST",
    "mode": "cors"
});'''