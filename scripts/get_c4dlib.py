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


def main():
    for m in ['bitmaps', 'documents', 'gui', 'modules', 'plugins','storage','threading','utils']:
        filename = '/Users/sml/Dropbox/prj/python_projects/c4d/scripts_dev/c4d/{0}.py'.format(m)
        modulename = 'c4d.{0}'.format(m)
        moduleeval = eval(modulename)
        with file(filename, 'a') as f:
            slist = []
            attlist = dir(moduleeval)
            for att in attlist:
                s = '%s = %s' % (att, getattr(moduleeval, att))
                slist.append(s)
            f.write('\n'.join(slist))
            f.close()

if __name__=='__main__':
    main()
