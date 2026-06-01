# import json
#
# import httpx
#
#
# login_payload = {
#   "email": "valera_old@mail.ru",
#   "password": "12345D"
# }
#
# login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json = login_payload)
#
# login_response_data = login_response.json()
#
# print("Login response: ", login_response_data)
# print("Status code: ", login_response.status_code)
#
# me_payload = {
#     "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
#
# }
#
# # print(me_payload)
#
# response_me = httpx.get("http://localhost:8000/api/v1/users/me",headers=me_payload)
# print(response_me.status_code)
# print(response_me)
#
#
# # refresh_payload = {
# #     "refreshToken": login_response_data["token"]["refreshToken"],
# #
# # }
# # refresh_response=httpx.post("http://localhost:8000/api/v1/authentication/refresh", json = refresh_payload)
# # refresh_response_data = refresh_response.json()
# #
# # print("Refresh response: ", refresh_response_data)
# # print("Status code: ", refresh_response.status_code)