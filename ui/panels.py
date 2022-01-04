import bpy
from bpy.types import Panel, UILayout, Menu
from ..operators.ops_createmarkers import *

from bpy.props import StringProperty
# Null ##################################################################################
class LT_OT_Null(Operator):
    bl_idname      = "cameramanager.null_tool"
    bl_label       = ""
    bl_description = "Camera Manager"

    nullMode : bpy.props.StringProperty(name="tool", default="")

    def invoke(self, context, event):
        scene         = context.scene
        chosen_camera = context.active_object
        selectedObj   = context.selected_objects
        cameras       = sorted([o for o in scene.objects if o.type == 'CAMERA'],key=lambda o: o.name)
        selectedCam   = sorted([o for o in selectedObj if o.type == 'CAMERA'],key=lambda o: o.name)

        if self.nullMode == 'SELECT':
            if chosen_camera not in selectedCam:
                if event.alt:
                    bpy.ops.cameramanager.select_tool("INVOKE_DEFAULT",selectTool = "INVERT")
                elif event.shift:
                    bpy.ops.cameramanager.select_tool("INVOKE_DEFAULT",selectTool = "ALL")
                else:
                    bpy.ops.cameramanager.select_tool("INVOKE_DEFAULT",selectTool = "NONE")

        elif self.nullMode == 'NOTSELECTED':
            self.report({"INFO"}, 'Select Camera Before !')

        elif self.nullMode == 'NULL':
            self.nullMode == ''
            #return {"FINISHED"}

        self.nullMode == ''

        return {"FINISHED"}

# SELECT MENU CAMERA ##################################################################################
class LT_MT_SelectMenu(Menu):
    bl_label       = "Select Camera"
    bl_idname      = "LT_MT_selectmenu"
    #bl_description = "Camera Tools"

    def draw(self, context):
        scene  = context.scene
        rs     = scene.RBTab_Settings
        render = scene.render

        cameras         = sorted([o for o in scene.objects if o.type == 'CAMERA'],key=lambda o: o.name)
        selectedObj     = context.selected_objects
        selectedCam     = sorted([o for o in selectedObj if o.type == 'CAMERA'],key=lambda o: o.name)
        noneSelectedCam = list(set(cameras) - set(selectedCam))
        constraintsCam  = sorted([o for o in cameras if len(o.constraints) > 0],key=lambda o: o.name)
        customDimCam    = sorted([o for o in cameras if o.RBTab_obj_Settings.Custom_CamRes_prop == True],key=lambda o: o.name)

        animDataCam     = sorted([o for o in cameras
                                    if (o.animation_data is not None) or (o.data.animation_data is not None)
                                    ],key=lambda o: o.name)
        emptyAnimCam    = sorted([o for o in animDataCam
                                    if (o.animation_data is not None and o.animation_data.action is None)
                                    or (o.data.animation_data is not None and o.data.animation_data.action is None)
                                    ],key=lambda o: o.name)

        marker_list         = context.scene.timeline_markers
        list_marked_cameras = [o.camera for o in marker_list if o != None]

        layout  = self.layout
        row = layout.row(align=True)

        row.operator("cameramanager.select_tool",text="All").selectTool="ALL"
        row = layout.row(align=True)
        row.operator("cameramanager.select_tool",text="None").selectTool="NONE"
        row = layout.row(align=True)
        row.operator("cameramanager.select_tool",text="Invert").selectTool="INVERT"
        row = layout.row(align=True)
        row.operator("cameramanager.select_tool",text="Scene Camera").selectTool="SCCAMERA"


        layout.separator()

        row = layout.row(align=True)
        if len(constraintsCam)>0:row.enabled = True
        else: row.enabled = False
        row.operator("cameramanager.select_tool",text="With Tract to",icon='CON_FOLLOWTRACK').selectTool="TRACKTO"

        row = layout.row(align=True)
        if len(list_marked_cameras)>0:row.enabled = True
        else: row.enabled = False
        row.operator("cameramanager.select_tool",text="With Marker",icon='MARKER_HLT').selectTool="MARKER"

        row = layout.row(align=True)
        if len(animDataCam)>0:row.enabled = True
        else: row.enabled = False
        row.operator("cameramanager.select_tool",text="With Anim Datas",icon='KEYTYPE_KEYFRAME_VEC').selectTool="ANIMDATA"

        row = layout.row(align=True)
        if len(emptyAnimCam)>0:row.enabled = True
        else: row.enabled = False
        row.operator("cameramanager.select_tool",text="With Empty Anim Datas",icon='KEYFRAME').selectTool="EMPTYANIMDATA"

        row = layout.row(align=True)
        if len(customDimCam)>0:row.enabled = True
        else: row.enabled = False
        row.operator("cameramanager.select_tool",text="With Custom Resolution",icon='WORKSPACE').selectTool="CUSTOMDIM"


