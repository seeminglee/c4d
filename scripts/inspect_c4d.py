"""
inspect_c4d.py

Inspect the Python environment in Cinema 4D (c4d) and automatically generate
Python files meant for code completions for IDEs such as PyCharm, etc. 

How to use:
1. Change the variable START_PATH (first line of code before the imports)
to a real path on your system.
2. Load the script inside C4D's Python Manager
3. Hit Execute

The script should have written a ton of files under the designated path you
have set above. Now if you designate this path as a 'source root' in IDEs
such as PyCharm, auto-completions shoud work automagically.

Created by See-ming Lee on 2012-02-12.
License under CC-BY-SA Creative Commons Attribution Share-Alike 3.0
Copyright (c) 2012 See-ming Lee, Crazyisgood. Some rights reserved.
"""

START_PATH = '/Users/sml/Dropbox/prj/python_projects/c4d/scripts_dev'

# ----------------------------------------------------------------------------
import c4d
import inspect
import os


def modulepath(module):
    '''
    Return filepath for module named
    '''
    path = START_PATH
    pathlist = module.__name__.split('.')
    pathlist.insert(0, path)
    return os.path.join(*pathlist)


# ----------------------------------------------------------------------------
fmt_constants = '{name} = {value!r}'

fmt_function = '''
def {name}(*args, **kwargs):
    """
    {docstring}
    """
    pass'''
def s_function(name, docstring):
    return fmt_function.format(name=name, docstring=docstring)

# ----------------------------------------------------------------------------

fmt_class = '''#!/usr/bin/env python
"""
{modulename}.{classname}

Important: these are not real files. They are automatically generated to
ease code completion only.
"""

class {classname}(object):
    """
    {docstring}
    """
    def __init__(self, *args, **kwargs):
{members}
{classes}
{methods}
'''
fmt_class_nomembers = '        pass'
#fmt_class_member    = '        self.{name} = {value!r}'
fmt_class_member    = '        self.{name} = None'
fmt_class_method = '''
    def {methodname}(self, *args, **kwargs):
        """
        {docstring}
        """
        pass'''
fmt_class_class = '''
    class {classname}(object):
        """
        {docstring}
        """
        def __init__(self, *args, **kwargs):
            pass
'''

def isprivateobj(name):
    return name.startswith('__') and name.endswith('__')

def write_class(module, classname, classvalue):

    classes = []
    methods = []
    builtins = []
    functions = []
    methoddescs = []
    others = []

    theclass = '{0}.{1}'.format(module.__name__, classname)
    theclass = eval(theclass)

    for name, value in inspect.getmembers(theclass):
        if not isprivateobj(name):
            if inspect.isclass(value):
                classes.append((name, value))
            elif inspect.ismethod(value):
                methods.append((name, value))
            elif inspect.isfunction(value):
                functions.append((name, value))
            elif inspect.isbuiltin(value):
                builtins.append((name, value))
            elif inspect.ismethoddescriptor(value):
                methoddescs.append((name, value))
            else:
                others.append((name, value))

    if not others:
        members = [fmt_class_nomembers]
    else:
        members = [fmt_class_member.format(name=n, value=v) for n, v in others]

    s_classes = [fmt_class_class.format(classname=name, docstring=value.__doc__) \
                 for name, value in classes]

    s_methods = [fmt_class_method.format(methodname=name, docstring=value.__doc__) \
                 for name, value in (methods + functions + builtins + methoddescs)]

    out = fmt_class.format(
        modulename = module.__name__,
        classname = classname,
        docstring = theclass.__doc__,
        members = '\n'.join(members),
        classes = '\n'.join(s_classes),
        methods = '\n'.join(s_methods)                     
    )

    mpath = modulepath(module)
    if not os.path.exists(mpath):
        os.makedirs(mpath)
    cfile = os.path.join(mpath, classname + '.py')

    try:
        with open(cfile, 'w') as f:
            f.write(out)
            f.close()
            print(cfile)
    except IOError:
        print "IOError"

# ----------------------------------------------------------------------------


def write_module(module):

    modules = []
    functions = []
    classes = []
    constants = []
    others = []

    for name, value in inspect.getmembers(module):
        if inspect.ismodule(value):
            modules.append(name)
        elif inspect.isbuiltin(value):
            functions.append((name, value))
        elif inspect.isclass(value):
            classes.append((name, value))
        else:
            if name.upper() == name:
                constants.append((name, value))
            else:
                others.append((name, value))

    out = []
    if modules:
        out.append('# {0:-<60}'.format('Modules '))
        out.append("'"*3)
        for m in modules:
            out.append(m)
            evalm = '{0}.{1}'.format(module.__name__, m)
            evalm = eval(evalm)
            write_module(evalm) # ------------------------------------WRITE
        out.append("'"*3)

    if functions:      
        out.append('# {0:-<60}'.format('Functions '))
        for name, value in functions:
            out.append(s_function(name, value.__doc__))

    if classes:
        out.append('# {0:-<60}'.format('Classes '))
        out.append("'"*3)
        for name, value in classes:
            out.append(name)
            write_class(module, name, value) # -----------------------WRITE
        out.append("'"*3)
    
    if constants:
        out.append('# {0:-<60}'.format('Constants '))
        for name, value in constants:
            out.append(fmt_constants.format(name=name, value=value))
                    
    if others:
        out.append('# {0:-<60}'.format('Everything else '))
        for name, value in others:
            out.append(fmt_constants.format(name=name, value=value))


    mpath = modulepath(module)
    if not os.path.exists(mpath):
        os.makedirs(mpath)
    mfile = os.path.join(mpath, '__init__.py')

    try:
        with open(mfile, 'w') as f:
            f.write('\n'.join(out))
            f.close()
            print(mfile)
    except IOError:
        print "IOError"

    
def main():
    c4d.CallCommand(13957) # Clear Console
    c4d.EventAdd()
    write_module(c4d)
    
if __name__=='__main__':
    main()
