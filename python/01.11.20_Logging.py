
# critical
#
# error
#
# warning
#
# info
#
# debug
#
# notset

#
# import logging
# logging.basicConfig(filename='01.11.20log.txt',level =logging.ERROR)
#
# logging.critical("Hello i am the critical error")
# logging.error("Hello i am the error")
#
# logging.warning("I am a warning")
# logging.info("I am the info")
# logging.debug("I am the debug")



import logging

logging.basicConfig(filename='01.11.20log.txt',level =logging.ERROR)

try:
    a = int(input("Enter the number"))
    b = int(input("Enter the number"))
    c = a/b
except Exception as e:
    logging.exception(e)

else:
    print('The result of division '+ str(c))
#
# in the console
# Enter the number1
# Enter the number0
#
# in the 01.11.20log.txt file
# ERROR:root:division by zero
# Traceback (most recent call last):
#   File "/Users/Hiren/PycharmProjects/pythonbasic/01.11.20_Logging.py", line 34, in <module>
#     c = a/b
# ZeroDivisionError: division by zero
