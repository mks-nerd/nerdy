from web import app

from web.base import base

app.register_blueprint(base, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)