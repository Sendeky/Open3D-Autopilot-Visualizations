import open3d as o3d
import time
import numpy as np
from scipy.interpolate import CubicSpline


# example of lane
left_lane = [[26, 519], [55, 509], [88, 499], [124, 489], [160, 479],
             [197, 469], [233, 458], [265, 449], [301, 439], [338, 429],
             [376, 419], [413, 409], [448, 399], [482, 389], [510, 379]]

# example of how the lanes are given
center_lane = [[229, 709], [238, 699], [249, 689], [260, 679], [271, 669], [282, 659],
    [293, 649], [304, 639], [315, 629], [325, 619], [336, 609], [348, 599], [359, 589],
    [369, 579], [381, 569], [390, 559], [404, 549], [415, 539], [426, 529], [438, 519],
    [450, 509], [461, 499], [472, 489], [482, 479], [493, 469], [504, 458], [515, 449],
    [526, 439], [536, 429], [546, 419], [555, 409], [565, 399], [572, 389]]

# Convert 2D points to 3D
constant_z = 0
center_lane_3d = np.array([[x, y, constant_z] for x, y in center_lane])
# center_lane_3d = np.array([[constant_z, x, y] for x, y in center_lane])
left_lane_3d = np.array([[x, y, constant_z] for x, y in left_lane])

# Normalize the values
center_x_min = np.min(center_lane_3d[:, 0])
center_x_max = np.max(center_lane_3d[:, 0])
# center_normalized_x = center_lane_3d[:, 0] / (center_x_max - center_x_min)
# print("norm x: ", normalized_x)
left_x_min = np.min(left_lane_3d[:, 0])
left_x_max = np.max(left_lane_3d[:, 0])
# left_normalized_x = left_lane_3d[:, 0] / (left_x_max - left_x_min)


# Approximate the curve using cubic spline interpolation
# spline = CubicSpline(center_lane_3d[:, 0], center_lane_3d[:, 1])
# center_lane_3d[:, 0] = center_normalized_x
# left_lane_3d[:, 0] = left_normalized_x

# Combine both lanes' data
combined_lane_data = np.vstack((left_lane_3d, center_lane_3d))

# Create a PointCloud object
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(combined_lane_data)
# pcd.points = o3d.utility.Vector3dVector(left_lane_3d)

# Create a visualization window
vis = o3d.visualization.Visualizer()
vis.create_window()

# Add the PointCloud to the visualization
vis.add_geometry(pcd)

# Update the visualization
try:
    while True:
        # Update your data points (e.g., center_lane_3d)
        # Update your data points with slight motion
        for i in range(len(center_lane_3d)):
            center_lane_3d[i, 0] += np.random.uniform(-0.2, 0.2)
            # center_lane_3d[i, 1] += np.random.uniform(-0.1, 0.1)

        # Interpolate y-values based on the curve
        # center_lane_3d[:, 0] = spline(center_lane_3d[:, 0])
        # print("spline: ", spline(center_lane_3d[:, 0]))

        # Update the PointCloud data
        pcd.points = o3d.utility.Vector3dVector(combined_lane_data)
        # pcd.points = o3d.utility.Vector3dVector(left_lane_3d)

        # Update the visualization
        vis.update_geometry(pcd)
        vis.poll_events()
        vis.update_renderer()

        # Sleep to achieve the desired update frequency (e.g., 1/12 seconds)
        time.sleep(1/12)
finally:
    # Close the visualization window when done
    vis.destroy_window()