class LT_PT_CreateCollection(Panel):
    bl_label = "Create Collection"
    bl_category = "Layouter Tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_idname = "LT_PT_createcollection"
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

        myproperties = scene.my_properties
        col = layout.column(align=True)
        row = layout.row(align=True)
        col.operator("lt.createcollections", text="Create Collection", icon="IMPORT")


class LT_PT_CreateMarkers(Panel):
    bl_label = "Create Markers"
    bl_category = "Layouter Tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_idname = "LT_PT_createmarkers"
    bl_options = {'DEFAULT_CLOSED'}


    #text = bpy.props.StringProperty(name= "Name Marker:")

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

        myproperties = scene.my_properties
        col = layout.column(align=True)
        row = layout.row(align=True)
        row.label(text="Name Markers")
        row.prop(myproperties, "nameMarker", text="")
        col = layout.column(align=True)
        col.operator("lt.createmarker", text="Create Marker", icon="IMPORT")


class LT_PT_SetupCameras(Panel):
    bl_label = "Setup Cameras"
    bl_category = "Layouter Tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_idname = "LT_PT_setupcameras"
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

        scene   = context.scene
        render  = scene.render
        cameras = sorted([o for o in scene.objects if o.type == 'CAMERA'],key=lambda o: o.name)

        selectedObj    = bpy.context.selected_objects
        selectedCam    = sorted([o for o in selectedObj if o.type == 'CAMERA'],key=lambda o: o.name)
        constraintsCam = sorted([o for o in cameras if len(o.constraints) > 0],key=lambda o: o.name)

        animDataCam    = sorted([o for o in cameras
                                    if (o.animation_data is not None) or (o.data.animation_data is not None)
                                    ],key=lambda o: o.name)
        emptyAnimCam   = sorted([o for o in animDataCam
                                    if (o.animation_data is not None and o.animation_data.action is None)
                                    or (o.data.animation_data is not None and o.data.animation_data.action is None)
                                    ],key=lambda o: o.name)

        render_all_list = []

        myproperties = scene.my_properties
        col = layout.column(align=True)
        row = layout.row(align=True)
        TheLayout = self.layout
        col = TheLayout.column(align=True)
        
        for camera in cameras:
            col.separator()
            col.label(text=camera.name)
             #Camera name          
            if len(selectedCam) <=1 and camera not in selectedObj: col.prop(camera, "name", text="")
            elif len(selectedCam) >=1 and camera in selectedObj: col.operator("cameramanager.null_tool", text="{0}".format(camera.name)).nullMode='SELECTs'#row.prop(camera, "name", text="",emboss=False)                        
            #else: row.operator("cameramanager.null_tool", text="{0}".format(camera.name),emboss=False).nullMode='SELECT'
            col.separator()
            col.prop(camera.data, "lens")
        
        #print (cameras)
#        col.operator("lt.createcollections", text="Create Collection", icon="IMPORT")

# #   ###Cameras List[ ______________________________________________________________________________________________

#         if len(cameras) >1:
#             row = layout.row(align=True)
#             row.menu(SCENECAMERA_MT_SelectMenu.bl_idname,text="Selection",icon='BORDERMOVE')
#             if len(selectedCam)>0:
#                 row.menu(SCENECAMERA_MT_ToolsMenu.bl_idname,text="Tools",icon='TOOL_SETTINGS')
#         for camera in cameras:
#             #rs_obj = camera.RBTab_obj_Settings
#             row    = layout.row(align=True)

#             row.context_pointer_set("active_object", camera)

#             if rs.Manager_ShowSelect == True:
#                 if len(selectedCam)>0:

#                     if rs.Manager_ShowSelect_Gray == True and len(selectedCam)>1: row.active = False

#                     if camera in selectedObj:

#                         if rs.Manager_ShowSelect_Pointer == True:
#                             row.operator("cameramanager.null_tool", text="", icon='RIGHTARROW_THIN',emboss=False).nullMode='SELECT'
#                             #row.label(text ="",icon='RIGHTARROW_THIN')

#                         if rs.Manager_ShowSelect_Color == True:
#                             row.alert = True

#                         row.active = True
#                     else:
#                         if rs.Manager_ShowSelect_Pointer == True:
#                             row.operator("cameramanager.null_tool", text="", icon='BLANK1',emboss=False).nullMode='SELECT'

