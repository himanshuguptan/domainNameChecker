import menu
from selenium import webdriver
from check_availability import is_available
from generate_bird_names import get_bird_names
import random


def handle_is_available(domain_name):
    print(domain_name + ".com" + " is available!")
    menu.print_menu()
    user_input = input(": ").rstrip()
    while True:
        try:
            user_input = int(user_input)
            break
        except ValueError:
            user_input = input(": ").rstrip()
            continue
    if user_input == 1:
        # 1. Open GoDaddy.com for the available domain name
        url = 'https://godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=' + domain_name + ".com"
        new_browser = webdriver.Chrome()
        new_browser.get(url)


def handle_get_random_domain_name():
    print("Generating a random domain name...please be patient...")
    name_list = get_bird_names()
    while True:
        n = random.randint(0, len(name_list) - 1)
        domain_name = name_list[n]
        available = is_available(domain_name)
        if available == '':
            print("Checked " + domain_name + ".com" + "... it is already taken!")
            print("Checking more...")
            continue
        else:
            handle_is_available(domain_name)
            break
