def fetch_value_from_nested_object(obj, key_string):
    keys = key_string.split('/')
    value = obj
    try:
        for key in keys:
            value = value[key]
        return value
    except (KeyError, TypeError):
        return None

nested_input = input("Enter the nested object in the format of {'a': {'b': {'c': 'd'}}}: ")
key_input = input("Enter the key in the format of 'a/b/c': ")

try:
    nested_object = eval(nested_input)
except (SyntaxError, TypeError):
    print("Invalid nested object format.")
else:
    result = fetch_value_from_nested_object(nested_object, key_input)
    print(result)
