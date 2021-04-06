from graphviz import Digraph
from graphviz.dot import Dot
import model

class FullGraphDotRenderer(object):
    """Renders the full graph into a graphviz.Digraph object"""

    def __init__(self, graph: model.Graph):
        super(FullGraphDotRenderer, self).__init__()
        self.graph = graph

    def render(self):
        dg = Digraph(comment='Skill Graph')
        for p in self.graph.people.values():
            dg.node(f'P{p.id}', p.name, shape="ellipse", color='lightblue', style='filled')
        for s in self.graph.skills.values():
            dg.node(f'S{s.id}', s.name, shape="rectangle", color='lightpink', style='filled')
        for p, s in self.graph.people_skills:
            dg.edge(f'P{p.id}', f'S{s.id}')
        return dg

class PNGRenderer(object):
    """Renders a graph in a PNG image file"""

    def __init__(self, dot_graph: Dot):
        super(PNGRenderer, self).__init__()
        self.dot_graph = dot_graph

    def render(self):
        return self.dot_graph.render(format="png", filename='./graph.dot', view=False)
