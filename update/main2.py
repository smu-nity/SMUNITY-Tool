import requests


cookies = {
    'WMONID': '52mcwiNmRf3',
    '_ga_5BEDF8DSQJ': 'GS1.1.1697453111.1.0.1697453111.0.0.0',
    '_ga_61DCRX9WGH': 'GS1.1.1697453101.1.1.1697453230.0.0.0',
    '_ga_G9YNZX5B4C': 'GS1.1.1697453010.1.0.1697453231.0.0.0',
    '_ga': 'GA1.3.484988329.1697453010',
    'mc_appid': 'usrCPsnlInfoUpd-STD',
    '_ga_K641YX4P55': 'GS1.1.1697456256.2.0.1697456256.0.0.0',
    'SMJSESSIONID': 'ihUvKMBeNmMPDLddCrdB8j6JdmuEBEbrwX6mFweUYnRE1jjUnd74VOyBwMTRd9mh.amV1c19kb21haW4vc211LXdlYjE='
}

data = {
    '_AUTH_MENU_KEY': 'usrCPsnlInfoUpd-STD',
    '@d1#strStdNo': '201911019',
    '@d#': '@d1#',
    '@d1#': 'dmParam',
    '@d1#tp': 'dm'
}


url = 'https://smul.smu.ac.kr/Login/ssoLogin.do'
res = requests.get(url=url, cookies=cookies)
print(str(res))
SMJSESSIONID = res.cookies.get('SMJSESSIONID')
print(SMJSESSIONID)

url = 'https://smul.smu.ac.kr/UsrRecMatt/list.do'
cookies['SMJSESSIONID'] = SMJSESSIONID
cookies['_gid'] = 'GA1.3.1095688725.1697453010'
res = requests.post(url=url, cookies=cookies, data=data)
print(str(res))
print(res.text)