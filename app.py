import app

from src.flask import Flask
from src.flask import render_template

#app = Flask(__name__)
app = Flask(
    'service_using_custom_flask',
    #static_url_path="static",
    static_folder="web_resource",
    #template_folder=r"web_resource/views")
    template_folder="views")

@app.route("/")
def hello():
    #return "<h1>Hello World!</h1>"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True, debug=True)
