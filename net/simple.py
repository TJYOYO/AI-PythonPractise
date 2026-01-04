import requests
import json


def main():
    try:
        resp = requests.get('https://www.tianapi.com/article/195/guonei/?key=APIKey&num=10')
        print(f"status_code =  {resp.status_code}")
        print(f"Response content type: {resp.headers.get('content-type')}")
        print(f"First 100 chars of response: {resp.text[:100]}")
        
        # 检查响应是否是JSON
        if 'application/json' in resp.headers.get('content-type', ''):
            data_model = json.loads(resp.text)
            for news in data_model['newslist']:
                print(news['title'])
        else:
            print("Error: API returned non-JSON response")
            print("This usually means the API key is invalid")
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        print("Response text:", resp.text[:200])
    except Exception as e:
        print(f"Other error: {e}")


if __name__ == '__main__':
    main()