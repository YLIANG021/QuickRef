# QuickRef

QuickRef 是一款专为 Blender 打造的高效参考图工具。它让参考图的添加、切换和调整更加快速直观，减少反复打开设置和手动调整参数的时间，帮助你更快完成对照和构图。

- 🖼️ 在一个面板中快速管理和切换多张参考图
- ✋ 直接在视图中移动、缩放和旋转参考图，无需配置复杂的参考图参数
- 🎚️ 无需打开侧栏，即可在 3D 视图标题栏快速调整不透明度和可见性，不遮挡视图，也不会干扰其他插件
- 🎬 使用两种构图模式快速匹配摄像机与场景关系
- ⚡ 一键从当前视图快速创建摄像机

---

## 插件位置

1. 在 3D 视图中按下 `N`，然后在侧栏打开“视图” → QuickRef。

---

## 支持语言

English • 简体中文 • 繁體中文 • 日本語 • 한국어 • Deutsch • Français • Español • Italiano • Polski • Português • Русский • Tiếng Việt

---

## 核心功能

### 1. 🖼️ 集中管理多张参考图

在同一个面板中快速添加、切换、复制、替换和删除参考图，无需反复打开 Blender 的背景图设置。

<img width="810" height="480" alt="August 22 (2)" src="https://github.com/user-attachments/assets/8c693a33-f255-40ca-99c6-9b044628fb0e" />

---

### 2. ⚡ 从当前视图快速创建摄像机

找到合适的角度后，只需一键即可将当前透视或正交视图转换为匹配的摄像机，无需再次手动对齐。

<img width="810" height="480" alt="8月27日" src="https://github.com/user-attachments/assets/84faef1a-a42c-45cf-911d-c2f471ae0039" />

---

### 3. ✋ 直接在摄像机视图中调整

点击“调整”后，直接在 3D 视图中拖动即可对齐参考图，避免复杂且不直观的参数调整。

- `G`：移动　`S`：缩放　`R`：旋转
- `Shift`：精细调整　`Ctrl`：数值吸附
- 鼠标左键：确认　鼠标右键或 `Esc`：退出

<img width="810" height="480" alt="August 22 (1)" src="https://github.com/user-attachments/assets/57dd58ec-4217-4f41-9564-89ae4ea1c764" />

---

### 4. 🎬 使用两种模式快速匹配构图

当场景与参考图的透视关系和遮挡关系不匹配时，QuickRef 可以帮助你快速调整透视和遮挡，并且保持构图关系。

Tools里面选择调整模式，吸管吸物体，然后点击play按钮开始调整

#### 调整透视模式

联动调整摄像机位置和焦距，在改变画面透视的同时，保持目标在画面中的大小和位置。让透视匹配更快速、更直观。

<img width="810" height="480" alt="8月29日(2)" src="https://github.com/user-attachments/assets/6be3c7dc-b8fc-4c59-b6de-6ce69619a547" />

#### 调整遮挡模式

同时调整目标物体的位置和大小，在保持画面构图的同时，快速改变与其他物体的前后遮挡关系，省去反复移动、缩放和重新对齐的操作。

<img width="810" height="480" alt="8月29日" src="https://github.com/user-attachments/assets/afb6edd4-8d7c-4afe-b6d5-3f293538b62d" />

---

### 5. 🎚️ 将常用控制放在手边

启用标题栏控制后，无需打开侧栏，即可在 3D 视图顶部快速调整参考图的不透明度和可见性，不遮挡视图，也不会干扰其他插件。

<img width="810" height="480" alt="August 22" src="https://github.com/user-attachments/assets/9f9bfbbc-408f-482d-b3b8-ccf4ff2b7acc" />

---

## 更多功能

- 复制摄像机及其参考图设置
- 快速切换投影类型、焦距和正交缩放
- 在保留原参考图设置的情况下，直接替换丢失的图片
- 使用一个吸取按钮选择 Mesh、空物体或曲线作为构图调整目标
- 通过屏幕左上角 HUD 查看鼠标调整和确认方式

---

## 系统要求

- Blender 4.2.0 或更高版本

