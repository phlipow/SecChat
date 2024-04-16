import os
from getpass import getpass

# Colors
GREEN = '\033[32m'
RED = '\033[31m'
BLUE = '\033[34m'
USER = '\033[35m'
CONTACT = '\033[95m'
RESET = '\033[0m'

# Colored messages
def success(text):
    print(f'{GREEN}{text}{RESET}')

  
def error(text):
    print(f'{RED}{text}{RESET}')
   
def warning(text, i=0, type='message'):
    if type == 'message': print(BLUE + text + RESET)
    elif type == 'input': return input(BLUE + text + RESET)
    elif type == 'option': print(BLUE + str(i) + ' - ' + RESET + text)
        
def user_message(name, msg):
    print(USER + name + ': ' + RESET + msg)
    
def contact_message(name, msg):
    print(CONTACT + name + ': ' + RESET + msg)


# Clear terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    


# Interactive menu
def menu(options, input_message='Choose an option: ', success_text='Menu', error_text='Invalid option', print_option_title=True):

    clear_terminal()
    
    if success_text:
        success(success_text)
    elif error_text:
        error(error_text)
        
    for option in options:
        warning(option['title'], i=option['number'], type='option')
        
    if input_message:    
        choice = warning(input_message, type='input')
    else:
        getpass('')
        return
    
    try:
        choice = int(choice)
        if not any(option['number'] == choice for option in options): raise ValueError
    except:
        error_cpy = error_text
        return menu(options, success_text=False, error_text=error_cpy)
    else:
        choosen = next(option for option in options if option['number'] == choice)
        clear_terminal()
        if choosen.get('message'):
            success(choosen['message'])
        elif print_option_title:
            success(choosen['title'])
        return choosen['function'](*choosen.get('args', ()))