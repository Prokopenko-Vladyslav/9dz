def parse_command(command):
    command_parts = command.lower().split(' ', 1)
    if len(command_parts) > 1:
        action, details = command_parts
        return action, details
    else:
        return command_parts[0], None

contacts = dict()

def add_contact(details):
    name, number = details.split()
    contacts[name] = number
    return f"Added {name} with number {number} to contacts."

def change_contact(details):
    name, number = details.split()
    if name in contacts:
        contacts[name] = number
        return f"Changed number for {name} to {number}."
    else:
        return f"{name} not found in contacts."

def phone_number(name):
    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}."
    else:
        return f"{name} not found in contacts."

def show_all():
    if contacts:
        return "\n".join(
            [f"{name}: {number}" for name, number in contacts.items()]
            )
    else:
        return "No contacts available."

def exit_bot():
    return "Good bye!"
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid input"
        except AttributeError:
            return "Attribute error"
    return wrapper

@input_error
def execute_command(action, details=None):
    if action == 'hello':
        return "How can I help you?"
    elif action == 'add':
        return add_contact(details)
    elif action == 'change':
        return change_contact(details)
    elif action == 'phone':
        return phone_number(details)
    elif action == 'show':
        return show_all()
    elif action in ['good', 'bye', 'close', 'exit']:
        return exit_bot()
    else:
        return "Command not recognized."

def main():
    while True:
        user_input = input("Enter a command: ")
        action, details = parse_command(user_input)
        result = execute_command(action, details)
        print(result)
        if result == "Good bye!":
            break

if __name__ == "__main__":
    main()