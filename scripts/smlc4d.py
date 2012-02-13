#!/usr/bin/env python
# encoding: utf-8
"""
smlc4d.py

Created by See-ming Lee on 2012-02-07.
Copyright (c) 2012 See-ming Lee. All rights reserved.
"""

import c4d

class UserDataAccessor(object):
	k = dict(
		DESC_ = 1000,
		DESC_ACCEPT = 17,
		DESC_ALIGNLEFT = 32,
		DESC_ANIMATE = 10,
		DESC_ANIMATE_MIX = 2,
		DESC_ANIMATE_OFF = 0,
		DESC_ANIMATE_ON = 1,
		DESC_ASKOBJECT = 11,
		DESC_CHILDREN = 4,
		DESC_CHILDS = 4,
		DESC_COLUMNS = -1474809958,
		DESC_COLUMNSMATED = 64,
		DESC_CREATEPORT = 56,
		DESC_CUSTOMGUI = 21,
		DESC_CYCLE = 14,
		DESC_CYCLEICONS = 36,
		DESC_CYCLESYMBOLS = 37,
		DESC_DEFAULT = 16,
		DESC_EDITABLE = 26,
		DESC_EDITPORT = 60,
		DESC_FITH = 33,
		DESC_FORBID_INLINE_FOLDING = 39,
		DESC_FORBID_SCALING = 40,
		DESC_GROUPSCALEV = 29,
		DESC_GUIOPEN = 25,
		DESC_HIDE = 15,
		DESC_IDENT = 999,
		DESC_INPORT = 50,
		DESC_ITERATOR = 61,
		DESC_LAYOUTGROUP = 23,
		DESC_LAYOUTVERSION = 31,
		DESC_MATEDNOTEXT = 63,
		DESC_MAX = 6,
		DESC_MAXEX = 8,
		DESC_MAXSLIDER = 28,
		DESC_MIN = 5,
		DESC_MINEX = 7,
		DESC_MINSLIDER = 27,
		DESC_MULTIPLE = 54,
		DESC_NAME = 1,
		DESC_NEEDCONNECTION = 53,
		DESC_NEWLINE = 34,
		DESC_NOGUISWITCH = 66,
		DESC_NOTMOVABLE = 59,
		DESC_OUTPORT = 51,
		DESC_PARENTGROUP = 13,
		DESC_PARENTID = 20,
		DESC_PARENTMSG = 62,
		DESC_PARENT_COLLAPSE = 38,
		DESC_PORTONLY = 55,
		DESC_PORTSMAX = 58,
		DESC_PORTSMIN = 57,
		DESC_REFUSE = 19,
		DESC_REMOVEABLE = 24,
		DESC_SCALEH = 30,
		DESC_SEPARATORLINE = 18,
		DESC_SHADERLINKFLAG = 65,
		DESC_SHORT_NAME = 2,
		DESC_STATICPORT = 52,
		DESC_STEP = 9,
		DESC_TEMPDESCID = 998,
		DESC_TITLEBAR = 35,
		DESC_UNIT = 12,
		DESC_UNIT_DEGREE = 1717856114,
		DESC_UNIT_LONG = 1718382183,
		DESC_UNIT_METER = 1718445428,
		DESC_UNIT_PERCENT = 1718641524,
		DESC_UNIT_REAL = 1718773089,
		DESC_UNIT_TIME = 1717989997,
		DESC_VERSION = 3,
		DESC_VERSION_ALL = 3,
		DESC_VERSION_DEMO = 1,
		DESC_VERSION_XL = 2
	)
	
	def __init__(self, obj=None):
		self.obj = obj
	
		

def print_userdata):
def print_userdata(obj):
	for id, bc in obj.GetUserDataContainer():
		# id is the DescID, bc is the container
		print bc[c4d.DESC_NAME], id

		# look at each DescLevel
		# this isn't necessary, just instructive
		for level in xrange(id.GetDepth()):
		    print "Level ", level, ": ", \
		          id[level].id, ",", \
		          id[level].dtype, ",", \
		          id[level].creator


def main():
    pass


if __name__ == '__main__':
    main()

