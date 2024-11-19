from manim import *

class Cover(Scene):
    def construct(self):
        title = Text("Digressão em Grafos")
        subtitle = Text("com a UFMG").scale(0.5).next_to(title, DOWN)
        author = Text("Por: Augusto Guerra de Lima").scale(0.4).next_to(subtitle, DOWN)

        self.play(FadeIn(title))
        self.play(FadeIn(subtitle))
        self.play(Write(author))

        self.wait(2)

        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(author))
