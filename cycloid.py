from manim import *

class CycloidScene(Scene):
    def construct(self):
        # Circle parameters
        radius = 1
        circle = Circle(radius=radius, color=WHITE).shift(LEFT * 5)  # Start on left
        dot = Dot(color=YELLOW, radius=0.08).move_to(circle.get_bottom())  # Dot at bottom
        line = Line(LEFT * 7, RIGHT * 7, color=GRAY, stroke_opacity=0.3)  # Ground line

        # Cycloid curve
        cycloid = VMobject(color=GOLD, stroke_width=4)
        cycloid.start_new_path(dot.get_center())

        # Updater for rolling and tracing
        def update_circle_and_dot(m, dt):
            roll_speed = 2  # Adjust for smoother roll
            circle.shift(RIGHT * dt * roll_speed)  # Move right
            theta = -circle.get_center()[0] / radius  # Angle based on x-position
            dot.move_to(circle.point_from_proportion((theta / (2 * PI)) % 1))  # Update dot
            cycloid.add_points_as_corners([dot.get_center()])  # Trace cycloid

        circle.add_updater(update_circle_and_dot)

        # Add objects to scene
        self.add(line, circle, dot, cycloid)

        # Animate one full roll (2πr distance)
        roll_distance = 2 * PI * radius
        roll_time = roll_distance / 2  # 2 units/second speed
        self.play(circle.animate.shift(RIGHT * roll_distance), run_time=roll_time, rate_func=linear)

        # Stop updates and finalize
        circle.clear_updaters()
        self.wait(1)