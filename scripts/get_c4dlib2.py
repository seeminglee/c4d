import c4d

modlist = dict()
modlist[
    "c4d.bitmaps"c4d.bitmaps,
    c4d.documents,
    c4d.gui,
    c4d.internals,
    c4d.modules,
    c4d.plugins,
    c4d.storage,
    c4d.threading,
    c4d.utils
)


def main():
    with file('/Users/sml/Downloads/c4d_dir.py', 'w') as f:
        slist = []
        attlist = dir(c4d)
        for att in attlist:
            s = '%s = %s' % (att, getattr(c4d, att))
            slist.append(s)
        f.write('\n'.join(slist))
        f.close()
        
    for m in modlist:
        with file('/Users/sml/Downloads/

if __name__=='__main__':
    main()
