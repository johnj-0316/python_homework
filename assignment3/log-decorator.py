# Task 1
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger.log(logging.INFO, func.__name__)
        logger.log(logging.INFO, args or None)
        logger.log(logging.INFO, kwargs or None)
        logger.log(logging.INFO, func(*args, **kwargs))
        
    return wrapper

@logger_decorator
def hello_world():
    print("Hello, World!")
    
@logger_decorator
def pos_args(*args):
    return True

@logger_decorator
def key_args(**kwargs):
    return logger_decorator

hello_world()
pos_args("hey")
key_args(test="testing!")