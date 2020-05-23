default_port = 8000
default_hast = 'localhost'

server_name = 'copy-writer-server'

def get_path(args, path):
    return f'http://{args.host}:{args.port}' + path

get_theme_list = 'get_theme_list'
get_theme_list_path = '/' + get_theme_list
get_demos = 'get_demos'
get_demos_path = '/' + get_demos
get_full_text = 'get_full_text'
get_full_text_path = '/' + get_full_text
get_money_for_text = 'get_money_for_text'
get_money_for_text_path = '/' + get_money_for_text
post_new_theme = 'post_new_theme'
post_new_theme_path = '/' + post_new_theme
post_text = 'post_text'
post_text_path = '/' + post_text
exit = 'exit'

get_method = 'GET'
post_method = 'POST'

OK = 'OK'
NONE = 'None'
dollar = '$'
yes = 'Y'
no = 'n'
bye = 'Goodbye!'
sys_symbol = '>'

unknown_theme = 'Unknown theme'
inappropriate_theme = 'Inappropriate theme'
known_theme = 'Already known theme'
no_id = 'No text with such id'

theme_name = 'theme_name'
id = 'id'
demo = 'demo'
text = 'text'

ask = {theme_name:'>Which theme are you interested in?> ', id: '>What is the text id?> ',  
            demo: '>Please write here your demo> ', text: '>Please write here your exciting text> '}

ask_cmd = sys_symbol + 'Enter command>'
ask_try_again = sys_symbol + 'Do you want to try again (Y/n)?> '
ask_add_text = sys_symbol + 'Do you want to add a new text on any of yours (Y/n)?> '
ask_leave = sys_symbol + 'Are you sure you want to leave (Y/n)?> '
ask_input_with_sys_sumbol = sys_symbol + 'Input can\'t begin with  ">"  > '


def ask_try_again_f(response):
    return sys_symbol + f'{response}, do you want to try again (Y/n)?> '


def ask_another_theme_f(response):
    return sys_symbol + f'{response}, do you want to choose another (Y/n)?> '


def ask_another_text_f(response):
    sys_symbol + f'{response}, do you want to get another text (Y/n)?> '


def ask_new_theme_problem_f(response):
    return sys_symbol + f'{response}, do you want to put another (Y/n)?> '


empty_list = sys_symbol + 'Theme list is empty yet'
here_theme_list = sys_symbol + 'Here is a theme list: '
no_money_yet = sys_symbol + 'You have not earned money for this text yet'
can_get_money =  sys_symbol + 'Please get your money: '
lets_continue = sys_symbol + 'OK, let\'s continue'
inappropriate_continue = sys_symbol + 'Didn\'t understand you, so let\'s continue'
int_warning = sys_symbol + 'id must be int'
here_text = sys_symbol + 'Here is the text:'
here_new_theme = sys_symbol + 'Your theme is now available!'


def unknown_cmd_f(cmd):
    return sys_symbol + f'Unknown command: {cmd}'


def text_with_same_f(response):
    return sys_symbol + f'There is a text with the same {response} in the system'


def posted_f(response):
    return sys_symbol + f'Your text successfully posted. Its id is {response}'


def id_f(text_id):
    return sys_symbol + f'text id is {text_id}'


def no_texts_f(theme_name):
    return sys_symbol + f'>Here are no texts on theme {theme_name}'


def here_demos_f(theme_name):
    return sys_symbol + f'Here are demos on the theme {theme_name}: '

