import c4d

frame = 0



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


def setText(objName, text):
    global doc
    obj = doc.SearchObject(objName)
    obj[c4d.PRIM_TEXT_TEXT] = '%s' % text
    
# visibility index of C4D is weird: it's reversed.
def setVis(obj, vis):
    if vis:
        obj[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 0
        obj[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = 0
    else:
        obj[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 1
        obj[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = 1
        
        
def main():
    global doc
    global frame
    global lsk_controllers
    global TestObj
    global TestObjsClone
    
    frame = doc.GetTime().GetFrame(doc.GetFps())
    
    # setup
    if frame == 0:
        container = doc.SearchObject('LSK-all')
        lsk_controllers = [c for c in container.GetChildren()]
        
        # Remove previous clones, if any
        itermax = 10
        while itermax > 0 and doc.SearchObject('TestObjsClone'):
            itermax += 1
            o = doc.SearchObject('TestObjsClone').Remove()
        
        # Create clones and set visibility
        TestObjs = doc.SearchObject('TestObjs')
        TestObjsClone = TestObjs.GetClone()
        TestObjsClone[c4d.ID_BASELIST_NAME] = 'TestObjsClone'
        setVis(TestObjs, False)
        setVis(TestObjsClone, True)
        
            
    # controller visible if id = frame % 20
    active_id = frame % len(lsk_controllers)

    # remove previous clone
    # TestObjsClone.Remove()
    oid=0
    active_o=None
    for o in lsk_controllers:
        if oid == active_id:
            setVis(o, True)
            TestObjsClone.InsertUnder(o)
            
            # material name
            mat_name = o[c4d.ID_BASELIST_NAME].replace(' Controllers', '')
            setText('MoTextCaption', mat_name)
            setText('MoTextCaption.1', '') 
            # userdata
            # udid = None
            # disp_height = None
            # disp_height_default = None
            # ud = o.GetUserDataContainer()
            # value = 0
            # correct_field = False
            # for id, bc in ud:
            #     items = list()
            #     for desc_id, data in bc:
            #         human_desc_id = decoder.decode('DESC', desc_id)
            #         if human_desc_id == 'DESC_NAME':
            #             if data == 'Displacement Height':
            #                 correct_field = True
            #         if correct_field:
            #             if human_desc_id == 'DESC_DEFAULT':
            #                 disp_height_value = data
            #                 udid = id
            #                 break
            # s = str(udid)
            # strlist = s[1:-1].split(',')
            # numlist = map(lambda s: eval(s.strip()), strlist)
            # if numlist:
            #     dataid = numlist[0]
            #     try:
            #         disp_height = o[c4d.ID_USERDATA, dataid]
            #     except AttributeError:
            #         disp_height = '--- AttributeError ---'
            # setText('MoTextCaption.1', 
            #         'Displacement Height / Default = %s / %s' % (
            #             value, 
            #             str(disp_height_default)))
                        
            # for id, bc in o.GetUserDataContainer():
            #         # id is the DescID, bc is the container
            #         print bc[c4d.DESC_NAME], id

            #         # look at each DescLevel
            #         # this isn't necessary, just instructive
            #         for level in xrange(id.GetDepth()):
            #             print "Level ", level, ": ", \
            #                   id[level].id, ",", \
            #                   id[level].dtype, ",", \
            #                   id[level].creator

        else:
            setVis(o, False)
        oid += 1

    
    c4d.EventAdd()


if __name__ == '__main__':
    main()
    
    
