# Version: 1.0.1
import barcode 
from barcode.writer import ImageWriter

# Define content of barcode as a string
number = input("Enter the code to generate barcode : ")

try:
    # Get the required barcode format
    barcode_format = barcode.get_barcode_class('upc')

    # Generate barcode and render as image
    my_barcode = barcode_format(number, writer=ImageWriter())

    # Save barcode as PNG
    my_barcode.save("generated_barcode.png")
    print("Barcode saved as generated_barcode.png")

except ValueError:
    print("Error: code must be a numeric string.")
except barcode.errors.IllegalCharacterError:
    print("Error: code contains non-numeric characters.")
except barcode.errors.NumberOfDigitsError:
    print("Error: code must be exactly 12 digits long.")

# With this error handling code,
# the program will inform the user about any input errors that occur and prompt them to enter a valid code.

# The code in Version: 1.0 seems to be correct, but it may produce some errors depending on the input provided by the user.
# Here are some possible errors that may occur:

# 1. If the user inputs a non-numeric string as the code, the program will raise a ValueError when the barcode_format() function is called.
# This is because the UPC format only accepts numeric codes.

# 2. If the user inputs a code that is too long or too short for the UPC format,
# the program will raise a barcode.errors.IllegalCharacterError or a barcode.errors.NumberOfDigitsError, respectively.

# To handle these errors, you can wrap the barcode_format() call in a try-except block and provide appropriate error messages to the user.
# Here's an updated version of the code with error handling:















# Version: 1.0
# import barcode 
# from barcode.writer import ImageWriter

# # Define content of barcode as a string
# number = input("Enter the code to generate barcode : ")

# # Get the required barcode format
# barcode_format = barcode.get_barcode_class('upc')

# # Generate barcode and render as image
# my_barcode = barcode_format(number, writer=ImageWriter())

# # Save barcode as PNG
# my_barcode.save("generated_barcode")

# #rayturner.dev #clcoding.com