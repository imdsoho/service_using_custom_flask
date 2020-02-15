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
    #run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
    '''def run_simple(
            hostname,
            port,
            application,
            use_reloader=False,
            use_debugger=False,
            use_evalex=True,
            extra_files=None,
            reloader_interval=1,
            reloader_type="auto",
            threaded=False,
            processes=1,
            request_handler=None,
            static_files=None,
            passthrough_errors=False,
            ssl_context=None,
    ):'''
    #app.run(host="0.0.0.0", port="8080", debug=True, threaded=True)
    app.run(host="0.0.0.0", port="8080", threaded=True)
    #app.run(host="0.0.0.0", port="8080", threaded=False, processes=2)