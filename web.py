from flask import Flask, render_template
from website.routes.image import image_bp
from website.routes.api import api_bp
import sys

host = False

if host:
    import socket

app = Flask(__name__,
            template_folder='website/templates',
            static_folder='website/static')
app.register_blueprint(image_bp)
app.register_blueprint(api_bp)

app.config['SECRET_KEY'] = 'secret!'
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # This likely isn't a smart practice but it works ;D
    if 'socket' in sys.modules:
        app.run()
    else:
        app.run(socket.gethostbyname(socket.gethostname()))