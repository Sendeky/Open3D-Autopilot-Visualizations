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

o3d.visualization.draw_geometries([mesh, knot_translate, plane])

