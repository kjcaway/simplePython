from flask import Flask, render_template


app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
  return render_template('404.html') ,404


from .views import home
from .views import auth
from .views import member

app.register_blueprint(home.blueprint, url_prefix='/')
app.register_blueprint(auth.blueprint, url_prefix='/auth')
app.register_blueprint(member.blueprint, url_prefix='/member')





