import random
import string
def autoID(length):
    characters = string.ascii_letters + string.digits  # Includes lowercase, uppercase letters, and numbers
    random_id = ''.join(random.choices(characters, k=length))
    return random_id
