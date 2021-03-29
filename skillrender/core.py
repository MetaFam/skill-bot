from skillgraph import SkillGraph
from graphviz import Digraph

class DotRenderer(object):
    """Renders a graph into a graphviz.Digraph object"""

    def __init__(self, skill_graph: SkillGraph):
        super(DotRenderer, self).__init__()
        self.skill_graph = skill_graph

    def render(self):
        dg = Digraph(comment='Skill Graph')
        for pid, pname in self.skill_graph.people.items():
            dg.node(f'P{pid}', pname, shape="ellipse")
        for sid, sname in self.skill_graph.skills.items():
            dg.node(f'S{sid}', sname, shape="rectangle")
        for sid, pid in self.skill_graph.people_skills:
            dg.edge(f'P{pid}', f'S{sid}')
        return dg

class PNGRenderer(object):
    """Renders a graph in a PNG image file"""

    def __init__(self, skill_graph: SkillGraph):
        super(PNGRenderer, self).__init__()
        self.skill_graph = skill_graph

    def render(self):
        dot = DotRenderer(self.skill_graph).render()
        return dot.render(format="png", filename='./graph.dot', view=False)
