import bpy

from bpy.types import (Panel ,
                       Operator ,
                       AddonPreferences ,
                       PropertyGroup ,
                       Menu ,
                       UIList ,
                       )

from bpy.props import (StringProperty , BoolProperty , IntProperty , FloatProperty , EnumProperty , PointerProperty , )


# from bpy.types import (Panel,Operator,AddonPreferences,PropertyGroup,)


# Simple Operator


class animtools_Operator(bpy.types.Operator):
    bl_idname = 'object.animtools'
    bl_label = "AnimTools"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(cls , context):
        return True

    def execute(self , context):
        return {'FINISHED'}


class TranslateWrapper(bpy.types.Operator):
    bl_idname = "animblend.translate_wrapper"
    bl_label = "animblend translate"
    bl_description = ""
    bl_options = {"REGISTER" , "UNDO"}

    @classmethod
    def poll(cls , context):
        return True

    def execute(self , context):
        # call translate but constraining the axis with the lockY option
        bpy.ops.transform.translate(
            "INVOKE_DEFAULT" ,
            constraint_axis=(False , context.scene.my_properties.LocY , False)
        )
        return {"FINISHED"}


# prache pra fazer um botao:
# class LocY(bpy.types.Operator):
#    bl_idname = "animtools.loc_Y"
#    bl_label = "mover cubo(texto do botao)"
#    bl_options = {'REGISTER', 'UNDO'}
#    LocY = BoolProperty(
#            name="LocY",
#            description="Property is Loc in Y",
#            default = True
#        )

# a funçao do botao
#    def execute(self, context):

#        scene = context.scene
#        myProperties = scene.my_properties
#        bpy.context.window_manager.keyconfigs['Blender'].keymaps['Graph Editor'].keymap_items[
#            'transform.translate'].properties['constraint_axis'] = [False,not(scene.my_properties.LocY),False]
#        bpy.context.window_manager.keyconfigs['Blender'].keymaps['Graph Editor'].keymap_items[
#            'transform.translate'].properties.constraint_axis.update()
#        bpy.context.window_manager.keyconfigs['Blender'].keymaps['Graph Editor'].keymap_items[
#            'transform.translate'].active = False
#        bpy.context.window_manager.keyconfigs['Blender'].keymaps['Graph Editor'].keymap_items[
#            'transform.translate'].active = True


#        scene.my_properties.LocY=not(scene.my_properties.LocY)

#        return {"FINISHED"}  # dizer ao blender que acabou

class curveLocY(bpy.types.Operator):
    bl_idname = "animtools.curve_LocY"
    bl_label = "Curve LocY"
    bl_options = {'REGISTER' , 'UNDO'}

    #    LocY = BoolProperty(
    #            name="LocY",
    #            description="Property is Loc in Y",
    #            default = True
    #        )

    @classmethod
    def poll(cls , context):
        return True

    def execute(self , context):
        layout = self.layout
        scene = context.scene
        myProperties = scene.my_properties
        layout.prop(myProperties , "LocY")
        print("Passou por aqui")
        bpy.ops.transform.translate(constraint_axis=(False , True , False))
        return {'FINISHED'}


##===================================================
##================= Panel / UI ======================
##===================================================

# Menu Panel
'''
class animtools_Panel(bpy.types.Panel):
    bl_idname = "view3d.AnimTools"
    bl_label = "AnimTools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_category = "Animation"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.animtools", text="animtools")
        layout.operator("animtools.loc_Y",text="Move")
        layout.operator("animtools.mover_objeto",text="Move")
'''


class animtools_GE_Panel(bpy.types.Panel):
    bl_idname = 'object.animtools_GE_Panel'
    bl_label = "Graph Editor Panel"
    bl_space_type = "GRAPH_EDITOR"
    bl_region_type = "UI"
    bl_category = "Animation"

    # bl_options = {'REGISTER'}

    def draw(self , context):
        layout = self.layout
        scene = context.scene
        my_Properties = scene.my_properties
        layout.operator("animtools.curveLocY" , text="LocY")
        # layout.operator("render.opengl", text="Still", icon='RENDER_STILL')
        #        layout.operator("object.animtools", text="Loc Y")
        #        layout.operator("animtools.mover_objeto",text="Move")
        #        layout.operator("animblend.translate_wrapper",text="Move")

        layout.prop(my_Properties , "LocY")


# =====================================
#  Class of properties
# =====================================

class MyProperties(bpy.types.PropertyGroup):
    LocY = BoolProperty(
        name="LocY" ,
        description="Property is Loc in Y",
        default=True
    )


addon_keymap = []


# Register/Unregister

def register():
    bpy.utils.register_class(MyProperties)
    bpy.types.Scene.my_properties = bpy.props.CollectionProperty(type=MyProperties)

    keymap_config = bpy.context.window_manager.keyconfigs.addon
    if keymap_config:
        km = keymap_config.keymaps.new(name="Graph Editor" , space_type="GRAPH_EDITOR")
        kmi = km.keymap_items.new("animblend.translate_wrapper" , "G" , "PRESS")
        addon_keymap.append((km , kmi))

#    if keymap_config:
#        km = keymap_config.keymaps.new(name="Graph Editor" , space_type="GRAPH_EDITOR")
#        kmi = km.keymap_items.new("animblend.translate_wrapper" , "SELECTMOUSE" , "PRESS")
#        addon_keymap.append((km , kmi))

    bpy.utils.register_module(__name__)


def unregister():
    del bpy.types.Scene.my_properties

    bpy.utils.unregister_class(MyProperties)

    bpy.utils.unregister_module(__name__)
    del bpy.types.Scene.my_properties

    for km , kmi in addon_keymap:
        km.keymap_items.remove(kmi)
    addon_keymap.clear()


if __name__ == "__main__":
    register()


