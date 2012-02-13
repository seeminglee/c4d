#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
debug_userdata

Writes the userdata of objects inside LSK_TestObj.py file to separate
data files for analysis

:copyleft: 2012 by See-ming Lee + SML Universe.
:license: MIT, see LICENSE for more details.
"""

class Decoder(object):
    """
    Helper class to decode C4D's internal enums into human-readable equivalent
    """
    C4DDict = dict(
        DESC = dict(
            DESC_=1000,
            DESC_ACCEPT=17,
            DESC_ALIGNLEFT=32,
            DESC_ANIMATE=10,
            DESC_ASKOBJECT=11,
            DESC_CHILDREN=4,
            DESC_CHILDS=4,
            DESC_COLUMNS=-1474809958,
            DESC_COLUMNSMATED=64,
            DESC_CREATEPORT=56,
            DESC_CUSTOMGUI=21,
            DESC_CYCLE=14,
            DESC_CYCLEICONS=36,
            DESC_CYCLESYMBOLS=37,
            DESC_DEFAULT=16,
            DESC_EDITABLE=26,
            DESC_EDITPORT=60,
            DESC_FITH=33,
            DESC_FORBID_INLINE_FOLDING=39,
            DESC_FORBID_SCALING=40,
            DESC_GROUPSCALEV=29,
            DESC_GUIOPEN=25,
            DESC_HIDE=15,
            DESC_IDENT=999,
            DESC_INPORT=50,
            DESC_ITERATOR=61,
            DESC_LAYOUTGROUP=23,
            DESC_LAYOUTVERSION=31,
            DESC_MATEDNOTEXT=63,
            DESC_MAX=6,
            DESC_MAXEX=8,
            DESC_MAXSLIDER=28,
            DESC_MIN=5,
            DESC_MINEX=7,
            DESC_MINSLIDER=27,
            DESC_MULTIPLE=54,
            DESC_NAME=1,
            DESC_NEEDCONNECTION=53,
            DESC_NEWLINE=34,
            DESC_NOGUISWITCH=66,
            DESC_NOTMOVABLE=59,
            DESC_OUTPORT=51,
            DESC_PARENTGROUP=13,
            DESC_PARENTID=20,
            DESC_PARENTMSG=62,
            DESC_PARENT_COLLAPSE=38,
            DESC_PORTONLY=55,
            DESC_PORTSMAX=58,
            DESC_PORTSMIN=57,
            DESC_REFUSE=19,
            DESC_REMOVEABLE=24,
            DESC_SCALEH=30,
            DESC_SEPARATORLINE=18,
            DESC_SHADERLINKFLAG=65,
            DESC_SHORT_NAME=2,
            DESC_STATICPORT=52,
            DESC_STEP=9,
            DESC_TEMPDESCID=998,
            DESC_TITLEBAR=35,
            DESC_UNIT=12,
            DESC_VERSION=3,
        ),
        
        DESC_ANIMATE = dict(
            DESC_ANIMATE_MIX = 2,
            DESC_ANIMATE_OFF = 0,
            DESC_ANIMATE_ON = 1,
        ),

        DESC_UNIT = dict(
            DESC_UNIT_DEGREE = 1717856114,
            DESC_UNIT_LONG = 1718382183,
            DESC_UNIT_METER = 1718445428,
            DESC_UNIT_PERCENT = 1718641524,
            DESC_UNIT_REAL = 1718773089,
            DESC_UNIT_TIME = 1717989997,
        ),

        DESC_VERSION = dict(
            DESC_VERSION_ALL = 3,
            DESC_VERSION_DEMO = 1,
            DESC_VERSION_XL = 2,
        ),

        DTYPE = dict(
            DTYPE_BASELISTLINK = 133,
            DTYPE_BOOL = 400006001,
            DTYPE_BUTTON = 8,
            DTYPE_CHILDREN = 0,
            DTYPE_CHILDS = 0,
            DTYPE_COLOR = 3,
            DTYPE_DYNAMIC = 10,
            DTYPE_FILENAME = 131,
            DTYPE_GROUP = 1,
            DTYPE_LONG = 15,
            DTYPE_MATRIX = 25,
            DTYPE_MULTIPLEDATA = 6,
            DTYPE_NONE = 0,
            DTYPE_NORMAL = 400006005,
            DTYPE_POPUP = 13,
            DTYPE_REAL = 19,
            DTYPE_SEPARATOR = 11,
            DTYPE_STATICTEXT = 12,
            DTYPE_STRING = 130,
            DTYPE_SUBCONTAINER = 5,
            DTYPE_TEXTURE = 7,
            DTYPE_TIME = 22,
            DTYPE_VECTOR = 23
        )
    )

    def __init__(self):
        pass


    def decode_desc(self, value):
        return self.decode('DESC', value)

    def decode_dtype(self, value):
        return self.decode('DTYPE', value)

    def decode(self, name, value):
        d = self.C4DDict[name]
        found = [k for k, v in d.items() if v == value]
        if not found:
            return None
        if len(found) == 1:
            return found[0]
        return 'Multi-found: {0}'.format(', '.join(found))



decoder = Decoder()
# ----------------------------------------------------------------------------
import c4d
import os

global doc
global op


def userdata(obj):
    out = list()
    out.append('=' * 70)
    out.append(str(obj))
    ud = obj.GetUserDataContainer()
    for id, bc in ud:
        out.append('-' * 70)
        out.append(str(bc))
        out.append('DescId: %s' % id)        
        # current value
        # TODO: Curretnly hacked
        s = str(id)
        strlist = s[1:-1].split(',')
        numlist = map(lambda s: eval(s.strip()), strlist)
        if numlist:
            dataid = numlist[0]
            dtype =  numlist[1]
            try:
                value = str(obj[c4d.ID_USERDATA, dataid])
            except AttributeError:
                value = '--- AttributeError ---'
            out.append('Id: {0:<5} DType: {1:<2}: {2:<30}'.format(
                    dataid, dtype, decoder.decode_dtype(dtype)))
            out.append('Value: {0}'.format(value))
        # Configuration
        items = list()
        for desc_id, data in bc:
            human_desc_id = decoder.decode('DESC', desc_id)
            if human_desc_id in ['DESC_UNIT', 'DESC_ANIMATE', 'DESC_VERSION']:
                data = decoder.decode(human_desc_id, data)
            items.append((desc_id, human_desc_id,
                          str(data).replace('\n', ' / ')))
        for item in sorted(items, key=lambda rows: rows[0]):
            out.append('{0:<10} {1:<30} {2}'.format(*item))
        # concat and return
    return '\n'.join(out)


def save_userdata(doc):
    container = doc.SearchObject('LSK-all')
    datapath = '/Users/sml/Dropbox/prj/python_projects/c4d/data'
    children_count = 0
    for obj in container.GetChildren():
        obj_name = obj[c4d.ID_BASELIST_NAME]
        fname = obj_name.replace(' ', '_') + '.txt'
        fpath = os.path.join(datapath, fname)
        data = userdata(obj)
        try:
            with open(fpath, 'w') as f:
                f.write(data)
                f.close()
                children_count += 1
        except IOError:
            print("IOError writing to {}. Skipping...".format(fpath))
    print("Output completed. {0} files written to {1}".format(children_count,
                                                              datapath))


def main():
    global doc
    save_userdata(doc)


if __name__ == '__main__':
    main()
        
    
    
