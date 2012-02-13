

import c4d
import os

global doc
global op


def main():
    global doc

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


def userdata(obj):
    out = list()
    out.append('=' * 70)
    out.append(str(obj))
    ud = obj.GetUserDataContainer()
    for id, bc in ud:
        out.append('-' * 70)
        out.append(str(bc))
        items = list()
        for desc_id, data in bc:
            items.append((desc_id, desc_id_helper.decode(desc_id), str(data)))
        for item in sorted(items, key=lambda rows: rows[0]):
            out.append('{0:<10} {1:<30} {2}'.format(*item))
    return '\n'.join(out)

        
        
    
    
