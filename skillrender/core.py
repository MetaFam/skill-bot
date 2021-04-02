from repository import SqliteRepository
from graphviz import Digraph

class DotRenderer(object):
    """Renders a graph into a graphviz.Digraph object"""

    def __init__(self, repo: SqliteRepository):
        super(DotRenderer, self).__init__()
        self.repo = repo

    def render(self):
        dg = Digraph(comment='Skill Graph')
        for pid, pname in self.repo.get_people():
            # print(f"🎨 Person {pname} (P{pid})")
            dg.node(f'P{pid}', pname, shape="ellipse")
        for sid, sname in self.repo.get_skills():
            # print(f"🎨 Skill {sname} (S{sid})")
            dg.node(f'S{sid}', sname, shape="rectangle")
        for pid, sid in self.repo.get_people_skills():
            # print(f"🎨 Connect P{pid} S{sid}")
            dg.edge(f'P{pid}', f'S{sid}')
        return dg

class PNGRenderer(object):
    """Renders a graph in a PNG image file"""

    def __init__(self, repo: SqliteRepository):
        super(PNGRenderer, self).__init__()
        self.repo = repo

    def render(self):
        dot = DotRenderer(self.repo).render()
        return dot.render(format="png", filename='./graph.dot', view=False)
