"""
change_textag_mat.py

Change selected texture tags' materials by name.
Written specifically for speedy imports of FaceGen OBJ charaters.

Created by See-ming Lee on 2012-02-12.
License under CC-BY-SA Creative Commons Attribution Share-Alike 3.0
Copyright (c) 2012 See-ming Lee. Some rights reserved.
"""
import c4d

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
	change_materials(doc, 'Texture{0}', 'Euro2.Tex{0}', 7)


if __name__ == '__main__':
	main()
    
