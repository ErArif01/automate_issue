import requests

# GitHub repository information

owner="ER MOHD ARIF"
repo="automate_issue"
url= f"https://api.github.com/automate_issue/ER MOHF ARIF/automate_issue/ issues"

token="github_path_11BBX5I7Q03k6dqALCpUoq_03csZ329rd13D3LKrOWKbQ"

Issue_date= {
  "title" : "New Issue",
  "body": "This is the content of the new issue."
}

headers = {
  "Authorizatoin": f"Bearer { PERSONAL_ACCESS_TOKEN"},
"Accept" : :application/vnd.github.v3+json",
}

response= requests.post(url, json=issue_data,headers=headers)
if response.status_code==201:
  print("Issue created successfully.")
else:
  print(f"Failed to create issue. Status code: {response.status_code}")
  print(response.json())
