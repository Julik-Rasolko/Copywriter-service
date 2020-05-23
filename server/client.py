import requests
import common
import config


def get_theme_list(main_args):
    theme_list = requests.get(config.get_path(main_args, config.get_theme_list_path)).text
    if theme_list == config.NONE:
        print(config.empty_list)
        common.dialog(post_new_theme, main_args, config.ask_add_text)
    else:
        print(config.here_theme_list, theme_list)


def get_demos(main_args):
    theme_name = common.get_argument(config.theme_name)
    response = requests.get(config.get_path(main_args, config.get_demos_path), 
                                                    params=dict(theme_name=theme_name)).text
    if response == config.unknown_theme:
        common.dialog(get_demos, main_args, config.ask_another_theme_f(response))
    elif response == config.NONE:
        print(config.no_texts_f(theme_name))
        common.dialog(get_demos, main_args)
    else:
        print(config.here_demos_f(theme_name), response)


def get_full_text(main_args):
    theme_name = common.get_argument(config.theme_name)
    id = common.get_argument(config.id)
    response = requests.get(config.get_path(main_args, config.get_full_text_path), 
                                                    params=dict(theme_name=theme_name, id=id)).text
    if response == config.unknown_theme or response == config.no_id:
        common.dialog(get_full_text, main_args, config.ask_another_text_f(response))
    else:
        print(config.here_text)
        print(response)


def post_new_theme(main_args):
    theme_name = common.get_argument(config.theme_name)
    response = requests.post(config.get_path(main_args, config.post_new_theme_path), 
                                                    params=dict(theme_name=theme_name)).text
    if response == config.OK:
        print(config.here_new_theme)
    else:
        common.dialog(post_new_theme, main_args, config.ask_new_theme_problem_f(response))


def main():
    main_args = common.create_main_args()

    while True:
        try:
            cmd = input(config.ask_cmd)
            if cmd == config.get_theme_list:
                get_theme_list(main_args)
            elif cmd == config.get_demos:
                get_demos(main_args)
            elif cmd == config.get_full_text:
                get_full_text(main_args)
            elif cmd == config.post_new_theme:
                post_new_theme(main_args)
            elif cmd == config.exit:
                common.my_exit()
            else:
                print(config.unknown_cmd_f(cmd))
        except KeyboardInterrupt:
            common.my_exit()


if __name__ == '__main__':
    main()

