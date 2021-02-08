import urllib.request
import json

FOLDER_ID = "b1gjigdhd7pe26110eqg" # Идентификатор каталога
IAM_TOKEN = "t1.9euelZqNj5yViZacmJfLnJOUjZOYne3rnpWamJGJi4uZmZ6Yxp7Hi5CUyIvl8_cODnt--e9Hbip6_N3z9048eH7570duKnr8.VQDty2" \
            "Ypb1oQ96MwrDkmwq-Czs9FMgqadvJEL9DLuNveaGlKT2MJcq-haceEGqdXRTsdNhq1T5Ub8r2VwDZvBg" # IAM-токен

params = "&".join([
    "topic=general",
    "folderId=%s" % FOLDER_ID,
    "lang=ru-RU"
])


def decode(filename):

    with open(filename, "rb") as f:
        data = f.read()

    url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?%s" % params, data=data)
    url.add_header("Authorization", "Bearer %s" % IAM_TOKEN)

    responseData = urllib.request.urlopen(url).read().decode('UTF-8')
    decodedData = json.loads(responseData)

    if decodedData.get("error_code") is None:
        result = decodedData.get("result")
        return result
    else:
        return 'Error'

