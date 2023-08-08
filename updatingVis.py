import numpy as np
import copy
import open3d as o3d
import time
import threading

print("Testing mesh in Open3D...")

# UPDATE INTERVAL
INTERVAL = 0.5

# Lane line
lane_line = o3d.geometry.TriangleMesh.create_box(width=50.0, height=10.0, depth=100.0)
lane_line = copy.deepcopy(lane_line).translate((0.0, 0.0, 50))
lane_line.compute_vertex_normals()



# bottom plane (from box)



# print(mesh)
# print('Vertices:')
# print(np.asarray(mesh.vertices))
# print('Triangles:')
# print(np.asarray(mesh.triangles))

# example of give lane
""" left_lane = [[229, 709], [238, 699], [249, 689], [260, 679], [271, 669], [282, 659],
    [293, 649], [304, 639], [315, 629], [325, 619], [336, 609], [348, 599], [359, 589],
    [369, 579], [381, 569], [390, 559], [404, 549], [415, 539], [426, 529], [438, 519],
    [450, 509], [461, 499], [472, 489], [482, 479], [493, 469], [504, 458], [515, 449],
    [526, 439], [536, 429], [546, 419], [555, 409], [565, 399], [572, 389]]
"""

plane_width = 300.0
plane_height = 5.0
plane_depth = 300.0
plane = o3d.geometry.TriangleMesh.create_box(width=plane_width, height=plane_height, depth=plane_depth)

def loopTest():
    # PLANE DIMENSIONS
    global plane_width
    global plane_height
    global plane_depth
    global plane

    threading.Timer(INTERVAL, loopTest).start()
    print("test")

    # plane
    plane_width += 100.0
    plane = o3d.geometry.TriangleMesh.create_box(width=plane_width, height=plane_height, depth=plane_depth)

    o3d.visualization.update_geometry()


plane_translate = copy.deepcopy(plane).translate((200, 0.0, 0.0))
o3d.visualization.draw_geometries([plane, plane_translate, lane_line])
loopTest()

print("")


