# Version: 1.0.2
# Added a type hint for the Barcode class.
# The error message you're seeing is related to static type checking in Python.
# Specifically, it's indicating that the Barcode class is not recognized as a member of the barcode module.
# This error message is similar to the previous error message you had regarding the errors module.
# This error message might be a false positive caused by the way barcode is structured or imported.

# import barcode
# from barcode.writer import ImageWriter
# from typing import Type

# # Define content of barcode as a string
# number = input("Enter the code to generate barcode: ")

# try:
#     # Get the required barcode format
#     barcode_format: Type[barcode.Barcode] = barcode.get_barcode_class('upc')

#     # Generate barcode and render as image
#     my_barcode: barcode.Barcode = barcode_format(number, writer=ImageWriter())

#     # Save barcode as PNG
#     my_barcode.save("generated_barcode.png")
#     print("Barcode saved as generated_barcode.png")

# except ValueError:
#     print("Error: code must be a numeric string.")
# except barcode.errors.IllegalCharacterError:
#     print("Error: code contains non-numeric characters.")
# except barcode.errors.NumberOfDigitsError:
#     print("Error: code must be exactly 12 digits long.")

# By adding a type hint for the Barcode class, you're explicitly telling Python that my_barcode is an instance of barcode.
# Barcode, which might help static type checkers like pylance to recognize the Barcode class as a member of the barcode module.




# Version: 1.0.1
# from typing import Type
# The code in Version: 1.0 seems to be correct, but it may produce some errors depending on the input provided by the user.
# Here are some possible errors that may occur:

# 1. If the user inputs a non-numeric string as the code, the program will raise a ValueError when the barcode_format() function is called.
# This is because the UPC format only accepts numeric codes.

# 2. If the user inputs a code that is too long or too short for the UPC format,
# the program will raise a barcode.errors.IllegalCharacterError or a barcode.errors.NumberOfDigitsError, respectively.

# To handle these errors, you can wrap the barcode_format() call in a try-except block and provide appropriate error messages to the user.

# With this error handling code,
# the program will inform the user about any input errors that occur and prompt them to enter a valid code.


# import barcode
# from barcode.writer import ImageWriter

# # Define content of barcode as a string
# number = input("Enter the code to generate barcode : ")

# try:
#     # Get the required barcode format
#     barcode_format: Type[barcode.Barcode] = barcode.get_barcode_class('upc')

#     # Generate barcode and render as image
#     my_barcode = barcode_format(number, writer=ImageWriter())

#     # Save barcode as PNG
#     my_barcode.save("generated_barcode.png")
#     print("Barcode saved as generated_barcode.png")

# except ValueError:
#     print("Error: code must be a numeric string.")
# except barcode.errors.IllegalCharacterError:
#     print("Error: code contains non-numeric characters.")
# except barcode.errors.NumberOfDigitsError:
#     print("Error: code must be exactly 12 digits long.")



# Version: 1.0
import barcode 
from barcode.writer import ImageWriter

# Define content of barcode as a string
number = input("Enter the code to generate barcode : ")

# Get the required barcode format
barcode_format = barcode.get_barcode_class('upc')

# Generate barcode and render as image
my_barcode = barcode_format(number, writer=ImageWriter())

# Save barcode as PNG
my_barcode.save("generated_barcode")

# #rayturner.dev #clcoding.com