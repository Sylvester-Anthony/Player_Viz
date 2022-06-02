import json
from mplsoccer.pitch import Pitch
import matplotlib.pyplot as plt

with open(r"3788741.json") as f:
    data = json.load(f)

p = Pitch()
fig, ax = p.draw(figsize=(8, 5))

frame_idx = 3470
visible_area_xs = data[frame_idx]["visible_area"][::2]
visible_area_ys = data[frame_idx]["visible_area"][1::2]

player_position_data = data[frame_idx]["freeze_frame"]
teammate_locs = [ppd["location"] for ppd in player_position_data if ppd["teammate"]]
opposition_locs = [ppd["location"] for ppd in player_position_data if not ppd["teammate"]]

ax.fill(visible_area_xs, visible_area_ys, color=(1, 0, 0, 0.3))

[ax.scatter(x, y,  color='orange', s=80, ec='k') for (x, y) in teammate_locs]
[ax.scatter(x, y,  color='blue', s=80, ec='k') for (x, y) in opposition_locs]

plt.show()