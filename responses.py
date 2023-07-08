import random

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Whats up choom'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == 'n!help':
        return "`I like trains`"

