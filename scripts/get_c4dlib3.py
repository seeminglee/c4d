import c4d
from c4d import gui
from c4d import bitmaps
from c4d import documents
from c4d import gui
from c4d import modules
from c4d import plugins
from c4d import storage
from c4d import threading
from c4d import utils
#Welcome to the world of Python
import os
import types


fmt_functions = '''
def {0}(*args, **kwargs):
    pass
'''

fmt_classes = '''
class {0}(object):
    def __init__(self, *args, **kwargs):
        pass
'''


def write_modules():
    for m in ['c4d','c4d.bitmaps', 'c4d.documents', 'c4d.gui', 'c4d.modules', 
            'c4d.plugins','c4d.storage','c4d.threading','c4d.utils']:
        mod_stubs('/Users/sml/Dropbox/prj/python_projects/c4d/scripts_dev', m)
        
        
 
def mod_stubs(path, module_fullname):
    filename = module_fullname.split('.')
    filename[-1] = filename[-1] + '.py'
    filename.insert(0, path)
    filepath = os.path.join(*filename)
    print(filepath)

    evaled_module = eval(module_fullname)
    with file(filepath, 'w') as f:
        slist = ['# simple values'+'-'*50]
        deflist = ['# functions'+'-'*50]
        classlist = ['# classes'+'-'*50]
        modulelist = ['# modules'+'-'*50]
        attlist = dir(evaled_module)
        for att in attlist:

            if att.startswith('__'):
                continue
            
            value = getattr(evaled_module, att)

            if type(value) is types.BuiltinFunctionType:
                s = fmt_functions.format(att)
                deflist.append(s)
            elif type(value) is types.ModuleType:
                # ignore modules writing for now
                s = '%s = %s' % (att, value)
                slist.append(s)
            elif type(value) is types.ClassType or type(value) == type(type):
                # a class:
                s = fmt_classes.format(att)
                classlist.append(s)
            else:
                s = '%s = %s' % (att, value) 
                slist.append(s)                 
        result = modulelist + classlist + deflist + slist
        f.write('\n'.join(result))
        f.close()  

def main():
    write_modules()
    

if __name__=='__main__':
    main()
