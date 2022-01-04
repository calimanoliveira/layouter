import bpy
from bpy.types import Operator
from bpy_extras.object_utils import object_data_add
from mathutils import Vector
from math import radians

from ..ui.ui_wgt_library import *
from .ops_createcollections import *

def get_wgt_collection(self, context):
    # List of collections.
    scene_collections = bpy.data.collections
    # Get list of collection names.
    collection_list = [col.name for col in scene_collections if col.name == "COL_widgets"]
    # Check if any in list of collections is called COL_widgets.
    if collection_list:
        # If there is, get it.
        widget_collection = bpy.data.collections["COL_widgets"]
    else:
        # Create COL_widgets.
        widget_collection = bpy.data.collections.new("COL_widgets")
        # Link it to scene collection.
        bpy.context.scene.collection.children.link(widget_collection)
    return widget_collection


def assign_wgt_collection(widget, widget_collection):
    # List of all collections the widget is in.
    old_collections = widget.users_collection
    if widget_collection not in old_collections:
        # Link Widget to the COL_widgets.
        widget_collection.objects.link(widget)
        # Unlink from all old collections.
        for old in old_collections:
            old.objects.unlink(widget)


def hide_collection(collection):
    # Hide collection
    collection.hide_viewport = True
    collection.hide_render = True


