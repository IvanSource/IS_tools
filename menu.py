import sys
import nuke
import IS_backdrop


print 'Loading Lab Tools...' #needed?
menubar = nuke.menu("Nuke")

# Custom Lab Tools
toolbar = nuke.toolbar("Nodes")
#define variable and icon for menu01
menu01 = toolbar.addMenu("CUSTOM MENU 1", icon="ICON NAME HERE.png")

#gizmos that needs to be part of that menu
menu01.addCommand("eFibonacciGlow", "nuke.createNode(\"eFibonacciGlow\")", icon="eFibonacciGlow.png")
menu01.addCommand("CUSTOMGIZMO", "nuke.createNode(\"CUSTOMGIZMO\")", icon="IMAGE NAME HERE.png")
menu01.addCommand("CUSTOMGIZMO", "nuke.createNode(\"CUSTOMGIZMO\")", icon="IMAGE NAME HERE.png")


##CUSTOM STICKYNOTES COLOUR
def IS_StickyNotes():
    nuke.knobDefault("StickyNote.tile_color", "4294967295.0")

IS_StickyNotes()

##CUSTOM BACKDROP COLOUR
def IS_Backdrop():
    nuke.knobDefault("autoBackdrop.tile_color", "555819519.0")

IS_Backdrop()

#Set Default format to 1080HD
nuke.knobDefault("Root.format", "HD_1080")

#TCL show Frame offset
def IS_timeOffset():
  x = nuke.thisNode()
  if x != None:
    label = x['label'].value()
    x['label'].setValue('input()')

IS_timeOffset()



