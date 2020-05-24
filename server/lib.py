import config


class Text:
    def __init__(self, theme_name, demo, text, id):
        self.theme_name = theme_name
        self.demo = demo
        self.text = text
        self.id = int(id)
        self.earned = 0


class Theme:
    def __init__(self, name):
        self.name = name
        self.texts = []

    def check_new_text(self, text_object):
        for text in self.texts:
            if text_object.demo == text.demo:
                return config.demo
            if text_object.text == text.text:
                return config.text
            if text_object.id == text.id:
                return config.id
        return config.OK

    def add_text(self, text_object):
        if text_object.theme_name != self.name:
            return config.inappropriate_theme
        check_text = self.check_new_text(text_object)
        if check_text == config.OK:
            self.texts.append(text_object)
        return check_text


class TextStorage:
    def __init__(self):
        self.themes = {}
    
    def get_theme_list(self):
        if len(self.themes.keys()) == 0:
            return
        return list(self.themes.keys())
    
    def post_new_theme(self, theme_name):
        if theme_name not in self.themes.keys():
            self.themes[theme_name] = Theme(theme_name)
            return config.OK
        else:
            return config.known_theme
    
    def post_text(self, theme_name, demo, text):
        if not theme_name in self.themes.keys():
            self.themes[theme_name] = Theme(theme_name)
        new_text = Text(theme_name, demo, text, len(self.themes[theme_name].texts))
        response = self.themes[theme_name].add_text(new_text)
        return new_text.id if response == config.OK else response
    
    def get_demos(self, theme_name):
        if not theme_name in self.themes.keys():
            return config.unknown_theme
        demos = []
        if len(self.themes[theme_name].texts) == 0:
            return
        for text in self.themes[theme_name].texts:
            demos.append([text.demo, config.id_f(text.id)])
        return list(demos)
    
    def get_full_text(self, theme_name, id):
        if not theme_name in self.themes.keys():
            return config.unknown_theme
        if len(self.themes[theme_name].texts) > int(id):
            self.themes[theme_name].texts[int(id)].earned += 1
            return self.themes[theme_name].texts[int(id)].text
        else:
            return config.no_id
    
    def get_money_for_text(self, theme_name, id):
        if not theme_name in self.themes.keys():
            return config.unknown_theme
        elif len(self.themes[theme_name].texts) > int(id):
            earned = self.themes[theme_name].texts[int(id)].earned
            self.themes[theme_name].texts[int(id)].earned = 0
            return earned
        else:
            return config.no_id

