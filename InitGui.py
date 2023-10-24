import os
import shutil
import FreeCAD as App

class Iconpack (Workbench):

    MenuText = "MisterMaker Icon pack"
    ToolTip = "This installs the MisterMaker Icon pack for the Icon theme addon."
    Icon = """paste here the contents of a 16x16 xpm icon"""

    def Initialize(self):
        """This function is executed when the workbench is first activated.
        It is executed once in a FreeCAD session followed by the Activated function.
        """
    def Activated(self):
        """This function is executed whenever the workbench is activated"""
        destination = (App.getUserAppDataDir() + "Gui" + os.path.sep + "Icons" + os.path.sep)
        source = "MM_Freecad_original_colors/"
        endlocation = (App.getUserAppDataDir() + "Gui" + os.path.sep + "Icons" + os.path.sep + "MM_Freecad_original_colors")
        if os.path.exists(endlocation):
            print("Icon pack MM already installed.")
        else:
            dest = shutil.copy(source, destination)
            print(dest)
            print("You can now find the icons in the Icon theme workbench.")
        return

    def Deactivated(self):
        """This function is executed whenever the workbench is deactivated"""
        endlocation = (App.getUserAppDataDir() + "Gui" + os.path.sep + "Icons" + os.path.sep + "MM_Freecad_original_colors")
        dest = shutil.rmtree(endlocation)
        print(dest)
        print("Icons are removed from the Icon theme workbench, please reboot and edit your Icon theme settings.")
        return

    def GetClassName(self):
        # This function is mandatory if this is a full Python workbench
        # This is not a template, the returned string should be exactly "Gui::PythonWorkbench"
        return "Gui::PythonWorkbench"

Gui.addWorkbench(Iconpack())