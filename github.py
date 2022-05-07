import requests

url = "https://api.github.com/repos/Hashicorp/consul/commits?page=1&per_page=100&since=2013-11-04&until=2021-08-16"
# url = "https://api.github.com/XXXX?simple=yes&per_page=100&page=1"
res=requests.get(url,headers={"Authorization": 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})
repos=res.json()
while 'next' in res.links.keys():
  res=requests.get(res.links['next']['url'],headers={"Authorization": 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})  
  repos.extend(res.json())