# 如何查看全局和局部中的内容
a = 10
b = 20

def func():
    print(locals())  # locals 查看的是当前作用域中的内容
    '''
    {'__name__': '__main__', '__doc__':
     None, '__package__': None, '__loader__':
      <_frozen_importlib_external.SourceFileLoader object at 0x0000021C0F691CC0>, 
      '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 
      'G:/python_study/day10 函数进阶/04 名称空间与作用域.py', '__cached__': None, 'a': 10, 'b': 20, 
      'func': <function func at 0x0000021C111DC1E0>}
    '''
    # 查看局部作用域中的内容，要将其放置到对应的位置
# 查看全局作用域中的内容
print(globals())
'''{'__name__': '__main__', 
'__doc__': None, '__package__': None, '__loader__':
 <_frozen_importlib_external.SourceFileLoader object at 0x0000014649251CC0>,
  '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__':
         'G:/python_study/day10 函数进阶/04 名称空间与作用域.py', '__cached__': None, 'a': 10, 'b': 20, 
   'func': <function func at 0x000001464AE6C1E0>}
'''
