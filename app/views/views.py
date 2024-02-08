from flask import Blueprint
from werkzeug.exceptions import NotFound

from app.db.models import Product
from app.db.sqla import db


view = Blueprint('view', __name__)


def get_available_products(product):
    available_articles_count = []

    for article in product.articles:
        count = article.amount_of
        available_articles = article.article.stock
        if available_articles > 0:
            available_articles_count.append(int(available_articles / count))
        else:
            available_articles_count.append(0)

    return min(available_articles_count)


@view.route('/')
def index():
    products = Product.query.all()
    response = []

    for product in products:
        available_products = get_available_products(product)

        if available_products > 0:
            response.append({
                'id': product.id,
                'name': product.name,
                'stock': available_products
            })

    return response


@view.route('/sell/<int:product_id>')
def sell_product(product_id):
    product = db.get_or_404(Product, product_id)
    if get_available_products(product) == 0:
        raise NotFound("No available products found.")

    for article in product.articles:
        count = article.amount_of
        article.article.stock = article.article.stock - count
        db.session.commit()

    return {"status": "success"}
