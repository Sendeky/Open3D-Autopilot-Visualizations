import open3d as o3d
import time
import numpy as np
from scipy.interpolate import CubicSpline


# example of lane
left_lane = [[27, 519], [54, 509], [87, 499], [123, 489], [157, 479],
             [193, 469], [235, 458], [271, 449], [310, 439], [352, 429],
             [393, 419], [430, 409], [465, 399], [497, 389], [523, 379]]

# example of how the lanes are given
center_lane = [[183, 709], [192, 699], [205, 689], [217, 679], [230, 669],
               [243, 659], [255, 649], [267, 639], [280, 629], [293, 619],
               [305, 609], [317, 599], [331, 589], [343, 579], [355, 569],
               [367, 559], [378, 549], [390, 539], [404, 529], [417, 519],
               [429, 509], [444, 499], [457, 489], [469, 479], [482, 469],
               [497, 458], [508, 449], [521, 439], [535, 429], [547, 419],
               [558, 409], [572, 399], [583, 389], [594, 379]]

# 2nd center lane
center2_lane = [[1141, 709], [1128, 699], [1115, 689], [1100, 679], [1087, 669],
                [1073, 659], [1059, 649], [1044, 639], [1029, 629], [1014, 619],
                [1000, 609], [986, 599], [971, 589], [956, 579], [939, 569],
                [925, 559], [910, 549], [893, 539], [875, 529], [858, 519],
                [842, 509], [827, 499], [811, 489], [796, 479], [778, 469],
                [761, 458], [746, 449], [729, 439], [715, 429], [700, 419],
                [686, 409], [674, 399], [661, 389], [650, 379]]

# rightmost lane
right_lane = [[1223, 509], [1187, 499], [1154, 489], [1120, 479], [1086, 469],
              [1042, 458], [1004, 449], [964, 439], [925, 429], [882, 419],
              [840, 409], [801, 399], [766, 389], [741, 379], [724, 368]]

# Convert 2D points to 3D
constant_z = 0
center_lane_3d = np.array([[x, y, constant_z] for x, y in center_lane])
center2_lane_3d = np.array([[x, y, constant_z] for x, y in center2_lane])
# center_lane_3d = np.array([[constant_z, x, y] for x, y in center_lane])
left_lane_3d = np.array([[x, y, constant_z] for x, y in left_lane])
right_lane_3d = np.array([[x, y, constant_z] for x, y in right_lane])

# Normalize the values
center_x_min = np.min(center_lane_3d[:, 0])
center_x_max = np.max(center_lane_3d[:, 0])
center2_x_min = np.min(center2_lane_3d[:, 0])
center2_x_max = np.max(center2_lane_3d[:, 0])
# center_normalized_x = center_lane_3d[:, 0] / (center_x_max - center_x_min)
# print("norm x: ", normalized_x)
left_x_min = np.min(left_lane_3d[:, 0])
left_x_max = np.max(left_lane_3d[:, 0])
right_x_min = np.min(right_lane_3d[:, 0])
right_x_max = np.max(right_lane_3d[:, 0])
# left_normalized_x = left_lane_3d[:, 0] / (left_x_max - left_x_min)


# Approximate the curve using cubic spline interpolation
# spline = CubicSpline(center_lane_3d[:, 0], center_lane_3d[:, 1])
# center_lane_3d[:, 0] = center_normalized_x
# left_lane_3d[:, 0] = left_normalized_x

# Combine both lanes' data
combined_lane_data = np.vstack((left_lane_3d, center_lane_3d, center2_lane_3d, right_lane_3d))

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
        start_time = time.time()
        # Update your data points (e.g., center_lane_3d)
        # Update your data points with slight motion
        for i in range(len(center_lane_3d)):
            center_lane_3d[i, 0] += np.random.uniform(-0.2, 0.2)
            center_lane_3d[i, 1] += np.random.uniform(-0.1, 0.1)

        # Interpolate y-values based on the curve
        # center_lane_3d[:, 0] = spline(center_lane_3d[:, 0])
        # print("spline: ", spline(center_lane_3d[:, 0]))
        combined_lane_data = np.vstack((left_lane_3d, center_lane_3d, center2_lane_3d, right_lane_3d))

        # Update the PointCloud data
        pcd.points = o3d.utility.Vector3dVector(combined_lane_data)
        # pcd.points = o3d.utility.Vector3dVector(left_lane_3d)

        # Update the visualization
        vis.update_geometry(pcd)
        vis.poll_events()
        vis.update_renderer()

        # Sleep to achieve the desired update frequency (e.g., 1/12 seconds)
        end_time = time.time()
        print("running time: ", end_time - start_time)
        # time.sleep(1/12)
finally:
    # Close the visualization window when done
    vis.destroy_window()