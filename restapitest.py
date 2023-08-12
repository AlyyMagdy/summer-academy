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

def add_user(name,job):
    url = "https://reqres.in/api/users"
    payload = {
        "name": name,
        "job": job
    }

    response = requests.post(url,json=payload)
    if response.status_code == 201:
        user_data = response.json()
        return user_data
    else:
        print("Unexpected status code:", response.status_code)
        return None


    
def register_user():
    url = "https://reqres.in/api/register"
    payload ={
        "email" : "anymail@gmail.com",
        "password" : "anyy" 
    }

    # Complete the code...