from manim import *

class CycloidScene(Scene):
    def construct(self):
        # Parameters
        radius = 1
        roll_speed = 1.5  # Slower for smoothness
        circle = Circle(radius=radius, color=WHITE).shift(LEFT * 5 + DOWN * radius)  # Circle on left, touching ground
        dot = Dot(color=YELLOW, radius=0.1).move_to(circle.get_bottom())  # Dot at bottom
        ground = Line(LEFT * 7, RIGHT * 7, color=GRAY_D, stroke_opacity=0.2)  # Subtle ground line
        cycloid = VMobject(color=GOLD, stroke_width=5)  # Gold cycloid trace
        cycloid.start_new_path(dot.get_center())

        # Track rotation angle
        angle_tracker = ValueTracker(0)

        # Updater for circle, dot, and cycloid
        def update_circle_and_dot(m, dt):
            # Increment angle based on roll speed
            angle_increment = roll_speed * dt / radius  # Arc length = radius * angle
            angle_tracker.increment_value(angle_increment)
            theta = angle_tracker.get_value()
            
            # Move circle right (roll distance = radius * theta)
            circle.shift(RIGHT * angle_increment * radius)
            
            # Rotate circle and update dot position
            circle.rotate(-angle_increment, about_point=circle.get_center())
            dot.move_to(circle.get_bottom())  # Keep dot at bottom
            cycloid.add_points_as_corners([dot.get_center()])  # Trace cycloid

        circle.add_updater(update_circle_and_dot)

        # Add objects
        self.add(ground, circle, dot, cycloid)

        # Animate one full roll (2π radians)
        self.play(
            angle_tracker.animate.set_value(2 * PI),
            run_time=2 * PI / roll_speed,  # Time = distance / speed
            rate_func=linear
        )

        # Stop updates and finalize
        circle.clear_updaters()
        self.wait(1)