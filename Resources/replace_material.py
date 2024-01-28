import bpy

# Access Blender's Mesh Editing Library
import bmesh


class ChangeMaterial:
    def __init__(self):
        """
        Define scene information
        """
        self.scene = bpy.data.scenes["Scene"]

        # Define the information relevant to the <bpy.data.objects>
        self.camera = bpy.data.objects["Camera"]
        self.axis = bpy.data.objects["Main Axis"]
        self.light_1 = bpy.data.objects["Light1"]
        self.light_2 = bpy.data.objects["Light2"]
        self.bg = bpy.data.objects["Plane"]
        self.obj_names = [
            "Hammer",
        ]
        self.objects = self.create_objects()

    def set_camera(self):
        """
        Set Camera Information
        """
        self.axis.rotation_euler = (0, 0, 0)
        self.axis.location = (0, 0, 0)
        self.camera.location = (0, 0, 1.2)

    def set_hammer(self):
        """
        Set Hammer Information
        """
        self.objects[0].rotation_euler = (90, 0, 180)
        self.objects[0].location = (0, -0.125, 0)
        self.objects[0].scale = (0.01, 0.01, 0.01)

    # def change_material(self, object):
    #     # Get a BMesh representation
    #     bm = bmesh.new()  # create an empty BMesh
    #     bm.from_mesh(me)  # fill it in from a Mesh
    #     pass

    def run(self):
        # bpy.ops.object.editmode_toggle()
        # bpy.ops.mesh.select_all()

        # bg_mesh = bmesh.edit_from_mesh(self.bg.data)

        # for face in bmesh.faces:
        #     mat = bpy.data.materials.new(f"face_{face.index}")
        #     mat.diffuse_color = (1.0, 1.0, 1.0, 1.0)
        #     self.bg.materials.append(mat)
        #     self.bg.active_material_index = face.index

        #     face.select = True
        #     bpy.ops.object.material_slot_assign()
        #     face.select = False
        pass
        # self.create_new_material()

    def create_new_material(self, pathname):
        material = bpy.data.materials.new(name="generated_material")
        material.use_nodes = True
        texImage = material.node_tree.nodes.new("ShaderNodeTexImage")
        texImage.image = bpy.data.images.load(pathname)

        principled_bsdf_node = material.node_tree.nodes["Principled BSDF"]
        principled_bsdf_node.inputs["Base Color"].default_value = (1.0, 1.0, 1.0, 1.0)

        material.node_tree.links.new(
            principled_bsdf_node.inputs["Base Color"], texImage.outputs["Color"]
        )

        # Assign it to object
        if self.bg.data.materials:
            self.bg.data.materials[0] = material
        else:
            self.bg.materials.append(material)

    def create_objects(
        self,
    ):  # This function creates a list of all the <bpy.data.objects>
        objs = []
        for obj in self.obj_names:
            objs.append(bpy.data.objects[obj])

        return objs


if __name__ == "__main__":
    # Initialize rendering class as r
    r = ChangeMaterial()
    # Initialize camera
    r.set_camera()
    # Set first object/hammer's information
    r.set_hammer()
    # Begin data generation
    r.create_new_material()
