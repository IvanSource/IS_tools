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


##CUSTOM BACKDROP COLOUR
def IS_backdrop():
    import nukescripts
    import colorsys

    # create backdrop
    node = nukescripts.autoBackdrop()

    # TileColor to HSV
    originalTileColor = node.knob('tile_color').value()
    originalRGB = [(0xFF & originalTileColor >> i) / 255.0 for i in [24, 16, 8]]
    originalHSV = colorsys.rgb_to_hsv(originalRGB[0], originalRGB[1], originalRGB[2])

    # Custom Color
    hue = originalHSV[0] * 0
    saturation = originalHSV[1] * 0
    value = originalHSV[2] * 0 + 0.13

    # HSV to TileColor
    newHSV = [hue, saturation, value]
    newRGB = colorsys.hsv_to_rgb(newHSV[0], newHSV[1], newHSV[2])
    newTileColor = int('%02x%02x%02x%02x' % (newRGB[0] * 255, newRGB[1] * 255, newRGB[2] * 255, 255), 16)

    # Replace tile_color with NetTileColor
    node.knob('tile_color').setValue(newTileColor)

nuke.menu('Nodes').addCommand('Other/Backdrop', IS_backdrop, icon='Backdrop.png')
nuke.menu("Nodes").addCommand("Other/Backdrop", "IS_backdrop()", "Alt+b")




