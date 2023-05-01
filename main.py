import requests

url = "https://connect.soligent.net/api/items"

querystring = {"language":"en","currency":"USD","c":"3510556","offset":"0","sitepath":"/sca/searchApi.ssp","sort":"custitem_ns_sc_ext_ts_90_amount:desc","use_pcv":"F","fieldset":"search","n":"2","include":"facets","limit":"100","country":"US","pricelevel":"4"}

payload = ""
headers = {
    "cookie": "NLShopperId2=_hLrdW4VA2FxSWc_; NLVisitorId=UZwMgW4VA2JxSe9n; NS_VER=2023.1; JSESSIONID=LJP8QsG021ZSXl-WlsMsgDXgBSgZHFJyNVEgHlR05ddj8uGSa79_yjdOXkB9u86PZ3sUeANxlhxw_SWm5242yuV4AneSHr_H6_-YHQwm6Hld2Koj-HHOBf0G8_dKqmj9\u0021154194789; chrole=1125:306749:2dd353aa; jsid_own=3510556.-83967632; SSPOperationId_ba51ba3a=05a1be0e-9ef2-4d9e-a814-5c739fd0c85a; SSPOperationId_2ec15251=890cd3ca-a0d7-4212-a099-887e978a4deb; SSPOperationId_6208967a=3d516026-14a1-46d1-909e-f78fb9e90333; recentlyViewedIds=[60596%2C65939]; SSPOperationId_6480fef=9a614971-3e7a-45a3-94e9-6d4123506b50",
    "authority": "connect.soligent.net",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "dnt": "1",
    "pragma": "no-cache",
    "referer": "https://connect.soligent.net/search",
    "sec-ch-ua-mobile": "?0",

    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "x-sc-touchpoint": "shopping"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)