from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
  return render_template('404.html') ,404


from .views import home

app.register_blueprint(home.blueprint, url_prefix='/')





