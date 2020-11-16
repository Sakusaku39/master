from graphviz import Digraph
import nlp100_41
data = nlp100_41.C_contact();

'''
G = Digraph(format="png")
G.attr("node", shape="circle")
edges = [(0, 1), (0, 95), (1, 2), (1, 4), (1, 94), (2, 3), (4, 5), (4, 92), (5, 6),
(6, 7), (6, 79), (6, 90), (6, 91), (7, 8), (7, 34), (7, 76), (7, 78), (8, 9), (8, 10), (8, 11),
(11, 12), (12, 13), (12, 28), (12, 29), (13, 14), (13, 21), (13, 25), (13, 26), (14, 15), (14, 17), (14, 18), (14, 20),
(15, 16), (18, 19), (21, 22), (21, 24), (22, 23), (26, 27), (29, 30), (30, 31), (31, 32), (31, 33),
(34, 35), (34, 70), (34, 71), (34, 72), (35, 36), (35, 37), (35, 56), (35, 64), (37, 38), (37, 53), (37, 55),
(38, 39), (39, 40), (40, 41), (40, 44), (40, 47), (40, 51), (40, 52), (41, 42), (42, 43), (44, 45), (44, 46),
(47, 48), (48, 49), (49, 50), (53, 54), (56, 57), (57, 58), (57, 59), (59, 60), (60, 61), (60, 62), (60, 63),
(64, 65), (64, 66), (66, 67), (66, 69), (67, 68), (72, 73), (73, 74), (74, 75), (76, 77), (79, 80), (80, 81), (80, 87),
(81, 82), (81, 86), (82, 83), (82, 84), (82, 85), (87, 88), (88, 89), (92, 93), (95, 96), (95, 98), (96, 97),
(98, 99), (98, 100), (98, 101), (101, 102), (102, 103), (103, 104), (103, 105), (105, 106), (105, 107), (105, 108)]
for i,j in edges:
    G.edge(str(i), str(j))
G.render("tree")
G.view()

与えられた文の係り受け木を有向グラフとして可視化せよ．
'''
relations = []
for chunk in data[2]:
  if int(chunk.dst) != -1:
    source = ''.join([morph.surface if morph.pos != '記号' else '' for morph in chunk.morphs])
    destination = ''.join([morph.surface if morph.pos != '記号' else '' for morph in data[2][int(chunk.dst)].morphs])
    relation = [source, destination]
    relations.append(relation)

rel_gra = Digraph(format='png')
rel_gra.attr('node', shape='circle')
for sour, dest in relations:
    rel_gra.edge(sour, dest)
rel_gra.render("tree")
rel_gra.view()
