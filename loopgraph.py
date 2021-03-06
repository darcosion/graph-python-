from graph_tool.all import *

for t in range(1, 51):
    g = Graph()
    for i in range(0, t):
        g.add_vertex()

    for i in range(g.num_vertices()):
        for e in range(g.num_vertices()):
            if(i != e):
                g.add_edge(g.vertex(i), g.vertex(e))
    graph_draw(g, vertex_text=g.vertex_index, vertex_font_size=18,
               output_size=(800, 800), output="result/result"+str(t)+".png")

