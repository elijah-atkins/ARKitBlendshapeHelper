import bpy
from .facial_rig_names import FacialRigNames

class OBJECT_PT_facial_rig_panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_facial_rig_panel"
    bl_label = "ARKit Helper"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "ARKit Helper"


    def draw(self, context):
        layout = self.layout
        # Add source object property
        layout.label(text="Set poses on frames 1-52")
        frame_number = context.scene.frame_current
        if frame_number in FacialRigNames.names:
            layout.label(text="Pose: " + FacialRigNames.names[frame_number])
        else:
            layout.label(text="No name for this frame.")
        layout.prop(context.scene, "arkit_source_object", text="Source Object")
        # Add target object property
        layout.prop(context.scene, "arkit_target_object", text="Target Object")
        layout.operator("object.facial_rig_operator", text="Create ARKit Blendshapes")
