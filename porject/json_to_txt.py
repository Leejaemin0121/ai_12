import json


def convert_to_yolo_format(data):
    yolo_lines = []
    for shape in data['shapes']:
        label = shape['label']
        x_coords = [point[0] for point in shape['points']]
        y_coords = [point[1] for point in shape['points']]
        x_min = min(x_coords)
        x_max = max(x_coords)
        y_min = min(y_coords)
        y_max = max(y_coords)

        x_center = (x_min + x_max) / 2
        y_center = (y_min + y_max) / 2
        width = x_max - x_min
        height = y_max - y_min

        yolo_line = f"{label} {x_center} {y_center} {width} {height}"
        yolo_lines.append(yolo_line)

    return yolo_lines


json_file_path = 'V001_tom1_39_001_a1_00_20210930_14_00134902_49122255.json'
yolo_lines = []

with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)
    yolo_lines = convert_to_yolo_format(json_data)

output_file_path = 'V001_tom1_39_001_a1_00_20210930_14_00134902_49122255.txt'
with open(output_file_path, 'w') as output_file:
    for line in yolo_lines:
        output_file.write(line + '\n')

print(f"Converted YOLO format saved to {output_file_path}")
