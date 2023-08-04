import numpy as np
import open3d as o3d

print("Testing mesh in Open3D...")
knot_mesh = o3d.data.KnotMesh()
mesh = o3d.io.read_triangle_mesh(knot_mesh.path)

# bottom plane
plane = o3d.geometry.TriangleMesh.create_box(width=300.0, height=300.0, depth=0.1)


# print(mesh)
# print('Vertices:')
# print(np.asarray(mesh.vertices))
# print('Triangles:')
# print(np.asarray(mesh.triangles))

o3d.visualization.draw_geometries([mesh, plane])

