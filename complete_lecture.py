import requests
from dict_json import open_file
from utils import print_sleep
from get_course_info import get_course_info
'''
await fetch("https://siigosas.udemy.com/api-2.0/users/me/subscribed-courses/1602900/completed-lectures/", {
    "credentials": "include",
    "headers": {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/json;charset=utf-8",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-origin",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache"
    },
    "referrer": "https://siigosas.udemy.com/course/learn-kubernetes/learn/lecture/9723216",
    "body": "{\"lecture_id\":22030420,\"downloaded\":false}",
    "method": "POST",
    "mode": "cors"
});'''
'''
POST /api-2.0/users/me/subscribed-courses/2622934/completed-lectures/ HTTP/2
Host: siigosas.udemy.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://siigosas.udemy.com/course/istio-hands-on-for-kubernetes/learn/lecture/23922450?isDefaultPlaying=
Content-Type: application/json;charset=utf-8
X-Requested-With: XMLHttpRequest
Content-Length: 42
Origin: https://siigosas.udemy.com
Connection: keep-alive
Cookie: __udmy_2_v57r=5a803c0a95ca4118a10f8bae10310137; __udmy_1_a12z_c24t=VGhlIGFuc3dlciB0byBsaWZlLCB0aGUgdW5pdmVyc2UsIGFuZCBldmVyeXRoaW5nIGlzIDQy; OptanonConsent=isIABGlobal=false&datestamp=Tue+Nov+01+2022+21%3A42%3A03+GMT-0500+(Colombia+Standard+Time)&version=202209.2.0&hosts=&consentId=5bdfaf9f-884c-4d81-914d-f3d3c76990e9&interactionCount=1&landingPath=NotLandingPage&groups=C0003%3A1%2CC0001%3A1%2CC0002%3A1&AwaitingReconsent=false; _ga=GA1.1.455412168.1644880951; _ga_7YMFEFLR6Q=GS1.1.1667247431.100.0.1667247431.60.0.0; __ssid=a457120ca73b782394e7df610b2ad98; csrftoken=dofiLttYZF7lK0xK7oTF5RekheM4v53QuVHJbbXa3XEvPHMye7SZaBA0dWNsiKRZ; ud_firstvisit=2022-02-14T23:25:07.358606+00:00:1nJkiR:7hC-UFaBRG-vSt_iauHO6gppoVs; ud_rule_vars=eJxljt1qwzAMRl8l-HZLkGQ7P36WgFFdZTNLMbWd3pS--wzrYKO34jvn6K4q5w-pcva3WGJN2VmeQQfgxQY2iDMjbPOJBUEjoJ5cSOkrinKduq9qi7nUH9afucra7qsiIOqBejQdaUfWwTRoizPMbwAOYFXvbbVzQ2s6wqevmbctBl_SkYP4G-fIp_1pkwvH_Q-S5XpIeekhtmQH5Mzi7DjAuJAxL73QCkWeH9d4-WeAXmNH4HBqkmEkvSD-Gh7q8Q2dyli3:1oq3pE:n6u8vopMgCKRzg-zkWcJjtqZ_JE; _ga=GA1.3.455412168.1644880951; _ga_E5H32MGF72=GS1.1.1644881266.1.0.1644881266.0; __zlcmid=18Xkhu9dYyHB8J3; ufb_acc="3@1Cn5EMld5BAnPz_6842ooBRlFMEL2-H8yCjeRI_y_oGyX-wtXzRDWToSQFopwZB5"; ud_last_auth_information="{\"backend\": \"udemy-auth\"\054 \"suggested_user_email\": \"santiago.ramirez@siigo.com\"\054 \"suggested_user_name\": \"Santiago Andr\\u00e9s Ram\\u00edrez\"\054 \"suggested_user_avatar\": \"https://img-c.udemycdn.com/user/50x50/anonymous_3.png\"}:1onLVW:c65XnBc2IYWF_-gRpkfuY1MVDBQ"; EUCookieMessageShown=true; muxData=mux_viewer_id=b949ed56-9b95-4c3f-b684-faf0ca1794a6&msn=0.3646599849251422&sid=edc131b9-0f73-4499-a9d4-7a9ae60f1072&sst=1667356925696&sex=1667358897971; G_ENABLED_IDPS=google; IR_PI=bd1bbe9c-f5cf-11ec-92f5-7bd9764ceda0%7C1656426708829; evi="3@F6rOaCXh91khUqhi3DSP3XX0-GoHQKRpfDkWLVyNJ4G7TRGt2MW_yWhbprDh4KWYGPviRa76S7LypZ0VGnPcF1JjZb-dk-8XTjVItOmld7956er2uQuoGjLNGzeMiU0v0uoAK2ihDCJbeg=="; ud_user_jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTg1NzEyOTc2LCJlbWFpbCI6InNhbnRpYWdvLnJhbWlyZXpAc2lpZ28uY29tIiwiaXNfc3VwZXJ1c2VyIjpmYWxzZSwiZ3JvdXBfaWRzIjpbXX0.BiF82onkE80WRdzFHJL1acY5vuX3cE88FQUOumdaC_E; ud_credit_last_seen=None; client_id=bd2565cb7b0c313f5e9bae44961e8db2; access_token=GPdTIMBTdoTNsQLR2D2rlKkNiMhBVX7ZxkHgV4YX; dj_session_id=3qvy591dxec2fiv2yai6szm3okcd9hsh; intercom-session-sehj53dd=RXZlcTFadzR4MHA5ckw4eWg5RHRtSURJRUVWUnlrekpGbVMzL2NFY2FXMVNvbTNyeWxyRWtsaTd3YlNEalIzMC0tbThyWDFRZnRtYlBOU1VQOGVQNTJjQT09--e0c9709bc3dc40178bbd3286b90dfd738a8262c2; mute=1; sidebar_content_3381074=none; dashboard_tab_3381074=reviews; caption=en; sidebar_content_2438804=transcript; _gac_UA-12366301-1=1.1667247429.CjwKCAjw5P2aBhAlEiwAAdY7dKjG6KZYmxfBVF_G_1FWnpgZhSA_88mdRqsTbLC0cXlXkIDd_i9pMRoCzkwQAvD_BwE; sidebar_content_2676278=default; __cfruid=cbb33fd8738137c7e3dd436e828ff2f22beb61ac-1667247426; _pxhd=EVGTHVBWB1DYqEFMNTur7YuF7bACaNC1OQG1L2Di0O6rzLfnKSMi8rhuFwLVSNLbiq8dBZvoYu1hF9CmbmBRAw==:6sFbqXQTsKHKdvNW/riIo8tJ8G6E3XFJARcSGatGSJEW9JmBsR2RkxzDw0zxo4PPwhtOfhfflv/vpNzStbVipFhj/Gsaj53hEtzmD/NEzts=; hlsJsStartLevel=4; ud_credit_unseen=0; __udmy_4_a12z=fa9b4b1091a9202300654e32c435c3719c479d256e7da4bfea7a0a0fb5b8de6e; seen=1; __cf_bm=MBfo_JVNV8dG2PrnEE4BjqXPOwWlE0xwl3cAfBRmyp4-1667356902-0-AWysObgslIVCF5oDdxfXQ28+5eAoJ3r+pQYVpjqX3Sa6w/x2n3tqZHXdYhqQbkroF/SSwvk6lsLsNUTHJns02KpeLzascPJGsNwob2uObjx8WHRF3VZB8zmYXL6kIfbtMyNZ+w9h2yqIbJ9gv7exN1bBTZaLKY8IVwKae1cXadMf; ud_cache_brand=102316COen_US; ud_cache_marketplace_country=CO; ud_cache_price_country=CO; ud_cache_release=5471189c22ad47b5ece3; ud_cache_user=185712976; ud_cache_version=1; ud_cache_language=en; ud_cache_device=None; ud_cache_logged_in=1; eventing_session_id=bGxc81gOSMy6vlLX42dIjw-1667359172781
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Pragma: no-cache
Cache-Control: no-cache
TE: trailers

'''
def complete_lecture(course_id,lecture_id):
    url=f"https://siigosas.udemy.com/api-2.0/users/me/subscribed-courses/{course_id}/completed-lectures/"

    headers=open_file("./headers.json")

    body={
        "downloaded": False,
        "lecture_id": lecture_id
    }
    response = requests.post(url,headers=headers,json=body)
    
    print(response.text)
    print(response)
    if not(300>response.status_code>=200):
        exit(1)
        
def complete_course(course_id):
    # course_id=1602900
    lectures = get_course_info(course_id)['results']
    # print(lectures)
    # lectures = open_file("./course.json")['results']
    for lecture in lectures:
        if lecture['_class'] == 'lecture':
            print(lecture['title'])
            print(f"continue to complete {lecture['id']}")
            complete_lecture(course_id,lecture['id'])
            print_sleep(15)
            print(f"success")
# complete_lecture(3884486,25220028)
complete_course(2622934)