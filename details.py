import requests

url = "https://connect.soligent.net/api/items"

querystring = {"language":"en","currency":"USD","c":"3510556","include":"facets","sitepath":"/sca/searchApi.ssp","country":"US","use_pcv":"F","fieldset":"details","pricelevel":"4","n":"2","url":"Sunergy-VSUN370-120BMH-370W-Black-on-Black-120-Half-Cell-Mono-Solar-Panel"}

payload = ""
headers = {
    "cookie": "NLShopperId2=_hLrdW4VA2FxSWc_; NLVisitorId=UZwMgW4VA2JxSe9n; NS_VER=2023.1; chrole=1125:306749:2dd353aa; recentlyViewedIds=[60596%2C65939]; JSESSIONID=W-gaTE7cGe5l7oM1QqlB9ph0_mAevUFOMXSCDYXA4NfDrsVTzedCkCaLhUrdbLNLECVSTe7CYMqcg1CuSNgf7uNpqyvIMMfY1_5RZFcLFWY8khX_3pl7mZEI_tk0JCGt\u0021154194789; jsid_own=3510556.2131778827; SSPOperationId_bf2c67e8=75cf1b32-6943-406d-b427-3517bbef3ff5; SSPOperationId_6480fef=444c2de9-458d-47db-83aa-6c1b09d83730",
    "authority": "connect.soligent.net",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "en-US,en;q=0.8",
    "cache-control": "no-cache",
    "dnt": "1",
    "pragma": "no-cache",
    "referer": "https://connect.soligent.net/Sunergy-VSUN370-120BMH-370W-Black-on-Black-120-Half-Cell-Mono-Solar-Panel",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "x-sc-touchpoint": "shopping"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)