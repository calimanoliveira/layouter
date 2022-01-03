import bpy


class PlayBlastPanel(bpy.types.Panel):
    bl_label = "Playblast"
    bl_category = "AnimBlend"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_idname = "PB_painel"
    bl_options = {'DEFAULT_CLOSED'}

    
    def draw(self, context):    

        layout = self.layout     
        
        col = layout.column(align=True)
 
        rd = context.scene.render
        #am = context.active_object.data
        view = context.space_data
        scene = context.scene
        ob = context.object
        space = context.space_data
        toolsettings = context.tool_settings
        screen = context.screen
        userpref = context.user_preferences
        edit = userpref.edit 
#        arm = context.object.data
#        ad = context.active_object.animation_data
        interpolation = context.user_preferences.edit.keyframe_new_interpolation_type

        image_settings = rd.image_settings
        file_format = image_settings.file_format
        
        col= layout.column(align=True)
        col.label(text="Playblast:")
        
        row = layout.row(align=True)     
        row.operator("render.opengl", text="Still", icon='RENDER_STILL')
        row.operator("render.opengl", text="Animation", icon='RENDER_ANIMATION').animation = True
        row.operator("render.play_rendered_anim", text="Play", icon='PLAY')
        row = layout.row()
        row.menu("RENDER_MT_presets", text=bpy.types.RENDER_MT_presets.bl_label)
        row = layout.row(align=True)
        row.prop(scene, "use_preview_range", text="", toggle=True)
        if not scene.use_preview_range:
            row.prop(scene, "frame_start", text="Start")
            row.prop(scene, "frame_end", text="End")
        else:
            row.prop(scene, "frame_preview_start", text="Start")
            row.prop(scene, "frame_preview_end", text="End")

        layout.prop(rd, "filepath", text="")
#        layout.template_image_settings(image_settings, color_management=False)

        col = layout.column(align=True)
        col.prop(edit, "keyframe_new_interpolation_type", text='Keys')
        col.prop(edit, "keyframe_new_handle_type", text="Handles")
        
        row = layout.row()
        row.prop(view, "show_only_render", text="Only Render View")
