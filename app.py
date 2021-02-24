from flask import *
from google_trans_new import google_translator
from werkzeug.exceptions import HTTPException

translator = google_translator()
app = Flask(__name__)


@app.errorhandler(HTTPException)
def handle_HTTPException_exception(e):
    res = e.get_response()
    res.data = json.dumps({
        'code': e.code,
        'name': e.name,
        'msg': e.description
    })
    res.content_type = 'application/json'
    return res


@app.route('/translate', methods=['POST'])
def translate():
    if request.form:
        text = request.form.get('text')
        lang = request.form.get('lang')
        if text and lang:
            return jsonify({
                'msg': 'done',
                'text': translator.translate(text, lang_tgt=lang)
            }), 200
        else:
            return jsonify({
                'msg': 'something wrong, maybe you mis text or lang key'
            }), 404


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
