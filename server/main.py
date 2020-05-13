import flask
import lib

app = flask.Flask('copy-writer-server')
texts = lib.TextStorage()


@app.route('/get_theme_list', methods=['GET'])
def get_theme_list():
    return str(texts.get_theme_list())

@app.route('/get_demos', methods=['GET'])
def get_demos():
    theme_name = flask.request.args['theme_name']
    return str(texts.get_demos(theme_name))

@app.route('/get_full_text', methods=['GET'])
def get_full_text():
    theme_name = flask.request.args['theme_name']
    id = flask.request.args['id'] 
    return str(texts.get_full_text(theme_name, id))

@app.route('/get_money_for_text', methods=['GET'])
def get_money_for_text():  
    theme_name = flask.request.args['theme_name']
    id = flask.request.args['id'] 
    return str(texts.get_money_for_text(theme_name, id))

@app.route('/post_new_theme', methods=['POST'])
def post_new_theme():
    theme_name = flask.request.args['theme_name']
    return str(texts.post_new_theme(theme_name))

@app.route('/post_text', methods=['POST'])
def post_text():
    theme_name = flask.request.args['theme_name']
    demo = flask.request.args['demo']
    text = flask.request.args['text']
    return str(texts.post_text(theme_name, demo, text))


def main():
    app.run('::', port=8000)


if __name__ == '__main__':
    main()

