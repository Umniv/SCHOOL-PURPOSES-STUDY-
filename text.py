import random
import string

characters = string.ascii_letters + string.digits
random_string = "".join(random.choice(characters) for _ in range(6))

print("Random 6-character string:", random_string)