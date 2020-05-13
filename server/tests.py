import unittest
import lib

class TestText(unittest.TestCase):
    def test_class(self):
        new_text = lib.Text('theme_name', 'demo', 'text', 13)
        self.assertEqual(new_text.earned, 0)

class TestTheme(unittest.TestCase):
    def test_class(self):
        new_theme = lib.Theme('theme_name')
        self.assertEqual(new_theme.texts, [])

    def test_adding(self):
        theme = lib.Theme('theme_name')
        new_text = lib.Text('theme_name', 'demo1', 'text1', 13)
        self.assertEqual(theme.add_text(new_text), 'OK')
        text_with_same_demo = lib.Text('theme_name', 'demo1', 'text2', 14)
        self.assertEqual(theme.add_text(text_with_same_demo), 'demo')
        text_with_same_text = lib.Text('theme_name', 'demo3', 'text1', 15)
        self.assertEqual(theme.add_text(text_with_same_text), 'text')
        text_with_same_id = lib.Text('theme_name', 'demo4', 'text4', 13)
        self.assertEqual(theme.add_text(text_with_same_id), 'id')
        text_with_another_theme = lib.Text('another_theme_name', 'demo', 'text', 13)
        self.assertEqual(theme.add_text(text_with_another_theme), 'Inappropriate theme')
        another_text = lib.Text('theme_name', 'demo100', 'text100', 100)
        self.assertEqual(theme.add_text(another_text), 'OK')

class TestTextStorage(unittest.TestCase):
    def test_posting_theme_and_getting_theme_list(self):
        texts = lib.TextStorage()
        texts.post_new_theme('name1')
        texts.post_new_theme('name2')
        self.assertEqual(texts.get_theme_list(), ['name1', 'name2'])
    
    def test_adding_text(self):
        texts = lib.TextStorage()
        self.assertEqual(texts.post_text('theme_name', 'demo', 'text'), 0)
        self.assertEqual(texts.post_text('theme_name', 'demo', 'text'), 'demo')
        self.assertEqual(texts.post_text('theme_name', 'demo1', 'text1'), 1)
        self.assertEqual(texts.post_text('theme_name1', 'demo', 'text'), 0)

    def test_getting_demos(self):
        texts = lib.TextStorage()
        texts.post_text('theme_name1', 'demo1', 'text1')
        texts.post_text('theme_name1', 'demo2', 'text2')
        texts.post_text('theme_name3', 'demo3', 'text3')
        self.assertEqual(texts.get_demos('theme_name1'), [['demo1', 'text id is 0'], ['demo2', 'text id is 1']])
    
    def test_getting_full_text_and_getting_money(self):
        texts = lib.TextStorage()
        texts.post_text('theme_name', 'demo', 'text')
        self.assertEqual(texts.get_full_text('theme_name', 0), 'text')
        self.assertEqual(texts.themes['theme_name'].texts[0].earned, 1)
        self.assertEqual(texts.get_full_text('theme_name2', 0), 'Unknown theme')
        self.assertEqual(texts.get_full_text('theme_name', 1), 'No text with such id')
        self.assertEqual(texts.get_money_for_text('theme_name', 0), 1)
        self.assertEqual(texts.get_money_for_text('theme_name', 0), 0)

