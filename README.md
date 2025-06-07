# Spinning-Doughnut

A terminal-based animation of the classic spinning donut, originally inspired by Andy Sloane's ASCII donut. This project is a fun and nostalgic demonstration of ASCII graphics and simple math to render a rotating 3D torus (doughnut shape).

✨ Features
Renders a rotating 3D donut in the terminal using ASCII characters 

Lightweight and portable

🛠️ How It Works
The donut is made using basic trigonometry and a z-buffer to simulate depth. The program:

Calculates x, y, z coordinates on a 3D torus

Projects 3D coordinates to 2D terminal space

Uses luminance values to choose ASCII characters (.,-~:;=!*#$@)

Continuously updates to simulate rotation
