import bpy


from bpy.types import (Panel,
                       Operator,
                       AddonPreferences,
                       PropertyGroup,
                       Menu,
                       UIList,
                       )

#from bpy.props import (
#    StringProperty,
#    IntProperty,
#    EnumProperty,
#    CollectionProperty,
#)


class TweenMachinePanel(bpy.types.Panel):
    bl_label = "TweenMachine"
    bl_category = "AnimBlend"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_idname = "pn_tweenmachine"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        row = col.row()

        rd = context.scene.render
        view = context.space_data
        scene = context.scene
        ob = context.object
        space = context.space_data
        toolsettings = context.tool_settings
        screen = context.screen
        userpref = context.user_preferences
        edit = userpref.edit 
        interpolation = context.user_preferences.edit.keyframe_new_interpolation_type
        
        col = layout.column(align=True)
        row = layout.row(align=True)
        row.operator("pose.breakdown0", text="0%", icon="REW")
        row.operator("pose.breakdown10", text="10%", icon="REW")
        row.operator("pose.breakdown33", text="33%", icon="REW")
        row = layout.row(align=True)
        row.operator("pose.breakdown50", text="50%", icon="PAUSE")
        row = layout.row(align=True)
        row.operator("pose.breakdown66", text="66%", icon="FF")
        row.operator("pose.breakdown90", text="90%", icon="FF")
        row.operator("pose.breakdown100", text="100%", icon="FF")
        row = layout.box()
        row.label("TweenMachine Variable")
        row.label("use SHIFT + E")



def register():

    bpy.utils.register_module(__name__)

def unregister():

    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()

