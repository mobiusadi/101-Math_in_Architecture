from manim import *

class GoldenRatioAnimation(Scene):
    def construct(self):
        # Golden ratio
        phi = (1 + np.sqrt(5)) / 2  # ≈ 1.618
        b = 1.0  # Length of segment b
        a = phi * b  # Length of segment a ≈ 1.618
        total_length = 2 * (a + b)  # ≈ 5.236

        # Step 1: Show the initial line of length 2(a + b)
        start = np.array([-total_length / 2, 0, 0])
        end = np.array([total_length / 2, 0, 0])
        line = Line(start, end, color=WHITE)
        self.play(Create(line))
        self.wait(1)

        # Step 2: Divide at point a
        # Place point a such that the line is split appropriately
        point_a_pos = start + np.array([a, 0, 0])  # Adjust position
        point_a = Dot(point_a_pos, color=RED)
        label_a = Text("a", color=RED).next_to(point_a, UP)
        self.play(FadeIn(point_a, label_a))
        self.wait(1)

        # Step 3: Bend into L-shape at point a
        # Split line into two segments: from start to a, and a to end
        line1 = Line(start, point_a_pos, color=WHITE)
        line2_start = point_a_pos
        line2_end = point_a_pos + np.array([0, -(total_length - a), 0])  # Bend down
        line2 = Line(line2_start, line2_end, color=WHITE)
        self.play(Transform(line, VGroup(line1, line2)))
        self.wait(1)

        # Step 4: Mark point b on the second segment
        point_b_pos = line2_start + np.array([0, -b, 0])
        point_b = Dot(point_b_pos, color=BLUE)
        label_b = Text("b", color=BLUE).next_to(point_b, LEFT)
        self.play(FadeIn(point_b, label_b))
        
        # Show ratio text
        ratio_text = MathTex(r"\frac{a}{b} = \frac{b}{a + b} = \phi").to_edge(UP)
        self.play(Write(ratio_text))
        self.wait(1)

        # Step 5: Complete the rectangle
        # Continue from b: turn 90° right (length a), then 90° up (length a + b)
        line3_start = point_b_pos
        line3_end = line3_start + np.array([a, 0, 0])  # Right by a
        line3 = Line(line3_start, line3_end, color=WHITE)
        line4_start = line3_end
        line4_end = line4_start + np.array([0, a + b, 0])  # Up by a + b
        line4 = Line(line4_start, line4_end, color=WHITE)
        self.play(Create(line3), Create(line4))
        self.wait(1)

        # Highlight the rectangle
        rectangle = Polygon(
            line2_start, line2_end, line3_end, line4_end,
            color=YELLOW, fill_opacity=0.2
        )
        self.play(Create(rectangle))
        self.wait(1)

        # Step 6: Highlight rectangle side ratios
        side_ratio_text = MathTex(
            r"\text{Side ratios: } \frac{a + b}{a} = \frac{a}{b} = \phi"
        ).next_to(ratio_text, DOWN)
        self.play(Write(side_ratio_text))
        self.wait(2)

        # Fade out for clean ending
        self.play(FadeOut(line1, line2, line3, line4, point_a, point_b, label_a, label_b, rectangle, ratio_text, side_ratio_text))
        self.wait(1)