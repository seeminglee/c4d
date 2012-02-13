"""
facegen-obj-helper.py

Utilities for FaceGen OBJ files loading and character setup.

Created by See-ming Lee on 2012-02-12.
License under CC-BY-SA Creative Commons Attribution Share-Alike 3.0
Copyright (c) 2012 See-ming Lee. Some rights reserved.
"""
import c4d
import os
import signal

class FaceGenFileHelperError(Exception):
    pass


class FaceGenFileLoader(object):
    sections = (
        'base',
        'textures',
        'expressions',
        'modifiers',
        'phonemes',
        )

    fmts = dict(
        base='{name}.obj',
        textures='{name}_{type}.jpg',
        expressions='{name}_Expression{type}.obj',
        modifiers='{name}_Modifier{type}.obj',
        phonemes='{name}_Phoneme{type}.obj',
        )

    types = dict(
        textures=(
            'eyeL_hi',
            'eyeR_hi',
            'skin_hi',
            'sock',
            'teethLower',
            'teethUpper',
            'tongue',
            ),

        expressions=(
            'Anger',
            'Disgust',
            'Fear',
            'Sad',
            'SmileClosed',
            'SmileOpen',
            'Surprise',
            ),

        modifiers=(
            'BlinkLeft',
            'BlinkRight',
            'BrowDownLeft',
            'BrowDownRight',
            'BrowInLeft',
            'BrowInRight',
            'BrowUpLeft',
            'BrowUpRight',
            'EarsOut',
            'EpicanthicFold',
            'EyeSquintLeft',
            'EyeSquintRight',
            'LookDown',
            'LookLeft',
            'LookRight',
            'LookUp',
            ),

        phonemes=(
            'aah',
            'B,M,P',
            'bigaah',
            'ch,J,sh',
            'D,S,T',
            'ee',
            'eh',
            'F,V',
            'i',
            'K',
            'N',
            'oh',
            'ooh,Q',
            'R',
            'th',
            'W',
            ),
        )


    def __init__(self, doc, dirpath, name, objname=None):
        """
        setup common attributes:
        doc:      document to load files in
        dirpath:  full path to the directory containing the files
        name:     common prefix of filenames, excluding the underscore
                usually the name of the character
        objname:  optional name of the character object to be created inside the doc
                if not specified, name will be used in document as well
        """
        self.doc = doc
        self.name = name
        self.dirpath = os.path.abspath(dirpath)
        self.objname = self.name
        if objname is not None:
            self.objname = objname
        self.init_filepaths()


    def init_filepaths(self):
        """
        Setup list of files to be loaded
        """
        if not os.path.isdir(self.dirpath) or\
           not os.path.exists(self.dirpath):
            raise FaceGenFileHelperError(
                "Path does not exist: {0}".format(self.dirpath))

        self.filepaths = dict()
        for section in self.sections:
            files = []
            if section == 'base':
                files.append(self.fpath(
                    self.fmts['base'].format(name=self.name)))
            else:
                for sectype in self.types[section]:
                    files.append(self.fpath(
                        self.fmts[section].format(name=self.name,
                                                  type=sectype)))
            self.filepaths[section] = files


    def fpath(self, fname):
        """
        Return full absolute path to supplied filename
        """
        return os.path.join(self.dirpath, fname)


    def check_files(self):
        """
        Print full paths to the files to load and verify existence
        """
        err = []
        for section in self.filepaths:
            for fname in self.filepaths[section]:
                try:
                    with open(fname, 'rb') as f:
                        f.read()
                        f.close()
                        print('{0}... OK'.format(fname))
                except IOError:
                    err.append('IOError: {0}'.format(fname))
                except:
                    err.append('Unknown Error: {0}'.format(fname))

        if not err:
            print 'Verification complete. PASS'
            return True
        else:
            print('We found {0} errors:'.format(len(err)))
            for e in err:
                print e
            return False


    def file_load_signal_handler(self, signum, frame):
        print 'Signal handler called with signal', signum
        raise IOError('Failed loading document')


    def start_loading(self):
        """
        Merge document with list of files to be loaded
        Create a hierachical list of objects inside object manager
        """
        err = []

        # create topmost container null
        self.doc.StartUndo()

        obj = c4d.BaseObject(c4d.Onull)
        obj.SetName(self.objname)
        self.doc.InsertObject(obj)
        self.doc.AddUndo(c4d.UNDOTYPE_NEW, obj)
        self.doc.EndUndo()
        c4d.EventAdd()
        self.base_obj = obj


        # with self.doc.InsertObject(c4d.BaseObject(c4d.Onull)) as base_obj:
        # 	base_obj.SetName(self.objname)
        # 	self.base_obj = base_obj

        #		self.update_highest_objects()

        loadflags = c4d.SCENEFILTER_0

        loadflags |= c4d.SCENEFILTER_OBJECTS
        loadflags |= c4d.SCENEFILTER_MATERIALS
        loadflags |= c4d.SCENEFILTER_DIALOGSALLOWED
        loadflags |= c4d.SCENEFILTER_PROGRESSALLOWED
        loadflags |= c4d.SCENEFILTER_MERGESCENE

        for section in ['base', 'expressions']:
            for fname in self.filepaths[section]:
                print('Loading {0}'.format(fname))

                # signal.signal(signal.SIGALRM, self.file_load_signal_handler)
                # signal.alarm(5)

                # c4d.documents.LoadFile(fname)

            loaded_doc = c4d.documents.LoadDocument(fname, )

            # disable alarm if reached

            # signal.alarm(0)

            # if success:
            if loaded_doc:
                # print('file merged successfully.')
                print('doc loaded')
                doc = c4d.documents.GetActiveDocument()
                # while doc is not None:
                print(doc)


            else:
                print('file load failed')
            # if loaded_doc is None:
            # 				print("WARNING: loaded_doc is None")
            #
            # 			if loaded_doc is not None:
            # 				self.doc.StartUndo()
            #
            # 				obj = loaded_doc.GetFirstObject()
            #
            # 				while obj is not None:
            # 					self.doc.StartUndo()
            # 					obj.InsertUnder(self.base_obj)
            # 					self.doc.AddUndo(c4d.UNDOTYPE_NEW, obj)
            # 					self.doc.EndUndo()
            # 					c4d.EventAdd()
            # 					obj = obj.GetNext()
            #
            # 				loaded_doc.Flush()


    def update_highest_objects(self):
        self.highest_objs = self.doc.GetObjects()


    def new_objects(self):
        """
          Return list of objects which just got loaded
          by comparing last recorded Doc.GetObjects()
          """
        new_objs = [obj for obj in self.doc.GetObjects() if
                    obj not in self.highest_objs]

        for o in new_objs:
            p = o.GetUp()
            while p not in self.highest_objs:
                new_objs.append(p)
                p = p.GetUp()

        return new_objs


def change_materials(doc, in_fmt, out_fmt, count):
    # conversion dictionary
    out_names = dict()
    out_mats = dict()
    for i in xrange(count):
        in_name = in_fmt.format(i)
        out_name = out_fmt.format(i)
        out_mat = doc.SearchMaterial(out_name)
        out_names[in_name] = out_name
        out_mats[in_name] = out_mat

    for t in doc.GetActiveTags():
        if t.GetMaterial:
            mat_name = t.GetMaterial().GetName()
            print mat_name
            if mat_name in out_mats.keys():
                t.SetMaterial(out_mats[mat_name])


def main():
    doc = c4d.documents.GetActiveDocument()
    loader = FaceGenFileLoader(doc, '/Volumes/Scratch/OctaneRender/FaceGen',
                               name='euro-002', objname='Euro2Char')
    # loader.check_files()
    loader.start_loading()


if __name__ == '__main__':
    main()
    
