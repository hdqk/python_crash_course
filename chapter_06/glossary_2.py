glossary = {
    'variable': 'a label that references a certain value',
    'string': 'a series of characters',
    'whitespace': 'any nonprinting character',
    'syntax error': 'code that is not valid according to the interpreter',
    'float': 'any number with a decimal point',
    'constant': 'a variable whose value stays the same',
    'list': 'a collection of items in a particular order',
    'slice': 'a specific group if items in a list',
    'tuple': 'an immutable, or unchanging, list',
    'dictionary': 'a collection of key-value pairs',
    'key-value pair': 'a set of values associated with each other',
    'set': 'a collection in which each item must be unique'
}

for key,value in glossary.items():
    print(f"{key.title()}: {value}.\n")