import json
import os

from app.db.models import Article, Product, ProductArticle, add_instance
from app.db.sqla import db


def create_article_instance(inventory_json):
    for item in inventory_json["inventory"]:
        article_instance = Article(id=int(item["art_id"]), name=item["name"], stock=int(item["stock"]))
        add_instance(article_instance)


def create_product_instance(product_json):
    for product in product_json["products"]:
        product_instance = Product(name=product["name"])
        add_instance(product_instance)
        for article in product["contain_articles"]:
            article_instance = ProductArticle(
                product=product_instance,
                article_id=int(article["art_id"]),
                amount_of=int(article["amount_of"])
            )
            add_instance(article_instance)


def create_instances_from_json():
    with open(os.path.abspath('db_samples/inventory.json')) as f:
        inventory_data = json.load(f)
        create_article_instance(inventory_data)

    with open(os.path.abspath("db_samples/products.json")) as f:
        product_data = json.load(f)
        create_product_instance(product_data)


def create_models():
    db.drop_all()
    db.create_all()
    create_instances_from_json()
