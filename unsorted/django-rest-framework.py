import requests as r

def car_types():
    auth_token = '74e074c29ea39ff25761f5c43aa60396a1239628'
    car_types = r.request(method='GET', url='http://127.0.0.1:8000/api/v1/cars/car-types', headers={'authorization': f'Token {auth_token}'}).json()
    values = (list(car_types.values()))
    keys = (list(car_types.keys()))
    mixed = list(zip(keys, values))
    print(mixed)
    for i in mixed:
        print(i[0], i[1])
text1 = 'A1234567ru'
text = "Ваш текст с цифрами 123 и 456"
digits = ''.join(c for c in text1 if c.isdigit())



url = "http://127.0.0.1:8000/api/v1/telegram/media/upload/"
files = {'file': open('example.txt', 'rb')}
headers = {'Content-Disposition': 'attachment; filename="example.txt"'}
#response = r.post(url, files=files, headers=headers)





def download():
    url = 'http://127.0.0.1:8000/api/v1/telegram/media/download/62cf99ae-9a51-47c6-9682-9e788938b2c7/'
    response = r.request(url=url, method='GET')
    print(response.json())


def SaveFile(raw_data):
    raw_data = ''
    message = email.message_from_string(raw_data, policy=policy.HTTP)
    file_data = message.get_payload(0).get_payload(decode=True)
    with open('saved_example.txt', 'wb') as file:
        file.write(file_data)

download()