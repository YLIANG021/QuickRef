# QuickRef

QuickRef is an efficient reference-image tool built specifically for Blender. It streamlines the workflow for camera reference images, making them faster and more intuitive to add, switch, and adjust, with less time spent digging through settings or tweaking parameters, so you can quickly complete comparisons and composition.

- 🖼️ Quickly manage and switch between multiple reference images
- ✋ Move, scale, and rotate reference images directly in the viewport without configuring complex reference-image parameters
- 🎚️ Quickly adjust opacity and visibility from the viewport header without opening the sidebar, blocking the view, or interfering with other add-ons
- 🎬 Use two composition modes to quickly match the camera and scene
- ⚡ Quickly create a camera from the current view

---

## Add-on Location

1. In the 3D View, press `N`, then open `View` → QuickRef in the sidebar.

---

## Language Support

English • 简体中文 • 繁體中文 • 日本語 • 한국어 • Deutsch • Français • Español • Italiano • Polski • Português • Русский • Tiếng Việt

---

## Core Features

### 1. 🖼️ Manage Multiple Reference Images in One Place

Quickly add, switch, duplicate, replace, and delete reference images from a single panel without repeatedly opening Blender's background-image settings.

<img width="810" height="480" alt="August 22 (2)" src="https://github.com/user-attachments/assets/8c693a33-f255-40ca-99c6-9b044628fb0e" />

---

### 2. ⚡ Quickly Create a Camera from the Current View

Found the right angle? Convert the current perspective or orthographic view into a matching camera with one click, without having to align the camera again.

<img width="810" height="480" alt="8月27日" src="https://github.com/user-attachments/assets/84faef1a-a42c-45cf-911d-c2f471ae0039" />

---

### 3. ✋ Adjust Directly in Camera View

After clicking `Adjust`, drag in the 3D viewport to align the reference image, avoiding complex and unintuitive parameter adjustments.

- `G`: Move　`S`: Scale　`R`: Rotate
- `Shift`: Fine adjustment　`Ctrl`: Numeric snapping
- Left mouse button: Confirm　Right mouse button or `Esc`: Exit

<img width="810" height="480" alt="August 22 (1)" src="https://github.com/user-attachments/assets/57dd58ec-4217-4f41-9564-89ae4ea1c764" />

---

### 4. 🎬 Quickly Match Composition with Two Modes *(New in v1.2.0)*

When the perspective and occlusion relationships in the scene do not match the reference image, QuickRef helps you quickly adjust perspective and occlusion while preserving the composition.

Choose an adjustment mode in Tools, use the eyedropper to pick an object, then click the play button to start adjusting.

#### Adjust Perspective Mode *(New in v1.2.0)*

Adjust the camera position and focal length together, changing the perspective while keeping the target's size and position in the frame. This makes perspective matching faster and more intuitive.

<img width="810" height="480" alt="8月29日(2)" src="https://github.com/user-attachments/assets/6be3c7dc-b8fc-4c59-b6de-6ce69619a547" />

#### Adjust Occlusion Mode *(New in v1.2.0)*

Adjust the target object's position and size together to quickly change its front-to-back occlusion relationship with other objects while preserving the composition, eliminating repeated moving, scaling, and realignment.

<img width="810" height="480" alt="8月29日" src="https://github.com/user-attachments/assets/afb6edd4-8d7c-4afe-b6d5-3f293538b62d" />


---

### 5. 🎚️ Keep Common Controls Close at Hand

Once the header controls are enabled, quickly adjust reference-image opacity and visibility from the top of the 3D View without opening the sidebar, blocking the view, or interfering with other add-ons.

<img width="810" height="480" alt="August 22" src="https://github.com/user-attachments/assets/9f9bfbbc-408f-482d-b3b8-ccf4ff2b7acc" />

---

## More Features

- Duplicate a camera and its reference-image settings
- Quickly change the projection type, focal length, and orthographic scale
- Replace missing images directly while preserving the original reference-image settings
- Use a single eyedropper button to select a Mesh, Empty, or Curve as the composition-adjustment target
- View mouse controls and confirmation instructions in the on-screen HUD

---

## System Requirements

- Blender 4.2.0 or later
