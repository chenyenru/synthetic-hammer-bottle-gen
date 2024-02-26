# Generate synthetic data with Blender and Python
======
Adapted from [Federico Arenas López's Data Generation with Blender](https://federicoarenasl.github.io/Data-Generation-with-Blender/)

## Demo

<img src="Resources/result.gif" height="300">
<img src="Resources/result2.gif" height="300">

## Todos

- [x] Different background
- [ ] Plastic Bottle
    - [ ] 1 L wide-mouthed plastic water bottle
    - [ ] Material
        - [ ] Transparent + Plastic
        - [ ] Plastic + :
            - [ ] Blue
            - [ ] Grey
            - [ ] Pink
            - [ ] Orange
            - [ ] Red

- [x] Hammer
    - [x] Different Hammer materials
        - [x] Rough plastic

- [ ] `main.script`
    - [x] Test the effect of rough plastic material
    - [x] Loop through different backgrounds
    - [ ] Loop through different color

## How to Run

### To create synthetic data

```bash
cd Resources
blender -b YOLO_data_generator.blend --background --python main_script.py
```

### To draw the bounding boxes and create a video
```bash
cd Resources
python3 draw_bounding.py
```
