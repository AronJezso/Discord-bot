import random


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Whats up choom'

    if p_message[1] == 'd':
        return str(int(p_message[0]) * random.randint(1, int(p_message[2])))

    if p_message == 'n!help':
        return "```So the basics are:\nhello -> Whats up choom\n" \
               " *D* -> returns a random throw from the numbers u give him by replacing the *\n" \
               " ```"

