import c4d
from c4d import gui


def main():
    # gui.MessageDialog('Hello World!')
    # doc = c4d.documents.GetActiveDocument()
    objs = doc.GetObjects()
    for obj in objs:
        print obj
    
    all = doc.SearchObject('LSK-all')
    for o in all.GetObjects():
        print o
        
        



if __name__=='__main__':
    main()