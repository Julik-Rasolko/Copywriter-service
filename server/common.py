import argparse
import config


def create_main_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default=config.default_hast)
    parser.add_argument('--port', default=config.default_port, type=int)

    return parser.parse_args()


def my_exit():
    user_answer = input(config.ask_leave)
    if user_answer == config.yes:
        print(config.bye)
        exit()
    elif user_answer == config.no:
        print(config.lets_continue)
    else:
        print(config.inappropriate_continue)


def dialog(func, func_args, question = config.ask_try_again):
    user_answer = input(question)
    if user_answer == config.yes:
        func(func_args)
    elif user_answer == config.no:
        print(config.lets_continue)
    else:
        print(config.inappropriate_continue)


def get_argument(arg_type):
    if arg_type == config.id:
        success = False
        while not success:
            try:
                arg = int(input(config.ask[arg_type]))
                success = True
            except ValueError:
                print(config.int_warning)
    else:
        arg = input(config.ask[arg_type])
        while arg[0] == config.sys_symbol:
            arg = input(config.ask_input_with_sys_sumbol)
    return arg

