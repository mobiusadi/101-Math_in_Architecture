from manim import *

class CycloidAnimation(Scene):
    def construct(self):
        # Parameters
        radius = 1.0  # Circle radius
        roll_distance = 2 * PI * radius  # Distance for one full rotation (circumference)
        t_max = 2 * PI  # Parameter t for one full rotation

        # Create the ground (x-axis)
        ground = Line(start=LEFT * 4, end=RIGHT * 4, color=WHITE)
        self.add(ground)

        # Create the circle and the point
        circle = Circle(radius=radius, color=BLUE)
        point = Dot(color=RED).move_to(circle.get_right())  # Start at (r, 0) relative to circle center
        circle.move_to(ORIGIN + UP * radius)  # Center starts at (0, r)

        # Create a tracer for the cycloid path
        cycloid_path = VMobject(color=YELLOW)
        cycloid_path.set_points([point.get_center()])

        # Group circle and point for rotation
        rolling_group = VGroup(circle, point)

        # Function to update circle and point position
        def update_group(group, alpha):
            t = alpha * t_max
            # Move circle center: x = r*t, y = r (rolls along x-axis)
            group.move_to([radius * t, radius, 0])
            # Rotate point around circle center
            point.move_to(group[0].get_center() + radius * np.array([np.cos(t), -np.sin(t), 0]))
            # Update cycloid path
            cycloid_path.add_points_as_corners([point.get_center()])

        # Animation
        self.add(rolling_group, cycloid_path)
        self.play(
            UpdateFromAlphaFunc(rolling_group, update_group),
            run_time=5,  # Duration of animation
            rate_func=linear  # Linear rolling speed
        )
        self.wait(1)  # Pause at the end