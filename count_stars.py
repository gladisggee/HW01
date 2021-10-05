import requests

firstpage = "https://api.github.com/users/emaadmanzoor/repos?page=1&per_page=100"

data_json1 = requests.get(firstpage)

separated_data1 = data_json1.json()


secondpage = "https://api.github.com/users/emaadmanzoor/repos?page=2&per_page=100"

data_json2 = requests.get(secondpage)

separated_data2 = data_json2.json()

#-----------------------------------------------------------------

sum1 = 0

for i in separated_data1:

    sum1 = sum1 + i["stargazers_count"]


sum2 = 0

for i in separated_data2:


    sum2 = sum2 + i["stargazers_count"]
#----------------------------------------------------------------
print(sum1+sum2)
