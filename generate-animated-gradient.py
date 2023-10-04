import sys
import uuid
from math import floor


def hex_string_to_col(input: str) -> (int, int, int):
    seg_1 = int(input[1:3], 16)
    seg_2 = int(input[3:5], 16)
    seg_3 = int(input[5:7], 16)
    return (seg_1, seg_2, seg_3)


def rgb_to_hex_string(r: int, g: int, b: int) -> str:
    return f"#{r:0{2}x}{g:0{2}x}{b:0{2}x}"


def lerp(x: int, y: int, amount: float) -> int:
    return round((1 - amount) * x + amount * y)


manner = "linear"
steps = 100
angle = 0


if len(sys.argv) < 5:
    print(
        "Usage: <gradient-begin-colour-1> <gradient-end-colour-1> <gradient-begin-colour-2> <gradient-end-colour-2> [steps] [easing] [angle]")
    exit(1)

start1 = hex_string_to_col(sys.argv[1])
end1 = hex_string_to_col(sys.argv[2])

start2 = hex_string_to_col(sys.argv[3])
end2 = hex_string_to_col(sys.argv[4])

if len(sys.argv) > 5:
    steps = int(sys.argv[5])

if len(sys.argv) > 6:
    manner = sys.argv[6]

if len(sys.argv) > 7:
    angle = sys.argv[7]

print(
    f"Interpolating {start1} -> {end1} (manner: {manner}, steps: {steps}, angle: {angle}deg)")

rising = floor(steps / 2)
falling = floor(steps / 2)

css_file = ""

keyframe_name = uuid.uuid4()
css_file += f"@keyframes generated-{keyframe_name}"
css_file += " {\n"

# background: linear-gradient(114deg, var(--grad-colour-one) 0%, var(--grad-colour-two) 100%);

for i in range(rising):
    amount = (i) / rising
    r1 = lerp(start1[0], end1[0], amount)
    g1 = lerp(start1[1], end1[1], amount)
    b1 = lerp(start1[2], end1[2], amount)
    hex_str1 = rgb_to_hex_string(r1, g1, b1)

    r2 = lerp(start2[0], end2[0], amount)
    g2 = lerp(start2[1], end2[1], amount)
    b2 = lerp(start2[2], end2[2], amount)
    hex_str2 = rgb_to_hex_string(r2, g2, b2)

    css_file += f"    {i}% "
    css_file += "{ "
    css_file += f"background: linear-gradient({angle}deg, {hex_str1} 0%, {hex_str2} 100%);"
    css_file += " } \n"

for i in range(falling + 1):
    amount = (i) / rising
    r1 = lerp(end1[0], start1[0], amount)
    g1 = lerp(end1[1], start1[1], amount)
    b1 = lerp(end1[2], start1[2], amount)
    hex_str1 = rgb_to_hex_string(r1, g1, b1)

    r2 = lerp(end2[0], start2[0], amount)
    g2 = lerp(end2[1], start2[1], amount)
    b2 = lerp(end2[2], start2[2], amount)
    hex_str2 = rgb_to_hex_string(r2, g2, b2)

    css_file += f"    {(i + rising)}% "
    css_file += "{ "
    css_file += f"background: linear-gradient({angle}deg, {hex_str1} 0%, {hex_str2} 100%);"
    css_file += " } \n"

css_file += "\n}"

f = open("generated.css", "w")
f.write(css_file)
f.close()
