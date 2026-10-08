import json

from playwright.sync_api import APIRequestContext, expect


API_ENDPOINT = "https://fakestoreapi.com/products/1"


def test_get_product_details(playwright) -> None:
    request: APIRequestContext = playwright.request.new_context()
    try:
        response = request.get(API_ENDPOINT)

        expect(response).to_be_ok()
        assert response.status == 200

        body = response.json()
        print(json.dumps(body, indent=2))

        required_keys = {"id", "title", "price", "category", "description"}
        assert required_keys.issubset(body)
        assert body["id"] == 1
        assert body["price"] == 109.95
        assert body["category"] == "men's clothing"
    finally:
        request.dispose()
