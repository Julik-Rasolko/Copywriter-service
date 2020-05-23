import flask
import lib
import config

app = flask.Flask(config.server_name)
texts = lib.TextStorage()


@app.route(config.get_theme_list_path, methods=[config.get_method])
def get_theme_list():
    return str(texts.get_theme_list())


@app.route(config.get_demos_path, methods=[config.get_method])
def get_demos():
    theme_name = flask.request.args[config.theme_name]
    return str(texts.get_demos(theme_name))


@app.route(config.get_full_text_path, methods=[config.get_method])
def get_full_text():
    theme_name = flask.request.args[config.theme_name]
    id = flask.request.args[config.id] 
    return str(texts.get_full_text(theme_name, id))


@app.route(config.get_money_for_text_path, methods=[config.get_method])
def get_money_for_text():  
    theme_name = flask.request.args[config.theme_name]
    id = flask.request.args[config.id] 
    return str(texts.get_money_for_text(theme_name, id))


@app.route(config.post_new_theme_path, methods=[config.post_method])
def post_new_theme():
    theme_name = flask.request.args[config.theme_name]
    return str(texts.post_new_theme(theme_name))


@app.route(config.post_text_path, methods=[config.post_method])
def post_text():
    theme_name = flask.request.args[config.theme_name]
    demo = flask.request.args[config.demo]
    text = flask.request.args[config.text]
    return str(texts.post_text(theme_name, demo, text))


def main():
    app.run('::', port=config.default_port)


if __name__ == '__main__':
    main()

