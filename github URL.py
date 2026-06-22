import requests

username = input("Enter a github username: ")
response = requests.get(f"https://api.github.com/users/{username}") 

if response.status_code == 200:
    data = response.json()
    print("Name: " + str(data.get("name")))
    print("Public Repos: " + str(data.get("public_repos")))
    print("Followers: " + str(data.get("followers")))
elif response.status_code == 404:
    print("User not found!")
else:
    print("Something went wrong!")