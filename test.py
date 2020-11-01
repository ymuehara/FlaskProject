import requests


BASE = "http://127.0.0.1:5000/"

# data = [{"likes": 53, "name": "Yuri", "views": 1345},
#         {"likes": 12, "name": "Pancake with blueberries", "views": 567},
#         {"likes": 34, "name": "Maple likes cake", "views": 8753}
#         ]
#
# for i in range(len(data)):
#     response = requests.put(f"{BASE}video/{i}", data[i])
#     print(response.json())

response = requests.patch(f"{BASE}video/2", {"views": 99})
print(response.json())