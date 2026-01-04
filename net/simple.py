import requests
import json


def main():
    resp = requests.get('https://www.tianapi.com/article/195/guonei/?key=APIKey&num=10')
    print(f"status_code =  {resp.status_code}")
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main()