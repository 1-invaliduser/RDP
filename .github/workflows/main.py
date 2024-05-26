import random
import string
import requests

running = True
def check_nitro_code(code):
    base_url = "https://discord.com/api/v8/entitlements/gift-codes/"
    url = f"{base_url}{code}"
    a=0
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Valid Nitro link: {url}")
            running = False
            a+=1
            print("total found:", a)
        else:
            running = True
            print("total found:", a)
    except requests.RequestException:
        print("Error checking Nitro code")
        print("total found:", a)

def generate_random_nitro_code():
    # Generate a random 16-character alphanumeric code
    return ''.join((random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(4, 19))))

def generate_nitro_link(code):
    base_url = "https://discord.gift/"
    return base_url + code


while running:
    random_nitro_code = generate_random_nitro_code()
    nitro_link = generate_nitro_link(random_nitro_code)
    print(nitro_link)
    check_nitro_code(nitro_link)