class LT_OT_CreateMarkers(bpy.types.Operator):
    
    bl_idname = "lt.createmarker"
    bl_label = "Create Marker"

    def execute(self, context):
        context = bpy.context
        scene = context.scene
        myproperties = scene.my_properties

        # self.CreateCamera(context)
        # self.CreateRig(context)
        # self.ShapeBones(context)

        # marker = scene.timeline_markers.new(myproperties.nameMarker) # make a new marker
        # marker.frame = scene.frame_current # set a frame
        # marker.select = True # set selected
        # marker.camera = scene.objects.get(myproperties.nameMarker+"_CAM")

        for collection in bpy.data.collections:
            #print(collection.name)
            if collection.name == '01_CAMERAS':
                self.CreateCamera(context)
                self.CreateRig(context)
                self.ShapeBones(context)

                marker = scene.timeline_markers.new(myproperties.nameMarker) # make a new marker
                marker.frame = scene.frame_current # set a frame
                marker.select = True # set selected
                marker.camera = scene.objects.get(myproperties.nameMarker+"_CAM")
                return {"FINISHED"}
            else:
                LT_OT_CreateCollections.execute(self, context)
                self.CreateCamera(context)
                self.CreateRig(context)
                self.ShapeBones(context)

                marker = scene.timeline_markers.new(myproperties.nameMarker) # make a new marker
                marker.frame = scene.frame_current # set a frame
                marker.select = True # set selected
                marker.camera = scene.objects.get(myproperties.nameMarker+"_CAM")

                return {"FINISHED"}
               
 
        return {"FINISHED"}
    
    def ShapeBones(self,context):
        
        context = bpy.context
        scene = context.scene
        myproperties = scene.my_properties    
        shapeExist=0
        name_rig=myproperties.nameMarker+'_RIG'
        name_cam=myproperties.nameMarker+'_CAM'    
        ob = bpy.context.scene.objects[name_rig]
        obj = bpy.data.objects[name_cam]       # Get the object
        bpy.ops.object.select_all(action='DESELECT') # Deselect all objects
        bpy.context.view_layer.objects.active = ob   # Make the cube the active object 
        ob.select_set(True)     
        
        arma = bpy.data.objects[myproperties.nameMarker+'_RIG']
        
        bpy.ops.object.select_all(action='SELECT') # Deselect all objects

        for obj in bpy.context.selected_objects:
            if  bpy.data.objects.find('WGTL_position')!=-1: #search for params items in object name
                shapeExist=1
                break

        bpy.ops.object.select_all(action='DESELECT') # Deselect all objects

        if shapeExist==0: 

            add_wgt_position(self,context)
            bpy.data.objects[name_rig].pose.bones['position'].custom_shape = bpy.context.selected_objects[0]
            bpy.data.objects[name_rig].pose.bones['position'].custom_shape_scale_xyz[0]=0.12
            bpy.data.objects[name_rig].pose.bones['position'].custom_shape_scale_xyz[1]=0.12
            bpy.data.objects[name_rig].pose.bones['position'].custom_shape_scale_xyz[2]=0.12
            bpy.data.objects[name_rig].pose.bones['position'].custom_shape_rotation_euler[0]=1.5708

            add_wgt_offset(self,context)

            bpy.data.objects[name_rig].pose.bones['offset'].custom_shape = bpy.context.selected_objects[0]
            bpy.data.objects[name_rig].pose.bones['offset'].custom_shape_scale_xyz[0]=0.06
            bpy.data.objects[name_rig].pose.bones['offset'].custom_shape_scale_xyz[1]=0.06
            bpy.data.objects[name_rig].pose.bones['offset'].custom_shape_scale_xyz[2]=0.06
            bpy.data.objects[name_rig].pose.bones['offset'].custom_shape_rotation_euler[0]=1.5708

            add_wgt_local(self,context)

            bpy.data.objects[name_rig].pose.bones['local'].custom_shape = bpy.context.selected_objects[0]
            bpy.data.objects[name_rig].pose.bones['local'].custom_shape_scale_xyz[0]=0.02
            bpy.data.objects[name_rig].pose.bones['local'].custom_shape_scale_xyz[1]=0.02
            bpy.data.objects[name_rig].pose.bones['local'].custom_shape_scale_xyz[2]=0.02
            bpy.data.objects[name_rig].pose.bones['local'].custom_shape_rotation_euler[0]=1.5708
            bpy.data.objects[name_rig].pose.bones['local'].custom_shape_rotation_euler[2]=1.5708
            bpy.data.objects[name_rig].pose.bones['local'].custom_shape_translation[2]=-3

            add_wgt_shake(self,context)

            bpy.data.objects[name_rig].pose.bones['shake'].custom_shape = bpy.context.selected_objects[0]
            bpy.data.objects[name_rig].pose.bones['shake'].custom_shape_scale_xyz[0]=0.2
            bpy.data.objects[name_rig].pose.bones['shake'].custom_shape_scale_xyz[1]=0.2
            bpy.data.objects[name_rig].pose.bones['shake'].custom_shape_scale_xyz[2]=0.2
            bpy.data.objects[name_rig].pose.bones['shake'].custom_shape_rotation_euler[0]=1.5708
            bpy.data.objects[name_rig].pose.bones['shake'].custom_shape_rotation_euler[1]=1.5708

            widget_collection = get_wgt_collection(self, context)

            all = bpy.context.scene.objects
            widglist = [wgt for wgt in all if "WGTL_" in wgt.name]
            for widget in widglist:
                assign_wgt_collection(widget, widget_collection)

            hide_collection(widget_collection)


        else:

            bpy.data.objects['WGTL_position'].select_set(True)
            bpy.data.objects[name_rig].pose.bones['position'].custom_shape =  bpy.data.objects['WGTL_position']
            bpy.data.objects[name_rig].pose.bones['position'].custom_shape_scale_xyz[0]=0.2
            bpy.data.objects[name_rig].pose.bones['position'].custom_shape_scale_xyz[1]=0.2
            bpy.data.objects[name_rig].pose.bones['position'].custom_shape_scale_xyz[2]=0.2
            bpy.data.objects[name_rig].pose.bones['position'].custom_shape_rotation_euler[0]=1.5708
            bpy.data.objects['WGTL_position'].select_set(False)
            
            bpy.data.objects['WGTL_offset'].select_set(True)
            bpy.data.objects[name_rig].pose.bones['offset'].custom_shape =  bpy.data.objects['WGTL_offset']
            bpy.data.objects[name_rig].pose.bones['offset'].custom_shape_scale_xyz[0]=0.1
            bpy.data.objects[name_rig].pose.bones['offset'].custom_shape_scale_xyz[1]=0.1
            bpy.data.objects[name_rig].pose.bones['offset'].custom_shape_scale_xyz[2]=0.1
            bpy.data.objects[name_rig].pose.bones['offset'].custom_shape_rotation_euler[0]=1.5708
            bpy.data.objects['WGTL_offset'].select_set(False)

            bpy.data.objects['WGTL_local'].select_set(True)
            bpy.data.objects[name_rig].pose.bones['local'].custom_shape =  bpy.data.objects['WGTL_local']
            bpy.data.objects[name_rig].pose.bones['local'].custom_shape_scale_xyz[0]=0.02
            bpy.data.objects[name_rig].pose.bones['local'].custom_shape_scale_xyz[1]=0.02
            bpy.data.objects[name_rig].pose.bones['local'].custom_shape_scale_xyz[2]=0.02
            bpy.data.objects[name_rig].pose.bones['local'].custom_shape_rotation_euler[0]=1.5708
            bpy.data.objects[name_rig].pose.bones['local'].custom_shape_rotation_euler[2]=1.5708
            bpy.data.objects[name_rig].pose.bones['local'].custom_shape_translation[2]=-3
            bpy.data.objects['WGTL_local'].select_set(False)
            bpy.data.objects['WGTL_shake'].select_set(True)
            bpy.data.objects[name_rig].pose.bones['shake'].custom_shape =  bpy.data.objects['WGTL_shake']
            bpy.data.objects[name_rig].pose.bones['shake'].custom_shape_scale_xyz[0]=0.1
            bpy.data.objects[name_rig].pose.bones['shake'].custom_shape_scale_xyz[1]=0.1
            bpy.data.objects[name_rig].pose.bones['shake'].custom_shape_scale_xyz[2]=0.1
            bpy.data.objects[name_rig].pose.bones['shake'].custom_shape_rotation_euler[0]=1.5708
            bpy.data.objects[name_rig].pose.bones['shake'].custom_shape_rotation_euler[1]=1.5708
            bpy.data.objects['WGTL_shake'].select_set(False)

        return {"FINISHED"}

    def CreateRig(self, context):

        context = bpy.context
        scene = context.scene
        myproperties = scene.my_properties

        armature = bpy.data.armatures.new(myproperties.nameMarker+'_RIG')
        armature_object = bpy.data.objects.new(myproperties.nameMarker+'_RIG', armature)
        view_layer = bpy.context.view_layer
        view_layer.active_layer_collection.collection.objects.link(armature_object)

        name_rig=myproperties.nameMarker+'_RIG' 
        name_cam=myproperties.nameMarker+'_CAM'   
        ob = bpy.context.scene.objects[name_rig]
        obj = bpy.data.objects[myproperties.nameMarker+'_CAM']       # Get the object
        bpy.ops.object.select_all(action='DESELECT') # Deselect all objects
        bpy.context.view_layer.objects.active = ob   # Make the cube the active object 
        ob.select_set(True)     
        
        arma = bpy.data.objects[myproperties.nameMarker+'_RIG']
        
        bpy.ops.object.mode_set(mode='EDIT', toggle=False)
        # Add a bone
        position = armature_object.data.edit_bones.new('position')
        position.head=(0,0,0)
        position.tail=(0,0,0.5)

        offset = armature_object.data.edit_bones.new('offset')
        offset.head=(0,0,0)
        offset.tail=(0,0,1)
        offset.parent=position
        local = armature_object.data.edit_bones.new('local')
        local.head=(0,0,1.4)
        local.tail=(0,0,2.4)
        local.parent=offset

        shake = armature_object.data.edit_bones.new('shake')
        shake.head=(0,0,1.4)
        shake.tail=(0,0,1.8)
        shake.parent=local

        # ...
        #Exit armature editing; this allows bones to be used in Pose/Object modes
        parent_bone = 'shake'
        arma.data.edit_bones.active = arma.data.edit_bones['shake']
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

        bpy.ops.object.mode_set(mode='POSE', toggle=False)
        
        bone = bpy.context.active_object.pose.bones['position']
        bone.rotation_mode='XYZ'
        bone.lock_rotation[0]=True
        bone.lock_rotation[2]=True
        bone.lock_scale[0]=True
        bone.lock_scale[1]=True
        bone.lock_scale[2]=True
        
        bone = bpy.context.active_object.pose.bones['offset']
        bone.rotation_mode='XYZ'
        bone.lock_rotation[0]=True
        bone.lock_rotation[2]=True
        bone.lock_scale[0]=True
        bone.lock_scale[1]=True
        bone.lock_scale[2]=True

        bone = bpy.context.active_object.pose.bones['local']
        bone.rotation_mode='XYZ'

        bone.lock_location[0]=True
        bone.lock_location[1]=True
        bone.lock_location[2]=True
        bone.lock_rotation[1]=True
        bone.lock_rotation[2]=True
        bone.lock_scale[0]=True
        bone.lock_scale[1]=True
        bone.lock_scale[2]=True

        bone = bpy.context.active_object.pose.bones['shake']
        bone.rotation_mode='XYZ'
        bone.lock_location[0]=True
        bone.lock_location[1]=True
        bone.lock_location[2]=True
        bone.lock_scale[0]=True
        bone.lock_scale[1]=True
        bone.lock_scale[2]=True
        #bpy.context.active_pose_bone.rotation_mode = 'XYZ'

        #context.active_pose_bone.lock_location[0]=True
        
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)


        bpy.ops.object.select_all(action='DESELECT') #deselect all objects
        obj.select_set(True)
        arma.select_set(True)
        bpy.context.view_layer.objects.active = arma    #the active object will be the parent of all selected object

        bpy.ops.object.parent_set(type='BONE', keep_transform=True)

        bpy.data.collections['01_CAMERAS'].objects.link(bpy.data.objects[name_rig])
        bpy.context.scene.collection.objects.unlink(bpy.data.objects[name_rig])

        bpy.data.collections['01_CAMERAS'].objects.link(bpy.data.objects[name_cam])
        bpy.context.scene.collection.objects.unlink(bpy.data.objects[name_cam])

        return {"FINISHED"}
    
    def CreateCamera(self,context):

        context = bpy.context
        scene = context.scene
        myproperties = scene.my_properties


        cam_data = bpy.data.cameras.new(myproperties.nameMarker+'_CAM')
        cam = bpy.data.objects.new(myproperties.nameMarker+'_CAM', cam_data)
        bpy.context.collection.objects.link(cam)

        name_cam=myproperties.nameMarker+'_CAM'    
        ob = bpy.context.scene.objects[name_cam]       # Get the object
        bpy.ops.object.select_all(action='DESELECT') # Deselect all objects
        bpy.context.view_layer.objects.active = ob   # Make the cube the active object 
        ob.select_set(True)     
        bpy.data.objects[name_cam].location.z = 1.4
        bpy.data.objects[name_cam].rotation_euler.x = 1.5708

        bpy.data.objects[name_cam].lock_location[0]=True
        bpy.data.objects[name_cam].lock_location[1]=True
        bpy.data.objects[name_cam].lock_location[2]=True

        bpy.data.objects[name_cam].lock_rotation[0]=True
        bpy.data.objects[name_cam].lock_rotation[1]=True
        bpy.data.objects[name_cam].lock_rotation[2]=True

        bpy.data.objects[name_cam].lock_scale[0]=True
        bpy.data.objects[name_cam].lock_scale[1]=True
        bpy.data.objects[name_cam].lock_scale[2]=True


        return {"FINISHED"}