from manim import *

class UfmgGraph(Scene):
    def construct(self):
        vertices = [0, 1, 2, 3 , 4 , 5 , 6, 7 , 8, 9 , 10, 11, 12, 13 , 14 ,15, 16, 17 ,18, 19, 20, 21, 22, 23]
        edges = [(0, 1), (1,2), (1,5), (2,3), (2,5), (5,4),
                 (5,6), (6,7), (7,8),
                 (1,9), (9,10), (10,11),
                 (0,12), (12,13),
                 (0,14), (14,15),
                 (15,16), (0,16), (16,17), (17,18), (18,19), (19,20), (20,21),
                 (12,23), (11,22), (8,22)]
        
        lt = {0: [0, 0, 0], 
              1: [0, -0.5 , 0],
              2: [-0.5,-1,0],
              3: [-0.5,-1.5,0],
              4: [0,-1.5,0],
              5: [0, -1, 0],
              6: [0.5, -1 , 0],
              7: [1, -1.5, 0],
              8: [1.5, -1.5,0],
              9: [1.5, -0.5 , 0],
              10: [2, -0.5, 0],
              11: [2.5, -0.7, 0],
              12: [1.5, 0, 0],
              13: [2.5, 0.5, 0],
              14: [0, 1 , 0],
              15: [0, 1.5, 0],
              16: [-0.5, 0.3,0],
              17: [-0.7, 0,0],
              18: [-1, 0.5, 0],
              19: [-1.5,1,0],
              20: [-2,1,0],
              21: [-2.5,1,0],
              22: [2.3, -1,0],
              23: [3,0,0]
              }

        G = Graph(vertices, edges, layout=lt)

        label0 = Text("Praça de Serviços").scale(0.2).next_to(G[0], 0.3*UP+0.3*RIGHT)
        label1 = Text("ICEX").scale(0.2).next_to(G[1], 0.3*UP+0.3*RIGHT)
        label2 = Text("CAD3").scale(0.2).next_to(G[2], 0.3*LEFT)
        label3 = Text("DQ").scale(0.2).next_to(G[3], 0.3*LEFT)
        label4 = Text("COLTEC").scale(0.2).next_to(G[4], 0.3*DOWN)
        label5 = Text("EE").scale(0.2).next_to(G[5], 0.3*RIGHT+0.1*UP)
        label6 = Text("IGC").scale(0.2).next_to(G[6], 0.3*RIGHT)
        label7 = Text("RU1").scale(0.2).next_to(G[7], 0.3*DOWN)
        label8 = Text("FAE").scale(0.2).next_to(G[8], 0.3*RIGHT)
        label9 = Text("FACE").scale(0.2).next_to(G[9], 0.3*DOWN)
        label10 = Text("FAFICH").scale(0.2).next_to(G[10], 0.3*UP)
        label11 = Text("FALE").scale(0.2).next_to(G[11], 0.3*RIGHT)
        label12 = Text("Reitoria").scale(0.2).next_to(G[12], 0.3*DOWN+0.1*LEFT)
        label13 = Text("Música").scale(0.2).next_to(G[13], 0.3*RIGHT)
        label14 = Text("Biblioteca Central").scale(0.2).next_to(G[14], 0.3*RIGHT)
        label15 = Text("CAD1").scale(0.2).next_to(G[15], 0.3*UP)
        label16 = Text("ICB").scale(0.2).next_to(G[16], 0.3*UP+0.3*RIGHT)
        label17 = Text("RU2").scale(0.2).next_to(G[17], 0.3*DOWN)
        label18 = Text("Farmácia").scale(0.2).next_to(G[18], 0.3*LEFT)
        label19 = Text("MedVet").scale(0.2).next_to(G[19], 0.3*UP)
        label20 = Text("Odonto").scale(0.2).next_to(G[20],0.3*DOWN)
        label21 = Text("EEFFTO").scale(0.2).next_to(G[21],0.3*LEFT)
        label22 = Text("CAD2").scale(0.2).next_to(G[22], 0.3*RIGHT)
        label23 = Text("Belas").scale(0.2).next_to(G[23], 0.3*RIGHT)

        self.play(Create(G, run_time=5))
   
        self.play(Write(label0, run_time=0.2))
        self.play(Write(label1, run_time=0.2))
        self.play(Write(label2, run_time=0.2))
        self.play(Write(label3, run_time=0.2))
        self.play(Write(label4, run_time=0.2))
        self.play(Write(label5, run_time=0.2))
        self.play(Write(label6, run_time=0.2))
        self.play(Write(label7, run_time=0.2))
        self.play(Write(label8, run_time=0.2))
        self.play(Write(label9, run_time=0.2))
        self.play(Write(label10, run_time=0.2))
        self.play(Write(label11, run_time=0.2))
        self.play(Write(label12, run_time=0.2))
        self.play(Write(label13, run_time=0.2))
        self.play(Write(label14, run_time=0.2))
        self.play(Write(label15, run_time=0.2))
        self.play(Write(label16, run_time=0.2))
        self.play(Write(label17, run_time=0.2))
        self.play(Write(label18, run_time=0.2))
        self.play(Write(label19, run_time=0.2))
        self.play(Write(label20, run_time=0.2))
        self.play(Write(label21, run_time=0.2))
        self.play(Write(label22, run_time=0.2))
        self.play(Write(label23, run_time=0.2))

        self.play(FadeOut(G, run_time=2), FadeOut(label0, run_time=2), FadeOut(label1, run_time=2),
                  FadeOut(label2, run_time=2), FadeOut(label3, run_time=2), FadeOut(label4, run_time=2),
                  FadeOut(label5, run_time=2), FadeOut(label6, run_time=2), FadeOut(label7, run_time=2),
                  FadeOut(label8, run_time=2), FadeOut(label9, run_time=2), FadeOut(label10, run_time=2),
                  FadeOut(label11, run_time=2), FadeOut(label12, run_time=2), FadeOut(label13, run_time=2),
                  FadeOut(label14, run_time=2), FadeOut(label15, run_time=2), FadeOut(label16, run_time=2),
                  FadeOut(label17, run_time=2), FadeOut(label18, run_time=2), FadeOut(label19, run_time=2),
                  FadeOut(label20, run_time=2), FadeOut(label21, run_time=2), FadeOut(label22, run_time=2),
                  FadeOut(label23, run_time=2))
