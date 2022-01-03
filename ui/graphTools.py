# -*- coding: utf-8 -*-
import bpy
from bpy.props import (StringProperty ,
                       BoolProperty ,
                       IntProperty ,
                       FloatProperty ,
                       EnumProperty ,
                       PointerProperty ,
                       )

from bpy.types import (Panel ,
                       Operator ,
                       AddonPreferences ,
                       PropertyGroup ,
                       )




#===============================================================================
'''
Operators
'''







#===============================================================================
'''
Panels
'''





#===============================================================================
'''
Classes
'''



#===============================================================================
'''
Properties
'''


#===============================================================================
'''
Register and Unregister
'''
addon_keymap = []


def register():
    # bpy.utils.rester_class(TweenMachinePanel)

    keymap_config = bpy.context.window_manager.keyconfigs.addon
    if keymap_config:
        km = keymap_config.keymaps.new(name="Graph Editor" , space_type="GRAPH_EDITOR")
        kmi = km.keymap_items.new("animblend.translate_wrapper" , "G" , "PRESS")
        addon_keymap.append((km , kmi))

    bpy.types.Scene.minha_propriedade = PointerProperty(type=MinhaPropriedade)
    bpy.types.Scene.prop_curves= PointerProperty(type=PropCurves)
    #bpy.utils.register_module(__name__)


def unregister():
    # bpy.utils.unregister_class(TweenMachinePanel)
    #bpy.utils.unregister_module(__name__)
    del bpy.types.Scene.minha_propriedade
    del bpy.types.Scene.prop_curves

    for km , kmi in addon_keymap:
        km.keymap_items.remove(kmi)
    addon_keymap.clear()


if __name__ == "__main__":
    register()
