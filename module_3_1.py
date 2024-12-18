call = 0
def count_calls():
    global call
    call += 1
def string_info(string):
    result = {len(string), string.upper(), string.lower()}
    count_calls()
    return result
def is_contains(string, list_to_search):
    fly = False
    count_calls()
    for i in list_to_search:
        if i.lower() == string.lower():
            fly = True
    return fly
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(call)