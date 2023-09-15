import requests

# make an API call and store the response
url ="https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {"Accept":"application/vnd.github.v3+json"}

r = requests.get(url, headers=headers)
print(f"status code: {r.status_code}")


# store API response in a variable
response_dict = r.json()
print(f"{response_dict.keys()}")

repository_info = response_dict["items"]

number = 0
for repository in repository_info:
    number += 1
    print(f"Project {number}: {repository['name']}")
    print(f"{repository['description']}")
    print("**********************")

