# Import all libraries
import requests
import time
import os
from discord_webhook import DiscordWebhook
import json

with open('skipall.txt', 'r') as f:
    toskip = f.read()

def print_text(text, speed): # Text print, like in undertale
    for i in text:
        time.sleep(speed)
        print(i, end='', flush=True)

def check_limit(prox_lol):
        response = requests.get(f'https://discord.com/api/v8/entitlements/gift-codes/123', proxies=prox_lol)
        try:
            json_data = json.loads(response.text)

            if json_data['message'] == 'You are being rate limited.':
                rate_limit_mins = int(json_data['retry_after']) / 60000
                print_text('Oops! There is a problem. All proxies, and your IP has been rate limited. You need to try again in '+str(json_data['retry_after'])+'ms! ('+str(rate_limit_mins)+'min)', 0.04)
                input()
                exit()
            else:
                pass
        except json.JSONDecodeError:
            print('No rate limit detected. Continue loop.')
if toskip == '0':
    # About programm
    print_text('''Warning! This freeware does not connected with Discord, or others.
This freeware for EDUCATION PURPOSES, NOT MORE.
If you have issues, write on this email: ojector@ojector.ru
    ''', 0.02)
    input('\nPress any key to continue')
    print_text('Hey! Welcome to the OJector`s NITRO CHECKER!\n', 0.03)
    print_text('There is a choice. You need select one of them.\n', 0.03)
    print_text('1 — Tutorial of the programm. 2 — Launch the programm\n', 0.03)
inp = input('Your choice is: ')
if inp == '2':
    # Check for all needed files
    if not os.path.isfile('proxy.prox'):
        print_text('Proxy file doesn`t found! Create file proxy.prox and enter proxies, after this launch, try to launch the programm again.', 0.03)
        input()
        exit()
    elif not os.path.isfile('codes.txt'):
        print_text('Codes file doesn`t found! Create file codes.txt and enter codes, after this, try to launch the programm again.', 0.03)
        input()
        exit()
    elif not os.path.isfile('webhook.txt'):
        print_text('Webhook file doesn`t found! Create file webhook.txt and enter webhook, after this, try to launch the programm again.', 0.03)
        input()
        exit()
    if not os.path.isfile('working_codes.txt'):
        f = open('working_codes.txt', 'w+')
        f.close()
    # The main code

    # Read codes file
    f = open('codes.txt', 'r')
    codes = f.readlines()
    f.close()

    # Read proxies file
    f = open('proxy.prox', 'r')
    proxy = f.read()
    f.close()
    # Read webhook file
    f = open('webhook.txt', 'r')
    hook = f.read()
    f.close()
    if True:
        def quickChecker(nitro:str, webhook_url, proxys):  # Used to check a single code at a time
            # Generate the request url
            url = f"https://discord.com/api/v8/entitlements/gift-codes/{nitro}"
            response = requests.get(url, proxies=proxys)  # Get the response from discord

            if response.status_code == 200:  # If the responce went through
                # Notify the user the code was valid
                print(f" Valid | {nitro} ", flush=True,
                      end="" if os.name == 'nt' else "\n")
                with open("working_codes.txt", "w") as file:  # Open file to write
                    # Write the nitro code to the file it will automatically add a newline
                    file.write(nitro)

                if webhook_url is not None:  # If a webhook has been added
                    DiscordWebhook(  # Send the message to discord letting the user know there has been a valid nitro code
                        url=url,
                        content=f"Valid Nitro Code detected! @everyone \n{nitro}"
                    ).execute()

                return True  # Tell the main function the code was found
            else:
                print(f' False | {nitro}', flush=True, end="" if os.name == 'nt' else "\n")
    prox_list = {"http" : prox for prox in proxy} # Unzip the proxies list
    if __name__ == '__main__':
        for code in codes: # Main code
            check_limit(prox_list)
            quickChecker(code, hook, prox_list) # Check the code
            time.sleep(0.4)
else:
    print_text('''How to use the programm?
To get started, create 3 files.
"codes.txt" — for the codes, programm need to check.
"proxy.prox" — for the proxies, programm need to use.
"webhook.txt" — sends the VALID nitro code to this webhook.
** Where I can get codes?
You can generate it in this file: gen.py
    ''', 0.05)
input('\nPress any key, to continue')
print_text('And.., there it is!', 0.1)
input()
