import c4d
from c4d import gui


def main():
    # gui.MessageDialog('Hello World!')
    # doc = c4d.documents.GetActiveDocument()
    mats = doc.GetObjects()
    for mat in mats:
        print mat
        



if __name__=='__main__':
    main()
