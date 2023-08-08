import open3d as o3d
import time
import numpy as np


left_lane = [[229, 709], [238, 699], [249, 689], [260, 679], [271, 669], [282, 659],
    [293, 649], [304, 639], [315, 629], [325, 619], [336, 609], [348, 599], [359, 589],
    [369, 579], [381, 569], [390, 559], [404, 549], [415, 539], [426, 529], [438, 519],
    [450, 509], [461, 499], [472, 489], [482, 479], [493, 469], [504, 458], [515, 449],
    [526, 439], [536, 429], [546, 419], [555, 409], [565, 399], [572, 389]]

# Convert 2D points to 3D
constant_z = 0
# left_lane_3d = np.array([[x, y, constant_z] for x, y in left_lane])
left_lane_3d = np.array([[constant_z, x, y] for x, y in left_lane])

# Create a PointCloud object
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(left_lane_3d)

# Create a visualization window
vis = o3d.visualization.Visualizer()
vis.create_window()

# Add the PointCloud to the visualization
vis.add_geometry(pcd)

# Update the visualization
try:
    while True:
        # Update your data points (e.g., left_lane_3d)
        # Update your data points with slight motion
        for i in range(len(left_lane_3d)):
            left_lane_3d[i, 0] += np.random.uniform(-0.1, 0.1)
            left_lane_3d[i, 1] += np.random.uniform(-0.1, 0.1)

        # Update the PointCloud data
        pcd.points = o3d.utility.Vector3dVector(left_lane_3d)

        # Update the visualization
        vis.update_geometry(pcd)
        vis.poll_events()
        vis.update_renderer()

        # Sleep to achieve the desired update frequency (e.g., 1/12 seconds)
        time.sleep(1/12)
finally:
    # Close the visualization window when done
    vis.destroy_window()