#             elif len(selectedCam)>0 and camera in selectedObj: row.alert = True

#             #Preview Camera button
#             _iconPreview       = ''
#             _iconPreviewEmboss = None
#             if camera == bpy.context.space_data.camera:
#                 _iconPreview       = 'RESTRICT_VIEW_OFF'
#                 _iconPreviewEmboss = True
#             else:
#                 if rs_obj.Custom_CamRes_prop == True:
#                     if camera == scene.camera:
#                         _iconPreview       = 'CAMERA_DATA'
#                         _iconPreviewEmboss = False
#                     else:
#                         _iconPreview       = 'WORKSPACE'
#                         _iconPreviewEmboss = False
#                 else:
#                     if camera == scene.camera:
#                         _iconPreview       = 'CAMERA_DATA'
#                         _iconPreviewEmboss = False
#                     else:
#                         _iconPreview       = 'RESTRICT_VIEW_ON'
#                         _iconPreviewEmboss = False

#             if len(selectedCam) <=1:
#                 row.operator("cameramanager.activpreview_scene_camera",text='', icon=_iconPreview, emboss=_iconPreviewEmboss)
#             elif len(selectedCam) >1 and camera in selectedObj: row.operator("cameramanager.activpreview_scene_camera",text='', icon=_iconPreview)
#             elif len(selectedCam) >1 and camera not in selectedObj:row.operator("cameramanager.activpreview_scene_camera",text='', icon=_iconPreview, emboss=_iconPreviewEmboss)
#             if rs.Manager_ShowSelect == False: row.alert = False

#             #Render button
#             if rs.cmBut_Render == True:
#                 if len(selectedCam) <=1:
#                     row.operator("cameramanager.render_scene_camera",text='', icon='SEQ_PREVIEW').renderFrom = 'CAMANAGER'
#                 #elif len(selectedCam) >1 and camera in selectedObj:row.operator("cameramanager.null_tool", text="", icon='BLANK1',emboss=True).nullMode='SELECT'
#                 elif camera not in selectedObj:row.operator("cameramanager.null_tool", text="", icon='SEQ_PREVIEW',emboss=True).nullMode='SELECT'


#             #Camera name          
#             if len(selectedCam) <=1 and camera not in selectedObj: row.prop(camera, "name", text="")
#             elif len(selectedCam) >=1 and camera in selectedObj: row.operator("cameramanager.null_tool", text="{0}".format(camera.name)).nullMode='SELECT'#row.prop(camera, "name", text="",emboss=False)                        
#             else: row.operator("cameramanager.null_tool", text="{0}".format(camera.name),emboss=False).nullMode='SELECT'


#             #Align View button
#             if rs.cmBut_AlignV == True:
#                 if len(selectedCam)<=1:
#                     row.operator("cameramanager.alignview_scene_camera", text="", icon='VIEW_PERSPECTIVE')
#                 #elif len(selectedCam) >1 and camera in selectedObj:row.operator("cameramanager.null_tool", text="", icon='BLANK1',emboss=True).nullMode='SELECT'
#                 elif camera not in selectedObj: row.operator("cameramanager.null_tool", text="", icon='VIEW_PERSPECTIVE',emboss=True).nullMode='SELECT'


#             #Align Obj button
#             if rs.cmBut_AlignO == True:
#                 if len(selectedCam) <=1 or  camera in selectedCam:
#                     row.operator("cameramanager.alignobj_scene_camera", text="", icon='CUBE')
#                 else:row.operator("cameramanager.null_tool", text="", icon='CUBE',emboss=True).nullMode='SELECT'

#             #Track To button: Add/Remove
#             if rs.cmBut_Trackto == True:
#                 if len(camera.constraints) == 0:
#                     #Add TrackTo button
#                     if camera in selectedObj or len(selectedCam) <=1:row.operator("cameramanager.trackto_scene_camera", text="", icon='TRACKER')
#                     else:row.operator("cameramanager.null_tool", text="", icon='TRACKER',emboss=True).nullMode='SELECT'
#                 else :
#                     #Remove TrackTo button
#                     if camera not in selectedCam and len(selectedCam) <=1:
#                         row.operator("cameramanager.removetrackto_scene_camera", text="", icon='CON_FOLLOWTRACK', emboss=False)
#                     elif camera in selectedCam and len(selectedCam) >= 1:
#                         row.operator("cameramanager.removetrackto_scene_camera", text="", icon='CON_FOLLOWTRACK', emboss=True)
#                     elif camera not in selectedCam and len(selectedCam) > 1:
#                         row.operator("cameramanager.null_tool", text="", icon='CON_FOLLOWTRACK',emboss=True).nullMode='SELECT'

