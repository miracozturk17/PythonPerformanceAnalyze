import timeit

def test_function():
    '''BU ALANDA TEST ETMEK ISTEDIGINIZ KOD BLOGU YER ALMALI.'''
    a=5
    b=6
    c=((a**6)-7*b)/2.05
    return c

setup_code = ''' '''
'''
   from __main__ import LIBRARY,
   import LIBRARY,
   vb.
'''
execution_time = timeit.timeit(
                               stmt=test_function,
                               setup=setup_code,
                               number=1000000
                              )

execution_repeat_time = timeit.repeat(
                               stmt=test_function,
                               setup=setup_code,
                               number=1000000,
                               repeat=5
                              )
print(f"Calisma zamani: {execution_time:.6f} saniye")
print(f"Tekrarli calisma zamani: {execution_repeat_time:} saniye")