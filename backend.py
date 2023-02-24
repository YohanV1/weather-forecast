import requests
API_KEY = "41074c86570fa5cfaf725e3de7d17858"


def get_data(place, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list'][:days*8]
    return filtered_data
    lst1 = [data['list'][i]['main']['temp'] for i in range(days*8)]
    lst1 = [data['list'][i]['weather'][0]['main'] for i in range(days*8)]

    print(lst1)


if __name__ == '__main__':
    get_data("Chennai", 3)

