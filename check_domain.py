import menu
from check_availability import is_available
import handle

while True:
    menu.print_app_menu()
    user_input = input(": ").rstrip()
    # Get input from the user
    while True:
        try:
            user_input = int(user_input)
            break
        except ValueError:
            user_input = input(": ").rstrip()
            continue

    # 1. Check availability of a given domain
    if user_input == 1:
        domain_name = input("Enter domain name to check(without .com): ")
        print("Checking availability of " + domain_name + ".com")
        available = is_available(domain_name)

        if available == '':
            print(domain_name + ".com" + " is already taken!")
        else:
            handle.handle_is_available(domain_name)

    # 2. Get a random domain name suggestion
    if user_input == 2:
        handle.handle_get_random_domain_name()

    # 3. Exit
    if user_input == 3:
        break
