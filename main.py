import bpy

number = 10
counter = 0
for a in range(0,number):
    counter+=2
    counter2 = 0
    for b in range(0,number):
        counter2+=2
        counter3 = 0
        for c in range(0,number):
            bpy.ops.mesh.primitive_cube_add(location=(counter3+2, counter2-2, counter-2), size=2)
            counter3+=2
