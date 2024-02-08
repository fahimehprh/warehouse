from app.db.sqla import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    product = db.relationship("ProductArticle", backref=db.backref('article'))

    def __repr__(self):
        return f'<Article {self.name}>'


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    articles = db.relationship("ProductArticle", backref=db.backref('product'))


class ProductArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey(Article.id), nullable=False)
    amount_of = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(Product.id), nullable=False)

    def __repr__(self):
        return f'<ProductArticle {self.product.name} - {self.art_id}>'


def add_instance(instance):
    db.session.add(instance)
    db.session.commit()
