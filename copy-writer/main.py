import requests
import argparse


def create_main_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default=8000, type=int)

    return parser


def get_theme_list(main_args):
    theme_list = requests.get(f'http://{main_args.host}:{main_args.port}/get_theme_list').text
    if len(theme_list) > 2:
        print('Here is a theme list: ', theme_list)
    else:
        print('Theme list is empty yet')
        user_answer = input('Do you want to add a theme (Y/n)?> ')
        if user_answer == 'Y':
            post_new_theme(main_args)
        elif user_answer == 'n':
            print('OK, let\'s continue')
        else:
            print('Didn\'t understand you, so let\'s continue')

def get_money_for_text(main_args):
    theme_name = input('Which theme is your text written on?> ')
    id = input('What is the text id?> ')
    response = requests.get(f'http://{main_args.host}:{main_args.port}/get_money_for_text', 
                                                    params=dict(theme_name=theme_name, id=id)).text
    if response == 'Unknown theme':
        user_input = input(f'{response}, do you want to try again (Y/n)?> ')
        if user_input == 'Y':
            get_money_money_for_text(main_args)
        elif user_input == 'n':
            print('OK, let\'s continue')
        else:
            print('Didn\'t understand you, so let\'s continue')
    elif response == 'No text with such id':
        user_input = input(f'{response}, do you want to try again (Y/n)?> ')
        if user_input == 'Y':
            get_money_for_text(main_args)
        elif user_input == 'n':
            print('OK, let\'s continue')
        else:
            print('Didn\'t understand you, so let\'s continue')
    elif int(response) == 0:
        print('You have not earned money for this text yet')
    else:
        print('Please get your money: ', '$'*int(response))

def post_text(main_args):
    theme_name = input('Which theme would you like to post a text on?> ')
    demo = input('Please write here your demo> ')
    text = input('Please write here your exciting text> ')
    response = requests.post(f'http://{main_args.host}:{main_args.port}/post_text', 
                                                        params=dict(theme_name=theme_name, demo=demo, text=text)).text
    if response in ['demo', 'text']:
        print(f'There is a text with the same {response} in the system')
        user_input = input(f'{response}, do you want to try again (Y/n)?> ')
        if user_input == 'Y':
            post_text(main_args)
        elif user_input == 'n':
            print('OK, let\'s continue')
        else:
            print('Didn\'t understand you, so let\'s continue')
    else:
        print(f'Your text successfully posted. Its id is {response}')

def my_exit():
    user_answer = input(' Are you sure you want to leave (Y/n)?> ')
    if user_answer == 'Y':
        print('Goodbye!')
        exit()
    elif user_answer == 'n':
        print('OK, let\'s continue')
    else:
        print('Didn\'t understand you, so let\'s continue')


def main():
    main_parser = create_main_parser()
    main_args = main_parser.parse_args()

    while True:
        try:
            cmd = input('Enter command>')
            if cmd == 'get_theme_list':
                get_theme_list(main_args)
            elif cmd == 'get_money_for_text':
                get_money_for_text(main_args)
            elif cmd == 'post_text':
                post_text(main_args)
            elif cmd == 'exit':
                my_exit()
            else:
                print(f'Unknown command: {cmd}')
        except KeyboardInterrupt:
            my_exit()

if __name__ == '__main__':
    main()

