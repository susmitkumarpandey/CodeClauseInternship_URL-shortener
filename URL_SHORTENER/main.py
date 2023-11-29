import requests

url = input("Enter the URL to shorten:")

response = requests.get('http://tinyurl.com/api-create.php?url='+url).text


if response == "Error":
    print("Enter a valid URL.")
else:
    print(f"Your shortened URL is:{response}")
