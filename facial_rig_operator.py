import bpy
from .facial_rig_names import FacialRigNames

class FacialRigOperator(bpy.types.Operator):
    bl_idname = "object.facial_rig_operator"
    bl_label = "ARKit Helper Operator"
    
    def execute(self, context):
        scn = bpy.context.scene #get current scene
        scn.frame_set(0)
        # Deselect all objects
        bpy.ops.object.select_all(action='DESELECT')
        
        # Get the source and target objects from the panel UI
        source_obj = context.scene.arkit_source_object
        target_obj = context.scene.arkit_target_object
        
        # Select the source and target objects
        target_obj.select_set(True)
        source_obj.select_set(True)
        obj = bpy.context.active_object

        # Find the armature modifier by type
        armature_mod = None
        for mod in obj.modifiers:
            if mod.type == 'ARMATURE':
                armature_mod = mod
                break

        # If an armature modifier was found, remove it
        if armature_mod:
            obj.modifiers.remove(armature_mod)
        scn.frame_set(1)
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #1 eyeBlinkLeft
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #2 eyeLookDownLeft
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #3 eyeLookInLeft
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #4 eyeLookOutLeft
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #5 eyeLookUpLeft
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #6 eyeSquintLeft
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #7 eyeWideLeft
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #8 eyeBlinkRight
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #9 eyeLookDownRight
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #10 eyeLookInRight
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #11 eyeLookOutRight
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #12 eyeLookUpRight
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #13 eyeSquintRight
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #14 eyeWideRight
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #15 jawForward
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #16 jawLeft
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #17 jawRight
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #18 jawOpen
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #19 mouthClose
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #20 mouthFunnel
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #21 mouthPucker
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #22 mouthRight
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #23 mouthLeft
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #24 mouthSmileLeft
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #25 mouthSmileRight
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #26 mouthFrownRight
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #27 mouthFrownLeft
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #28 mouthDimpleLeft
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #29 mouthDimpleRight
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #30 mouthStretchLeft
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #31 mouthStretchRight
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #32 mouthRollLower
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #33 mouthRollUpper
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #34 mouthShrugLower
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #35 mouthShrugUpper
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #36 mouthPressLeft
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #37 mouthPressRight
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #38 mouthLowerDownLeft`
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #39 mouthLowerDownRight
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #40 mouthUpperUpLeft
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #41 mouthUpperUpRight
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #42 browDownLeft
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #43 browDownRight
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #44 browInnerUp
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #45 browOuterUpLeft
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #46 browOuterUpRight
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #47 cheekPuff
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #48 cheekSquintLeft
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #49 cheekSquintRight
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #50 noseSneerLeft
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #51 noseSneerRight
        bpy.ops.object.join_shapes()
        scn.frame_set(scn.frame_current + 1) #52 tongueOut


        # get the selected object
        selected_object = bpy.context.object

        # get its shapekeys
        shape_keys = selected_object.data.shape_keys.key_blocks

        # loop through shapekeys and replace the names
        for index, key in enumerate(shape_keys):
            if key.name != "Basis":
                try: key.name = FacialRigNames.names[index]
                except: pass


        return {'FINISHED'}
