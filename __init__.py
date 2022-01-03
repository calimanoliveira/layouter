'''
Copyright (C) 2022 Edgard Caliman
edgard_caliman@yahoo.com.br

Created by Edgard Caliman and Team

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

bl_info = {
    "name": "LayouterTools",
    "description": "Tools of Layouter",
    "author": "Edgard Caliman",
    "version": (0, 0, 1),
    "blender": (3, 0, 0),
    "location": "View3D",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "Animation"}

#import bpy,bgl,blf
from bpy.utils import register_class, unregister_class
from .ui.panels import *
from .operators.ops_createmarkers import *
from .operators.ops_createcollections import *

from bpy.props import (StringProperty , BoolProperty , IntProperty , FloatProperty , EnumProperty , PointerProperty , )

from . import auto_load

auto_load.init()

class MyProperties(bpy.types.PropertyGroup):
    nameMarker : StringProperty(
        name="NameMarker" ,
        description="Name of Marker",
        default=""
    )
    nameCamera : StringProperty(
        name="NameCamera" ,
        description="Name of Camera",
        default=""
    )

#custom_1: bpy.props.FloatProperty(name="My Float")
classes = (
    LT_PT_CreateMarkers,
    LT_OT_CreateMarkers,
    LT_OT_CreateCollections,
    MyProperties
    #AB_OT_ValBreakdown_0,
)

def register():
    for cls in classes:
        register_class(cls)

    #bpy.utils.register_class(MyProperties)
    bpy.types.Scene.my_properties = bpy.props.PointerProperty(type=MyProperties)

    #bpy.utils.register_module(__name__)
#    register_all()

def unregister():
    for cls in reversed(classes):
        unregister_class(cls)
#    unregister_all()
    del bpy.types.Scene.my_properties

    #bpy.utils.unregister_class(MyProperties)
#    bpy.utils.unregister_module(__name__)
    #del bpy.types.Scene.my_properties

"""
#from . import auto_load

#auto_load.init()

#import bpy

# load and reload submodules
##################################

import importlib
#from . import developer_utils
#from animblend.ui.AnimTools import
#importlib.reload(developer_utils)
#modules = developer_utils.setup_addon_modules(__path__, __name__, "bpy" in locals())

# register
##################################

import traceback


def register():
    #auto_load.register()

#    from bpy.types import WindowManager as wm, Scene as scn
#    from bpy.props import PointerProperty
    from .ui.panels import register as register_ui
    #from .ui.panels import register
    from bpy.utils import register_class
    try:
        bpy.utils.register_module(__name__)
    except:
        traceback.print_exc()

    #print("Registered {} with {} modules".format(bl_info["name"], len(modules)))
    register_ui(register_class)

def unregister():
    from .ui.panels import unregister as unregister_ui
    #from .ui.panels import unregister
#    from bpy.utils import unregister_class
    try:
        bpy.utils.unregister_module(__name__)
    except:
        traceback.print_exc()
#    from bpy.types import WindowManager as wm, Scene as scn

    #print("Unregistered {}".format(bl_info["name"]))
    unregister_ui(unregister_class)
#    auto_load.unregister()

"""