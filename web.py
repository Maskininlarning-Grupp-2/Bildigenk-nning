from flask import Flask, render_template
from website.routes.image import image_bp
from website.routes.api import api_bp


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
    app.run()