# Generate synthetic data with Blender and Python
======
Adapted from [Federico Arenas López's Data Generation with Blender](https://federicoarenasl.github.io/Data-Generation-with-Blender/)

## Todos

- [ ] Different background
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

- [ ] Hammer
    - [ ] Different Hammer materials
        - [ ] Rough plastic


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
