__author__ = 'Kalyan'

notes = '''
Write your own implementation of converting a number to a given base. It is important to have a good logical
and code understanding of this.

Till now, we were glossing over error checking, for this function do proper error checking and raise exceptions
as appropriate.

Reading material:
    http://courses.cs.vt.edu/~cs1104/number_conversion/convexp.html
'''
import string
def convert(number, base):
    """
    Convert the given number into a string in the given base. valid base is 2 <= base <= 36
    raise exceptions similar to how int("XX", YY) does (play in the console to find what errors it raises).
    Handle negative numbers just like bin and oct do.
    """
    pass
    if base<2 or base>36:
        raise ValueError
    if type(number).__name__!='int' or type(base).__name__!='int':
        raise TypeError
    # if(base==2):
    #     num=bin(number)
    #     return num[2:]
    # if(base==8):
    #     num=oct(number)
    #     num = num.upper()
    #     return num[2:]
    # if(base==16):
    #     num=hex(number)
    #     num=num.upper()
    #     return num[2:]
    s=''
    #number=int(number)
    num=number
    if(number<0):
        number=-(number)
    base_list=list(range(10,36))
    str_list=list(string.ascii_uppercase)
    dictionary=dict(zip(base_list,str_list))
    while number!=0:
        n=number%base
        if(n>=0 and n<10):
            s=s+str(n)
        else:
           s=s+str(dictionary.get(n))
        number=int(number/base)
    s=''.join(reversed(s))
    if (num < 0):
        s='-'+s
    return s

def test_convert():
    assert "100" == convert(4,2)
    assert "FF" == convert(255,16)
    assert "377" == convert(255, 8)
    assert "JJ" == convert(399, 20)
    assert "-JJ" == convert(-399, 20)

    try:
        convert(10,1)
        assert False, "Invalid base <2 did not raise error"
    except ValueError as ve:
        print(ve)

    try:
        convert(10, 40)
        assert False, "Invalid base >36 did not raise error"
    except ValueError as ve:
        print(ve)

    try:
        convert("100", 10)
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print(te)

    try:
        convert(None, 10)
        assert False, "Invalid number did not raise error"
    except TypeError as te:
        print(te)


    try:
        convert(100, "10")
        assert False, "Invalid base did not raise error"
    except TypeError as te:
        print(te)