#             #Marker button
#             if rs.cmBut_Marker == True:
#                 if camera in list_marked_cameras :
#                     m = 0
#                     for i,marker in enumerate(marker_list_camera):
#                         if marker_list_camera[i].frame != 0:
#                             if marker.camera == camera and m < 1:#prevent adding button if multiple marker on same camera
#                                 #Remove marker button
#                                 if camera in selectedCam :#and len(selectedCam) <=1:
#                                     row.operator("cameramanager.remove_camera_marker",text='', icon='MARKER_HLT', emboss=True)
#                                 elif camera not in selectedCam and len(selectedCam) <=1:
#                                     row.operator("cameramanager.remove_camera_marker",text='', icon='MARKER_HLT', emboss=False)
#                                 elif camera not in selectedCam and len(selectedCam) > 1:
#                                     row.operator("cameramanager.null_tool", text="", icon='MARKER_HLT',emboss=False).nullMode='SELECT'
#                                 m += 1
#                         elif marker_list_camera[i].frame == 0 and marker.camera == camera:
#                             if camera in selectedObj:
#                                 row.operator("cameramanager.null_tool", text="", icon='BLANK1',emboss=False).nullMode='NULL'
#                             elif rs_obj.Custom_CamRender_prop == True and camera not in selectedObj:
#                                 row.operator("cameramanager.add_camera_marker",text='', icon='MARKER')
#                             else:
#                                 row.operator("cameramanager.add_camera_marker",text='', icon='MARKER')

#                 #Add marker button
#                 else:
#                     if len(selectedCam)<=1:
#                         row.operator("cameramanager.add_camera_marker",text='', icon='MARKER')
#                     #elif len(list_marked_cameras)>0 and camera in selectedObj:
#                     elif camera in selectedObj:
#                         row.operator("cameramanager.null_tool", text="", icon='BLANK1',emboss=True).nullMode='SELECT'
#                     elif camera not in selectedObj:
#                         row.operator("cameramanager.null_tool", text="", icon='MARKER',emboss=True).nullMode='SELECT'


#             #Animation Data
#             if rs.cmBut_AnimData == True:
#                 if len(animDataCam) >0:
#                     #if bpy.data.cameras[camera.name].animation_data.action != None :
#                     if camera in animDataCam:# or bpy.data.cameras[camera.name].animation_data != None :
#                         if camera in emptyAnimCam :
#                             if camera in selectedObj and len(selectedCam) <=1:
#                                 row.operator("cameramanager.null_tool", text="", icon='KEYFRAME',emboss=True).nullMode='NULL'
#                             elif camera in selectedCam and len(selectedCam) >1:
#                                 row.operator("cameramanager.null_tool", text="", icon='KEYFRAME',emboss=True).nullMode='SELECT'
#                             else: row.operator("cameramanager.null_tool", text="", icon='KEYFRAME',emboss=False).nullMode='SELECT'
#                         else:
#                             if camera not in selectedObj and len(selectedCam) <=1:
#                                 row.operator("cameramanager.null_tool", text="", icon='KEYTYPE_KEYFRAME_VEC',emboss=False).nullMode='NULL'
#                             elif camera not in selectedObj and len(selectedCam) >1:
#                                 row.operator("cameramanager.null_tool", text="", icon='KEYFRAME_HLT',emboss=False).nullMode='SELECT'
#                             elif camera in selectedObj or len(selectedCam) >1:
#                                 row.operator("cameramanager.null_tool", text="", icon='KEYTYPE_KEYFRAME_VEC',emboss=True).nullMode='NULL'
#                             #else: row.operator("cameramanager.null_tool", text="", icon='KEYFRAME_HLT',emboss=False).nullMode='SELECT'
#                     else:
#                         if camera in selectedObj:
#                             row.operator("cameramanager.null_tool", text="", icon='BLANK1').nullMode='SELECT'
#                         else:row.operator("cameramanager.null_tool", text="", icon='BLANK1',emboss=False).nullMode='SELECT'
#             if len(animDataCam) < 1:row.separator()

#             #Remove camera button
#             if camera not in selectedCam and len(selectedCam) <=1:
#                 row.operator("cameramanager.del_scene_camera",text='', icon='PANEL_CLOSE', emboss=False)
#             elif camera in selectedCam and len(selectedCam) >=1:
#                 row.operator("cameramanager.del_scene_camera",text='', icon='PANEL_CLOSE', emboss=True)
#             elif camera not in selectedCam and len(selectedCam) >1:
#                 row.operator("cameramanager.null_tool", text="", icon='PANEL_CLOSE',emboss=False).nullMode='SELECT'

