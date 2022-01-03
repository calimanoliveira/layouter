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
    bl_idname = "TM_painel"
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

class ValBreakdown_0(bpy.types.Operator):
    bl_idname = "pose.breakdown0"
    bl_label = "Val0"

    def execute(self, context):
        posAnterior = 0
        posPosterior = 0
        posAtual = 0
        screen = context.screen

        posAtual = context.scene.frame_current

        bpy.ops.screen.keyframe_jump(next=False)
        posAnterior = context.scene.frame_current

        context.scene.frame_current = posAtual

        bpy.ops.screen.keyframe_jump(next=True)
        posPosterior = context.scene.frame_current

        context.scene.frame_current = posAtual
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
        bpy.ops.pose.breakdown(prev_frame=posAnterior, next_frame=posPosterior, percentage=0)
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

        return {"FINISHED"}


class ValBreakdown_10(bpy.types.Operator):
    bl_idname = "pose.breakdown10"
    bl_label = "Val10"

    def execute(self, context):
        posAnterior = 0
        posPosterior = 0
        posAtual = 0
        screen = context.screen

        posAtual = context.scene.frame_current

        bpy.ops.screen.keyframe_jump(next=False)
        posAnterior = context.scene.frame_current
        print(posAnterior)
        context.scene.frame_current = posAtual

        bpy.ops.screen.keyframe_jump(next=True)
        posPosterior = context.scene.frame_current
        print(posPosterior)

        context.scene.frame_current = posAtual
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
        bpy.ops.pose.breakdown(percentage=0.1,prev_frame=posAnterior, next_frame=posPosterior)
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

        return {"FINISHED"}


class ValBreakdown_33(bpy.types.Operator):
    bl_idname = "pose.breakdown33"
    bl_label = "Val0"

    def execute(self, context):
        posAnterior = 0
        posPosterior = 0
        posAtual = 0
        screen = context.screen

        posAtual = context.scene.frame_current

        bpy.ops.screen.keyframe_jump(next=False)
        posAnterior = context.scene.frame_current

        context.scene.frame_current = posAtual

        bpy.ops.screen.keyframe_jump(next=True)
        posPosterior = context.scene.frame_current

        context.scene.frame_current = posAtual
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
        bpy.ops.pose.breakdown(prev_frame=posAnterior, next_frame=posPosterior, percentage=0.33)
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

        return {"FINISHED"}


class ValBreakdown_50(bpy.types.Operator):
    bl_idname = "pose.breakdown50"
    bl_label = "Val50"

    def execute(self, context):
        posAnterior = 0
        posPosterior = 0
        posAtual = 0
        screen = context.screen

        posAtual = context.scene.frame_current

        bpy.ops.screen.keyframe_jump(next=False)
        posAnterior = context.scene.frame_current

        context.scene.frame_current = posAtual

        bpy.ops.screen.keyframe_jump(next=True)
        posPosterior = context.scene.frame_current

        context.scene.frame_current = posAtual
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
        bpy.ops.pose.breakdown(prev_frame=posAnterior, next_frame=posPosterior, percentage=0.5)
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

        return {"FINISHED"}


class ValBreakdown_66(bpy.types.Operator):
    bl_idname = "pose.breakdown66"
    bl_label = "Val66"

    def execute(self, context):
        posAnterior = 0
        posPosterior = 0
        posAtual = 0
        screen = context.screen

        posAtual = context.scene.frame_current

        bpy.ops.screen.keyframe_jump(next=False)
        posAnterior = context.scene.frame_current

        context.scene.frame_current = posAtual

        bpy.ops.screen.keyframe_jump(next=True)
        posPosterior = context.scene.frame_current

        context.scene.frame_current = posAtual
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
        bpy.ops.pose.breakdown(prev_frame=posAnterior, next_frame=posPosterior, percentage=0.66)
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

        return {"FINISHED"}


class ValBreakdown_90(bpy.types.Operator):
    bl_idname = "pose.breakdown90"
    bl_label = "Val90"

    def execute(self, context):
        posAnterior = 0
        posPosterior = 0
        posAtual = 0
        screen = context.screen

        posAtual = context.scene.frame_current

        bpy.ops.screen.keyframe_jump(next=False)
        posAnterior = context.scene.frame_current

        context.scene.frame_current = posAtual

        bpy.ops.screen.keyframe_jump(next=True)
        posPosterior = context.scene.frame_current

        context.scene.frame_current = posAtual
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
        bpy.ops.pose.breakdown(prev_frame=posAnterior, next_frame=posPosterior, percentage=0.9)
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

        return {"FINISHED"}


class ValBreakdown_100(bpy.types.Operator):
    bl_idname = "pose.breakdown100"
    bl_label = "Val100"

    def execute(self, context):
        posAnterior = 0
        posPosterior = 0
        posAtual = 0
        screen = context.screen

        posAtual = context.scene.frame_current

        bpy.ops.screen.keyframe_jump(next=False)
        posAnterior = context.scene.frame_current

        context.scene.frame_current = posAtual

        bpy.ops.screen.keyframe_jump(next=True)
        posPosterior = context.scene.frame_current

        context.scene.frame_current = posAtual
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = True
        bpy.ops.pose.breakdown(prev_frame=posAnterior, next_frame=posPosterior, percentage=1)
        bpy.context.scene.tool_settings.use_keyframe_insert_auto = False

        return {"FINISHED"}


def register():
    bpy.utils.register_class(ValBreakdown_0)
    bpy.utils.register_class(ValBreakdown_10)
    bpy.utils.register_class(ValBreakdown_33)
    bpy.utils.register_class(ValBreakdown_50)
    bpy.utils.register_class(ValBreakdown_66)
    bpy.utils.register_class(ValBreakdown_90)
    bpy.utils.register_class(ValBreakdown_100)

    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_class(ValBreakdown_0)
    bpy.utils.unregister_class(ValBreakdown_10)
    bpy.utils.unregister_class(ValBreakdown_33)
    bpy.utils.unregister_class(ValBreakdown_50)
    bpy.utils.unregister_class(ValBreakdown_66)
    bpy.utils.unregister_class(ValBreakdown_90)
    bpy.utils.unregister_class(ValBreakdown_100)

    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()

