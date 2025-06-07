import math
import time

A = 0
B = 0

print("\x1b[2J") 

while True:
    output = [' '] * 1760  
    zbuffer = [0] * 1760

    for j in range(0, 628, 7):  
        for i in range(0, 628, 2):
            c = math.sin(i / 100)
            d = math.cos(j / 100)
            e = math.sin(A)
            f = math.sin(j / 100)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i / 100)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = x + 80 * y
            if 0 <= o < 1760:
                if D > zbuffer[o]:
                    zbuffer[o] = D
                    luminance_index = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
                    luminance_index = max(0, min(11, luminance_index))
                    chars = ".,-~:;=!*#$@"  
                    output[o] = chars[luminance_index]
    print("\x1b[H", end='')
    for i in range(0, 1760, 80):
        print("".join(output[i:i + 80]))

    A += 0.04
    B += 0.08
    time.sleep(0.0001)
