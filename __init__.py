bl_info = {
    "name": "ARKit Blendshape Helper",
    "author": "Elijah Atkins",
    "description": "ARKit Helper Add-on",
    "blender": (2, 93, 0),
    "version": (1, 0, 0),
    "location": "View3D > Sidebar > ARKit Helper",
    "category": "Animation"
}

import bpy
from .facial_rig_operator import FacialRigOperator
from .facial_rig_panel import OBJECT_PT_facial_rig_panel

classes = (
    
    FacialRigOperator,
    OBJECT_PT_facial_rig_panel,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.arkit_source_object = bpy.props.PointerProperty(type=bpy.types.Object)
    bpy.types.Scene.arkit_target_object = bpy.props.PointerProperty(type=bpy.types.Object)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.arkit_source_object
    del bpy.types.Scene.arkit_target_object

if __name__ == "__main__":
    register()
