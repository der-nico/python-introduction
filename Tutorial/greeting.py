def greeting(name, language="english"):
    if language =="english":
        return "Hello, {0}!".format(name)
    elif language =="french":
        return "Bonjour, {0}!".format(name)
    else:
        return "I do not speak {0}".format(language)

print greeting("Bob")
print greeting("Christop", "french")
print greeting("Kevin", "italian")


def data_taking_years(default_years=None):
    if default_years ==None:
        default_years =[]
    default_years += [2011,2012]
    return default_years

print data_taking_years()
print data_taking_years()

def call_this_function(func):
    return func()


def build_greeting(salutation):
    def greeting(name):
        return "{0} {1}!".format(salutation, name)
    return greeting

new_greeting = build_greeting("Na, ")
print new_greeting("Nico")
