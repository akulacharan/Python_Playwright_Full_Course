import base64

import pytest
from playwright.sync_api import Playwright

# 1) Basic Authentication 1
# url: https://httpbin.org/basic-auth/user/pass
# username: user
# password : pass
# def test_basic_auth(playwright: Playwright):
#     request_context = playwright.request.new_context()
#
#     credentials = base64.b64encode(b"user:pass").decode("utf-8")
#
#     response = request_context.get("https://httpbin.org/basic-auth/user/pass",
#                                    headers={"Authorization": f"Basic {credentials}"}
#                                    )
#     assert response.status == 200
#     response_body = response.json()
#     print("Response body:", response_body)
#
#     request_context.dispose()



# 2) Basic Authentication 2
# url: http://the-internet.herokuapp.com/basic_auth
# username: admin
# password : admin
# def test_basic_auth(playwright: Playwright):
#     request_context = playwright.request.new_context()
#
#     credentials = base64.b64encode(b"admin:admin").decode("utf-8")
#
#     response = request_context.get("http://the-internet.herokuapp.com/basic_auth",
#                                    headers={"Authorization": f"Basic {credentials}"}
#                                    )
#     assert response.status == 200
#     response_body = response.text()
#     print("Response body:", response_body)
#
#     request_context.dispose()


# 3) Bearer Token Authentication
# url: https://api.github.com/user/repos

# def test_bearer_token_auth_github_repos(playwright: Playwright):
#     request_context = playwright.request.new_context()
#     response = request_context.get("https://api.github.com/user/repos",
#                                        headers={"Authorization": f"Bearer {token}"}
#                                        )
#     assert response.status==200
#     response_body=response.json()
#
#     print("Response Body(Repositories....)",response_body)


# 4) Bearer Token Authentication
# url: https://api.github.com/user

# def test_bearer_token_auth_github_repos(playwright: Playwright):
#     request_context = playwright.request.new_context()
#     response = request_context.get("https://api.github.com/user",
#                                        headers={"Authorization": f"Bearer {token}"}
#                                        )
#     assert response.status==200
#     response_body=response.json()
#
#     print("Response Body(User details.....)",response_body)


#5) API Key Authentication - OpenWeatherMap
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

# def test_api_key_auth_openweather(playwright: Playwright):
#
#     request_context = playwright.request.new_context()
#
#     query_params = {
#         "q": "Delhi",
#         "appid": "fe9c5cddb7e01d747b4611c3fc9eaf2c"
#
#     }
#     response = request_context.get("https://api.openweathermap.org/data/2.5/weather",
#                                    params=query_params
#                                        )
#     assert response.status==200
#     response_body=response.json()
#
#     print("weather info:====>",response_body)


#6) API Key Authentication - weatherAPI
# URL: https://api.weatherapi.com/v1/current.json

# def test_api_key_auth_weatherapi(playwright: Playwright):
#
#     request_context = playwright.request.new_context()
#
#     query_params = {
#         "q": "Chennai",
#         "key": "59f38ebe55d5436ca0552856250606"
#
#     }
#     response = request_context.get("https://api.weatherapi.com/v1/current.json",
#                                    params=query_params
#                                        )
#     assert response.status==200
#     response_body=response.json()
#
#     print("weather info:====>",response_body)


# 7) OAuth2 Authentication

# 1) From the application get the following. (Manual process)
# https://imgur.com/
#     1) Client ID
#     2) Client Secrete
#
# 2) Send Post request for getting token
# POST https://api.imgur.com/oauth2/token
# 	ClientID
# 	Client secrete
# 	tokenURL
# 	Redirect URL
# 	Grant type
# 	Authorization code
#
# you will get token once POST request is succesfull.
#
# 3) Use Token to do API call ( Get request).


def test_verify_oauth2_authentication(playwright: Playwright):
    # Step 1: Initialize request context
    request_context = playwright.request.new_context()

    # Step 2: Define client credentials and OAuth2 parameters
    client_id = "cff93d24167b033"
    client_secret = "ac85c1a5bc7e775cfbcd5b40188a2aa3b9be68d2"
    redirect_uri = "https://www.getpostman.com/oauth2/callback"
    grant_type = "authorization_code"
    authorization_code = "4c91c2e0de4cc9fa95ddb6e3fd0df11cc29ef739"  # Replace with valid code

    # Step 3: Send POST request to get the access token
    token_response = request_context.post(
        "https://api.imgur.com/oauth2/token",
        form={
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": grant_type,
            "code": authorization_code,
            "redirect_uri": redirect_uri
        }
    )

    # Step 4: Validate token response
    assert token_response.status == 200
    token_data = token_response.json()
    access_token = token_data.get("access_token")
    print(f"\nGenerated Access Token: {access_token}")

    assert access_token is not None, "Access token not found in response!"

    # Step 5: Use access token to make authenticated GET request
    image_response = request_context.get(
        "https://api.imgur.com/3/account/me/images",
        headers={
            "Authorization": f"Bearer {access_token}"}
    )

    # Step 6: Validate image API response
    assert image_response.status == 200
    print("\nResponse JSON:", image_response.json())

    # Step 7: Cleanup
    request_context.dispose()