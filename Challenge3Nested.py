def get_value(obj, key):
    keys = key.split('/')  # split the key into its parts
    for k in keys:
        obj = obj.get(k)  # get the nested object for each key
        if obj is None:
            return None  # return None if any key is not found
    return obj

object1 = {"a":{"b":{"c":"d"}}}
key1 = "a/b/c"
value1 = get_value(object1, key1)
print(value1)  # prints "d"

object2 = {"x":{"y":{"z":"a"}}}
key2 = "x/y/z"
value2 = get_value(object2, key2)
print(value2)  # prints "a"



# To implement this code, you can follow these steps:

# Define the get_value function which takes two arguments: obj and key.
# Split the key string into its parts using the forward slash (/) separator. This can be done using the split method of the string.
# Loop over the parts of the key and use the get method of the obj dictionary to get the nested object for each key. If any key is not found, return None.
# Return the final object obtained after looping over all the keys.
# Call the get_value function with the obj and key arguments you want to test, and store the result in a variable.
# Print the value of the variable to verify that the function works as expected.


# Note that the get_value function can be reused for any nested object and key combination you want to access.

# Python3 Challenge3Nested.py