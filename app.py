from flask import Flask
from blueprints.articles.article import article_bp
from blueprints.comments.comment import comment_bp

app = Flask(__name__)
app.register_blueprint(article_bp)
app.register_blueprint(comment_bp)


if __name__ == "__main__":
    app.run()
