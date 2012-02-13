"""
change_textag_mat.py

Change selected texture tags' materials by name.
Written specifically for speedy imports of FaceGen OBJ charaters.

Created by See-ming Lee on 2012-02-12.
License under CC-BY-SA Creative Commons Attribution Share-Alike 3.0
Copyright (c) 2012 See-ming Lee. Some rights reserved.
"""

import c4d
import inspect
import os


def modulepath(module):
    '''
    Return filepath for module named
    '''
    path = '/Users/sml/Dropbox/prj/python_projects/c4d/scripts_dev/inspect'
    pathlist = module.__name__.split('.')
    pathlist.insert(0, path)
    return os.path.join(*pathlist)


# ----------------------------------------------------------------------------
fmt_constants = '{name} = {value!r}'

fmt_function = '''
def {0}(*args, **kwargs):
    pass'''
def s_function(name):
    return fmt_function.format(name)

# ----------------------------------------------------------------------------

fmt_class = '''#!/usr/bin/env python
"""
{modulename}.{classname}

Auto-generated stub by inspect_c4d
"""

class {classname}(object):
    def __init__(self, *args, **kwargs):
{members}
{classes}
{methods}
'''
fmt_class_nomembers = '''
        pass'''
fmt_class_member = '''
        self.{name} = {value!r}'''
fmt_class_method = '''
    def {methodname}(self, *args, **kwargs):
        pass'''
fmt_class_class = '''
    class {classname}(object):
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
                classes.append(name)
            elif inspect.ismethod(value):
                methods.append(name)
            elif inspect.isfunction(value):
                functions.append(name)
            elif inspect.isbuiltin(value):
                builtins.append(name)
            elif inspect.ismethoddescriptor(value):
                methoddescs.append(name)
            else:
                others.append((name, value))

    if not others:
        members = [fmt_class_nomembers]
    else:
        members = [fmt_class_member.format(name=n, value=v) for n, v in others]

    s_classes = [fmt_class_class.format(classname=item) \
                 for item in classes]

    s_methods = [fmt_class_method.format(methodname=item) \
                 for item in (methods + functions + builtins + methoddescs)]

    out = fmt_class.format(
        modulename = module.__name__,
        classname = classname,
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
    others = []

    for name, value in inspect.getmembers(module):
        if inspect.ismodule(value):
            modules.append(name)
        elif inspect.isbuiltin(value):
            functions.append(name)
        elif inspect.isclass(value):
            classes.append((name, value))
        else:
            others.append((name, value))

    out = []
    if modules:
        out.append('# Modules-----------')
        out.append("'"*3)
        for m in modules:
            out.append(m)
            evalm = '{0}.{1}'.format(module.__name__, m)
            evalm = eval(evalm)
            write_module(evalm) # ------------------------------------WRITE
        out.append("'"*3)

    if functions:      
        out.append('# Builtin Functions----------')
        for name in functions:
            out.append(s_function(name))

    if classes:
        out.append('# Classes------------')
        out.append("'"*3)
        for name, value in classes:
            out.append(name)
            write_class(module, name, value) # -----------------------WRITE
        out.append("'"*3)
            
    if others:
        out.append('# Others-------------')
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
