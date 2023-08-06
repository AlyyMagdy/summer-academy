import requests


def get_single_user_email(num):
    api_url = f"https://reqres.in/api/users/{num}"


    response = requests.get(api_url)
    if response.status_code == 200:
        joke_data = response.json()
        joke = joke_data['data']
        print(joke["email"])
        return joke["email"]
    else:
        print("Unexpected status code:", response.status_code)
        return None
