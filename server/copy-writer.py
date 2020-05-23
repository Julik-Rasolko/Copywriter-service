import requests
import common
import config


def get_theme_list(main_args):
    theme_list = requests.get(config.get_path(main_args, config.get_theme_list_path)).text
    if theme_list == config.NONE:
        print(config.print_empty_list)
        common.dialog(post_text, main_args, config.ask_add_text)
    else:
        print(config.print_theme_list, theme_list)


def get_money_for_text(main_args):
    theme_name = common.get_argument(config.theme_name)
    id = common.get_argument(config.id)
    response = requests.get(config.get_path(main_args, config.get_money_for_text_path), 
                                                    params=dict(theme_name=theme_name, id=id)).text
    if response == config.unknown_theme or response == config.no_id:
        common.dialog(get_money_for_text, main_args, config.ask_try_again_f(response))
    elif int(response) == 0:
        print(config.print_no_money_yet)
    else:
        print(config.print_get_money, config.dollar*int(response)) 


def post_text(main_args):
    theme_name = common.get_argument(config.theme_name)
    demo = common.get_argument(config.demo)
    text = common.get_argument(config.text)
    response = requests.post(config.get_path(main_args, config.post_text_path), 
                                            params=dict(theme_name=theme_name, demo=demo, text=text)).text
    if response in [config.demo, config.text]:
        print(config.print_text_with_same_f(response))
        common.dialog(post_text, main_args)
    else:
        print(config.print_posted_f(response))


def main():
    main_args = common.create_main_args()

    while True:
        try:
            cmd = input(config.ask_cmd)
            if cmd == config.get_theme_list:
                get_theme_list(main_args)
            elif cmd == config.get_money_for_text:
                get_money_for_text(main_args)
            elif cmd == config.post_text:
                post_text(main_args)
            elif cmd == config.exit:
                common.my_exit()
            else:
                print(config.print_unknown_cmd_f(cmd))
        except KeyboardInterrupt:
            common.my_exit()


if __name__ == config.main:
    main()

