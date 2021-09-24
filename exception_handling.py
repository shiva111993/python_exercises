# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:
# try:
#     print(x)
# except:
#     print("An exception occurred")

# -----------

# try:
#     print(x)
# except NameError:
#     print("An exception occurred")
# except:
#     print("Something else went wrong")

# --------------
# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised
# from typing import final


# try:
#     print("hello")
# except:
#     print("Something went wrong")
# else:
#     print("Nothing went wrong")

# --------------------
# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
# try:
#     print(x)
# except:
#     print("something went wrong")
# finally:
#     print("The 'try except' is finished")

# ----------------------

# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")

# ------------------------
# Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword.
x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")
# -------
x = -1
if not type(x) is int:
  raise Exception("Sorry, no numbers below zero")

# ------------------------