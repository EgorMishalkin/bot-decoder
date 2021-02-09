import urllib.request
import json

FOLDER_ID = "b1gjigdhd7pe26110eqg" # Идентификатор каталога
# curl -d "{\"yandexPassportOauthToken\":\"AgAAAAAqxiAZAATuwQ_be5qiR0d3lZ0n6irZf78\"}" "https://iam.api.cloud.yandex.net/iam/v1/tokens"
IAM_TOKEN = "t1.9euelZqPm4nJlsaRmZaNk5PLzM7Gzu3rnpWamJGJi4uZmZ6Yxp7Hi5CUyIvl9Pc-RHR--e9_b1L03fT3fnJxfvnvf29S9A.3zOnAa9lM" \
            "ApKmJyHvnfrsJUg-xkhsl18gF1D7gAENWdGuDO0EQBhi7UppycbHMd1dfqBkCYwd79Dfr4pmogpAw" # IAM-токен

params = "&".join([
    "topic=general",
    "folderId=%s" % FOLDER_ID,
    "lang=ru-RU"
])


def decode(filename):

    try:
        # открываем файл который задал пользователь
        with open(filename, "rb") as f:
            data = f.read()

        # передаем файл серверам яндекса
        url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?%s" % params, data=data)
        url.add_header("Authorization", "Bearer %s" % IAM_TOKEN)

        # получаем ответ
        responseData = urllib.request.urlopen(url).read().decode('UTF-8')
        decodedData = json.loads(responseData)

        # возвращаем переведенный текст
        if decodedData.get("error_code") is None:
            result = decodedData.get("result")
            return result
        # если какая-то ошибка :)
        else:
            return 'Error'
    # ошибка запроса(SpeechKit принимает запросы до 30 секунд)
    except urllib.error.HTTPError:
        return 'format error'

