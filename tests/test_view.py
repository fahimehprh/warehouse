def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert len(response.json) == 2
    assert response.content_type == "application/json"


def test_sell_product(client):
    response = client.get('/sell/1')
    assert response.status_code == 200
    assert response.json == {"status": "success"}
    assert response.content_type == "application/json"


def test_sell_product_not_found(client):
    response = client.get('/sell/3')
    assert response.status_code == 404
    assert response.json["code"] == 404
    assert response.json["name"] == "Not Found"
    assert response.content_type == "application/json"


def test_sell_product_sold_out(client):
    client.get('/sell/2')
    response = client.get('/sell/2')
    assert response.status_code == 404
    assert response.json["code"] == 404
    assert response.json["name"] == "Not Found"
    assert response.content_type == "application/json"
