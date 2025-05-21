questions = [
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\na = [1,2,3]\na.append(a)\nprint(a[3][3][3][3][3])\n```",
        "image_link": "",
        "options": {
            "[1,2,3]": False,
            "[1,2,3, [1,2,3, [1,2,3] ]]": False,
            "[1, 2, 3, [...]]": True,
            "SyntaxError": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nx = 11\nprint( [1,2,3,4] [( (x>=5) * 3 ) -2] )\n```",
        "image_link": "",
        "options": {
            "1": False,
            "2": True,
            "3": False,
            "4": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nseries = True, False, True, False\nif series:\n    print(series[False])\n```",
        "image_link": "",
        "options": {
            "False": False,
            "True, False, True, False": False,
            "None": False,
            "True": True
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nprint(1 << 1 ,'|',  1 >> 1)\n```",
        "image_link": "",
        "options": {
            "1 | 0": False,
            "2 | 1": False,
            "2 | 0": True,
            "1 | 1": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nx = (2 == 1) , (2 != 1) \nprint(x)\n```",
        "image_link": "",
        "options": {
            "(False, True)": True,
            "(True, False)": False,
            "(False, False)": False,
            "(True, True)": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\na, *_ , b = ( bool(print) , bool(bool), bool(id('_')), bool(0), bool(int) )\n\nprint(_)\n```",
        "image_link": "",
        "options": {
            "[True, False, True]": False,
            "[False, True, True]": False,
            "[True, True, False]": True,
            "[True, False, False]": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nx = {1, 2}\ny = {2, 1}\n\nprint( (x | y) - x - y)\n```",
        "image_link": "",
        "options": {
            "{}": False,
            "set()": True,
            "None": False,
            "{{}}": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\ndef operate( a:int, b:str, c:bool ) -> str | None:\n    return None if not c else a*b\n\noperate( **{'c':True, 'b':'False', 'a':2 } )\n```",
        "image_link": "",
        "options": {
            "'FalseFalse'": True,
            "None": False,
            "False": False,
            "NoneType": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nfns = square, double, triple, cube\n\na, *b, c = fns\n\nprint( b[0](b[-1](2)) )\n```",
        "image_link": "",
        "options": {
            "6": False,
            "8": False,
            "12": True,
            "24": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nprint( \n    (x := 10) << 1 | 0 | 1\n      )\n```",
        "image_link": "",
        "options": {
            "12": False,
            "20": False,
            "5": False,
            "21": True
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nprint( 1 ^ 2 ^ 3)\n```",
        "image_link": "",
        "options": {
            "1": False,
            "0": True,
            "6": False,
            "8": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nprint( int( True | False and True or False | True ) + int(1e4))\n```",
        "image_link": "",
        "options": {
            "10000": False,
            "10001": True,
            "1e5": False,
            "1e4": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nprint( type( id(1e9 / 1e4 ) ) )\n```",
        "image_link": "",
        "options": {
            "<class 'int'>": True,
            "<class 'float'>": False,
            "<class 'str'>": False,
            "<class 'bool'>": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nprint( 10_00e2 - ( [1e2, 1e4][x := (True if 1e2 > 1e4 else False)] ))\n```",
        "image_link": "",
        "options": {
            "100.0": False,
            "9990.0": False,
            "990.0": False,
            "99900.0": True
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\ny = set(( x := str(bool(str(None))) ).split() + x.split())\n\nprint(y)\n```",
        "image_link": "",
        "options": {
            "{'False'}": False,
            "{'True', 'True'}": False,
            "{'True'}": True,
            "set()": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nprint( (None if any( [None, None, None]) else 0)  ==  (None if all( [None, None, None]) else 0)  )\n```",
        "image_link": "",
        "options": {
            "False": False,
            "None": False,
            "NoneType": False,
            "True": True
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nnot all(\n    list(\n        map(\n            eval,\n            (\n                (str(None) + \" \")* int(1e5))\n            .split()\n            )\n        )\n    ) and bool(False)\n```",
        "image_link": "",
        "options": {
            "0": False,
            "True": False,
            "None": False,
            "False": True
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nfn = lambda x: 1 if x == 1 else fn(x-1)  \n\nprint( fn(4) << fn(1) )\n```",
        "image_link": "",
        "options": {
            "False": False,
            "True": False,
            "2": True,
            "infinite loop": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\ntry:\n    print(print)\nexcept:\n    print( x:= all( (True or False, True and False) ) )\nfinally:\n    print( x )\n```",
        "image_link": "",
        "options": {
            "<built-in function print>\nTrue": True,
            "SyntaxError": False,
            "True\nTrue": False,
            "<built-in function print>\n<built-in function print>\n": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nclass foo:\n    pass\nclass bar:\n    pass\n\nprint( id(foo) == id(bar) )\n```",
        "image_link": "",
        "options": {
            "0": False,
            "False": True,
            "True": False,
            "SyntaxError": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nsquare = lambda x: x**2\ndouble = lambda x: x*2\n\nx, y = square(2), double(2)\n\nprint( [square(3), double(3)][id(x) == id(y)] )\n```",
        "image_link": "",
        "options": {
            "3": False,
            "9": False,
            "12": False,
            "6": True
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\nx = 'Hi' 'This' 'is' 'a' 'hard' 'quiz'\ny = 'Hi', 'This', 'is', 'a', 'hard', 'quiz'\n\ntry:\n    print( x + y )\nexcept Exception:\n    print( type(x) == type(y)  )\n```",
        "image_link": "",
        "options": {
            "False": True,
            "True": False,
            "'HiThisisahardquizHiThisisahardquiz'": False,
            "TypeError": False
        }
    },
    {
        "question": "What will be the output of the following code?",
        "extra_content": "```python\na = (x for x in 'a''b''c')\n\nprint(\n    next(a),\n    next(a),\n    next(a)\n    )\n```",
        "image_link": "",
        "options": {
            "a b c": True,
            "a, b, c": False,
            "(a, b, c)": False,
            "a\nb\nc": False
        }
    }
]