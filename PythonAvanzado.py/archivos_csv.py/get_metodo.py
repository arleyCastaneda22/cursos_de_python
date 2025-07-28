import requests as r

response = r.get("https://api.github.com")


print(response.json()["current_user_url"])

