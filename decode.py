import urllib.request
import json

FOLDER_ID = "b1gjigdhd7pe26110eqg" # Идентификатор каталога
# curl -d "{\"yandexPassportOauthToken\":\"AgAAAAAqxiAZAATuwQ_be5qiR0d3lZ0n6irZf78\"}" "https://iam.api.cloud.yandex.net/iam/v1/tokens"
IAM_TOKEN = "t1.9euelZrOmoyeyMmUyJ7Pj5ycmIyTze3rnpWamJGJi4uZmZ6Yxp7Hi5CUyIvl9PdLLnd--e9vPV-13fT3C110fvnvbz1ftQ.BovLq7q9F7" \
            "uz0aNMpOeZwq4SR3UrwOO6phy30ylrJ6ZwzbbNldrKcC8PY-vN2aTrplk0qzQ14Nk8GNw-uJodCA" # IAM-токен

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
        return 'формат файла не подходит(длина больше 30 секунд)'