#             #Render Selection prop
#             if len(cameras) > 2 and rs.switchRenderSelection == True:
#                 #row.active = True
#                 row.alert = False
#                 row.prop(rs_obj,'Custom_CamRender_prop',text='')

#     ### ]Cameras List      

#class AB_PT_PlayBlast(bpy.types.Panel):
#    bl_label = "Playblast"
#    bl_category = "AnimBlend"
#    bl_space_type = 'VIEW_3D'
#    bl_region_type = 'UI'
#    bl_idname = "AB.playblast"
#    bl_options = {'DEFAULT_CLOSED'}

#    def draw(self, context):

#        layout = self.layout

#        col = layout.column(align=True)

#        rd = context.scene.render
#        # am = context.active_object.data
#        view = context.space_data
#        scene = context.scene
#        ob = context.object
#        space = context.space_data
#        toolsettings = context.tool_settings
#        screen = context.screen
#        userpref = context.preferences
#        edit = userpref.edit
#        #        arm = context.object.data
#        #        ad = context.active_object.animation_data
#        interpolation = context.preferences.edit.keyframe_new_interpolation_type

#        image_settings = rd.image_settings
#        file_format = image_settings.file_format

#        col = layout.column(align=True)
#        col.label(text="Playblast:")

#        row = layout.row(align=True)
#        row.operator("render.opengl", text="Still", icon='RENDER_STILL')
#        row.operator("render.opengl", text="Animation", icon='RENDER_ANIMATION').animation = True
#        row.operator("render.play_rendered_anim", text="Play", icon='PLAY')
#        row = layout.row()

#        layout.template_image_settings(image_settings, color_management=False)
#        layout.prop(rd.ffmpeg, "format")

#        row = layout.row(align=True)
#        row.prop(scene, "use_preview_range", text="", toggle=True)
#        if not scene.use_preview_range:
#            row.prop(scene, "frame_start", text="Start")
#            row.prop(scene, "frame_end", text="End")
#        else:
#            row.prop(scene, "frame_preview_start", text="Start")
#            row.prop(scene, "frame_preview_end", text="End")

#        layout.prop(rd, "filepath", text="")
#        #        layout.template_image_settings(image_settings, color_management=False)

#        col = layout.column(align=True)
#        col.prop(edit, "keyframe_new_interpolation_type", text='Keys')
#        col.prop(edit, "keyframe_new_handle_type", text="Handles")

#        row = layout.row()
#        row.prop(bpy.context.space_data.overlay, "show_overlays", text="Only Render View")

#class AB_PT_FrameRange(Panel):
#    bl_space_type = "VIEW_3D"
#    bl_region_type = "UI"
#    bl_category = "AnimBlend"

#    bl_idname = "AB.animblend"
#    bl_label = "Frame Range"

##    @classmethod
##    def poll(cls, context):
##        return

#    def draw(self, context):
#        layout = self.layout
#        col = layout.column(align=True)
#        row = col.row()

#        rd = context.scene.render
#        view = context.space_data
#        scene = context.scene
#        ob = context.object
#        space = context.space_data
#        toolsettings = context.tool_settings
#        screen = context.screen

#        col = layout.column(align=True)
#        row = layout.row(align=True)
#        col.label(text="Range :")

#        col = layout.column(align=True)
#        row = layout.row(align=True)

#        col.label(text="Range2 :")
#        
#	
#class AB_PT_animtools_GE(bpy.types.Panel):
#    bl_idname = 'ab.animtools_GE_Panel'
#    bl_label = "Graph Editor Panel"
#    bl_space_type = "GRAPH_EDITOR"
#    bl_region_type = "UI"
#    bl_category = "Animation"

#    # bl_options = {'REGISTER'}

#    def draw(self , context):
#        layout = self.layout
#        scene = context.scene
#        my_Properties = scene.my_properties
#        #layout.operator("ab.curve_LocY" , text="LocY")
#        # layout.operator("render.opengl", text="Still", icon='RENDER_STILL')
#        #        layout.operator("object.animtools", text="Loc Y")
#        #        layout.operator("animtools.mover_objeto",text="Move")
#        #        layout.operator("animblend.translate_wrapper",text="Move")
#        print("Passou por aqui")
#        layout.prop(my_Properties, "ab.curve_LocY" , text="LocY")

