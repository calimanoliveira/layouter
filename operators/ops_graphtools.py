

#class ANIMBLEND_OT_curveLocY(bpy.types.Operator):
#    bl_idname = "ab.curve_LocY"
#    bl_label = "Curve LocY"
#    bl_options = {'REGISTER' , 'UNDO'}

#    #    LocY = BoolProperty(
#    #            name="LocY",
#    #            description="Property is Loc in Y",
#    #            default = True
#    #        )

#    @classmethod
#    def poll(cls , context):
#        return True

#    def execute(self , context):
#        layout = self.layout
#        scene = context.scene
#        myProperties = scene.my_properties
#        layout.prop(myProperties , "LocY")
#        print("Passou por aqui")
#        bpy.ops.transform.translate(constraint_axis=(False , True , False))
#        return {'FINISHED'}

#class ANIMBLEND_OT_animtools_Operator(bpy.types.Operator):
#    bl_idname = 'ab.animtools'
#    bl_label = "AnimTools"
#    bl_options = {'REGISTER'}

#    @classmethod
#    def poll(cls , context):
#        return True

#    def execute(self , context):
#        return {'FINISHED'}


#class ANIMBLEND_OT_TranslateWrapper(bpy.types.Operator):
#    bl_idname = "ab.translate_wrapper"
#    bl_label = "animblend translate"
#    bl_description = ""
#    bl_options = {"REGISTER" , "UNDO"}

#    @classmethod
#    def poll(cls , context):
#        return True

#    def execute(self , context):
#        # call translate but constraining the axis with the lockY option
#        bpy.ops.transform.translate(
#            "INVOKE_DEFAULT" ,
#            constraint_axis=(False , context.scene.my_properties.LocY , False)
#        )
#        return {"FINISHED"}
