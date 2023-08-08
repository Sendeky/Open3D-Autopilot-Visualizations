import numpy as np
import copy
import open3d as o3d

print("Testing mesh in Open3D...")

# knot mesh
knot_mesh = o3d.data.KnotMesh()
# knot_mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()
mesh = o3d.io.read_triangle_mesh(knot_mesh.path)
knot_translate = copy.deepcopy(mesh).translate((120.0, 0.0, 0.0))

# bottom plane (from box)
plane = o3d.geometry.TriangleMesh.create_box(width=300.0, height=5.0, depth=300.0)

# plane_translate = copy.deepcopy(plane).translate((1.3, 0.0, 0.0))
# print(mesh)
# print('Vertices:')
# print(np.asarray(mesh.vertices))
# print('Triangles:')
# print(np.asarray(mesh.triangles))

o3d.visualization.draw_geometries([knot_translate, plane])

# example of give lane
""" left_lane = [[229, 709], [238, 699], [249, 689], [260, 679], [271, 669], [282, 659],
    [293, 649], [304, 639], [315, 629], [325, 619], [336, 609], [348, 599], [359, 589],
    [369, 579], [381, 569], [390, 559], [404, 549], [415, 539], [426, 529], [438, 519],
    [450, 509], [461, 499], [472, 489], [482, 479], [493, 469], [504, 458], [515, 449],
    [526, 439], [536, 429], [546, 419], [555, 409], [565, 399], [572, 389]]
"""