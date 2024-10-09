#!/home/codespace/.python/current/bin/python3

def greet(language_code):
    match language_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'
        
def extract_language(locale):
    # locales come in the format:
    #       'en_US.UTF-8'
    #       'en_GB.UTF-8'
    #       'en_AU.UTF-8'

    return locale.split('_')[0]

def extract_region(locale):
    # locales come in the format:
    #       'en_US.UTF-8'
    #       'en_GB.UTF-8'
    #       'en_AU.UTF-8'

    return locale.split('_')[1].split('.')[0]

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    match (language, region):
        case ('en', 'US'):
            return 'Hey!'
        case ('en', 'GB'):
            return 'Hello!'
        case ('en', 'AU'):
            return 'Howdy!'
        case _:
            return greet(language)

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!