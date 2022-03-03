#---Simple decorator--------#

def debug(func):
   msg_name = func.__name__
   msg_qualname = func.__qualname__
   def wrapper(*args,**kwargs):
      """It is a wrapper function """
      print(f'msg_name: {msg_name}')
      print(f'msg_qualname: {msg_qualname}')
      return func(*args,**kwargs)
   return wrapper

@debug
def add(x,y):
   """ This is add function"""
   return x+y

p = add(5,6)
print(p)
print(add.__name__) # comes wrapper, where as it shuld be add
print(add.__doc__) # comes wrapper.__doc__, where as it shuld be add.__doc__


#---Decorator with @wrpas------#
from functools import wraps

def debug(func):
   msg_name = func.__name__
   msg_qualname = func.__qualname__
   @wraps(func)
   def wrapper(*args,**kwargs):
      """It is a wrapper function """
      print(f'msg_name: {msg_name}')
      print(f'msg_qualname: {msg_qualname}')
      return func(*args,**kwargs)
   return wrapper

@debug
def add(x,y):
   """ This is add function"""
   return x+y

p = add(5,6)
print(f'with @wraps: {p}')
print(f'with @wraps: {add.__name__}') # comes wrapper, where as it shuld be add
print(f'with @wraps: {add.__doc__}') # comes wrapper.__doc__, where as it shuld be add.__doc__

#---Decorator with arguments------#

from functools import wraps

def debug_arg(argm = ''):
   def debug(func):
      msg_name = argm + func.__name__
      msg_qualname = argm + func.__qualname__
      @wraps(func)
      def wrapper(*args,**kwargs):
         """It is a wrapper function """
         print(f'msg_name: {msg_name}')
         print(f'msg_qualname: {msg_qualname}')
         return func(*args,**kwargs)
      return wrapper
   return debug

@debug_arg('with arguments *** ')
def add(x,y):
   """ This is add function"""
   return x+y

p = add(5,6)
print(f'with arg: {p}')


#-----Decorator with class--------#

x = 5
print(type(x))

y = 'pj'
print(type(y))

z = ['5','pj']
print(type(z))

print(type(int))
print(type(type))
