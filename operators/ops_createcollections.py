import bpy


class LT_OT_CreateCollections(bpy.types.Operator):
    
    bl_idname = "lt.createcollections"
    bl_label = "Create Collection"

    def execute(self, context):

        scene = context.scene
        obj = bpy.ops.objects
        myproperties = scene.my_properties

        for c in scene.collection.children:
            scene.collection.children.unlink(c)

        for c in bpy.data.collections:
            if not c.users:
                bpy.data.collections.remove(c)        

        collection = bpy.context.blend_data.collections.new(name='01_CAMERAS')
        bpy.context.collection.children.link(collection)

        collection = bpy.context.blend_data.collections.new(name='02_CHARACTERS')
        bpy.context.collection.children.link(collection)

        collection = bpy.context.blend_data.collections.new(name='03_PROPS')
        bpy.context.collection.children.link(collection)

        collection = bpy.context.blend_data.collections.new(name='04_ENVIRONMENT')
        bpy.context.collection.children.link(collection)

        collection = bpy.context.blend_data.collections.new(name='05_MOCAP')
        bpy.context.collection.children.link(collection)

        collection = bpy.context.blend_data.collections.new(name='06_FX')
        bpy.context.collection.children.link(collection)

        collection = bpy.context.blend_data.collections.new(name='07_PROXYS')
        bpy.context.collection.children.link(collection)


        #bpy.context.blend_data.collections.new(name='new_collection')
        #bpy.ops.outliner.collection_new()
        #bpy.data.collections.new(name='new_collection')

        # bpy.ops.collection.create("MyTestCollection")
        # collection = bpy.data.collections["MyTestCollection"]
        # we first create the camera object

        return {"FINISHED"}
