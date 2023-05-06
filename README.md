# ARKit Blendshape Helper
With this Blender addon, you can use ARKit blendshapes to animate any 3D model's face with facial motion capture. The addon automatically creates and applies shape keys to your model that match the ARKit facial expressions. This way, you can easily convert your facial rig into ARKit compatible blendshapes.

## To Install ARKitHelper.py, follow these steps:
- Download the file from github using this link: [https://github.com/elijah-atkins/ARKitBlendshapeHelper/ARKitHelper.py](https://github.com/elijah-atkins/ARKitBlendshapeHelper/blob/main/ARKitHelper)
- Open Blender and go to Edit > Preferences > Addons
- Click on "Install" and navigate to the script file you downloaded. Select the file and click "Install Add-on".
- Enable the "ARKit Helper" add-on by checking the box next to it.
- In the 3D Viewport, go to the Sidebar (press N) and find the "ARKit Helper" panel.
- 
## To use the blender addon ARKitBlendshapeHelper, follow these steps:
- Rig your character using your preferred method.
- Set a resting Basis pose on frame 0
- Create 52 ARKit poses for your character in frames 1-52. You can use the reference for the blendshapes here: https://arkit-face-blendshapes.com/ 
-  In each frame, the ARKit Helper panel will display the name of the pose it is expecting. If the frame number is out of range, the panel will display "No name for this frame".
- Duplicate your character and set the original as the source and the duplicate as the target in the ARKit Helper panel.
- Select a source object by clicking on the "Source Object" dropdown and choosing an object from the list.(The original)
- Select a target object by clicking on the "Target Object" dropdown and choosing an object from the list.(The duplicate)
- Click "Create ARKit Blendshapes" and wait for the addon to generate the blendshapes on the target head.

The name and order of each blendshape that ARKit uses to describe faces.
  1: 'eyeBlinkLeft',
  2: 'eyeLookDownLeft',
  3: 'eyeLookInLeft',
  4: 'eyeLookOutLeft',
  5: 'eyeLookUpLeft',
  6: 'eyeSquintLeft',
  7: 'eyeWideLeft',
  8: 'eyeBlinkRight',
  9: 'eyeLookDownRight',
  10: 'eyeLookInRight',
  11: 'eyeLookOutRight',
  12: 'eyeLookUpRight',
  13: 'eyeSquintRight',
  14: 'eyeWideRight',
  15: 'jawForward',
  16: 'jawLeft',
  17: 'jawRight',
  18: 'jawOpen',
  19: 'mouthClose',
  20: 'mouthFunnel',
  21: 'mouthPucker',
  22: 'mouthRight',
  23: 'mouthLeft',
  24: 'mouthSmileLeft',
  25: 'mouthSmileRight',
  26: 'mouthFrownRight',
  27: 'mouthFrownLeft',
  28: 'mouthDimpleLeft',
  29: 'mouthDimpleRight',
  30: 'mouthStretchLeft',
  31: 'mouthStretchRight',
  32: 'mouthRollLower',
  33: 'mouthRollUpper',
  34: 'mouthShrugLower',
  35: 'mouthShrugUpper',
  36: 'mouthPressLeft',
  37: 'mouthPressRight',
  38: 'mouthLowerDownLeft',
  39: 'mouthLowerDownRight',
  40: 'mouthUpperUpLeft',
  41: 'mouthUpperUpRight',
  42: 'browDownLeft',
  43: 'browDownRight',
  44: 'browInnerUp',
  45: 'browOuterUpLeft',
  46: 'browOuterUpRight',
  47: 'cheekPuff',
  48: 'cheekSquintLeft',
  49: 'cheekSquintRight',
  50: 'noseSneerLeft',
  51: 'noseSneerRight',
  52: 'tongueOut'
