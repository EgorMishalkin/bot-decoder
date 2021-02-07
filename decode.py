import urllib.request
import json

FOLDER_ID = "b1g202m0ik2cgsdk4h8e" # Идентификатор каталога
IAM_TOKEN = "t1.9euelZqbzo-VzpnLzsfMlpeVjJCQmO3rnpWayM-cisiVmcmYyM6UlYmbkpvl8_dJa39--e9HBV9u_t3z9wkafX7570cFX27-.ZbhA" \
            "DyDIGQJOdlyOMwrHdrn3FgF1yRoYlM1KJ3oop309tbL1gPr8TghyrezeJQlcYqEZtxhgfdu1tvOte7XTDA" # IAM-токен

with open("speech.ogg", "rb") as f:
    data = f.read()

params = "&".join([
    "topic=general",
    "folderId=%s" % FOLDER_ID,
    "lang=ru-RU"
])

url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?%s" % params, data=data)
url.add_header("Authorization", "Bearer %s" % IAM_TOKEN)

responseData = urllib.request.urlopen(url).read().decode('UTF-8')
decodedData = json.loads(responseData)

if decodedData.get("error_code") is None:
    print(decodedData.get("result"))
