from graphviz import Digraph, Graph
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

class WordCloudDotRenderer(object):
    """Renders a wordcloud into a graphviz.Graph object"""

    def __init__(self, graph: model.Graph):
        super(WordCloudDotRenderer, self).__init__()
        self.graph = graph

    def render(self):
        graph_attributes = [
            ('overlap', 'false'),
            ('layout', 'circo'),
            ('model', 'subset'),
        ]
        dg = Graph(comment='Skills Word Cloud', graph_attr=graph_attributes)
        font_sizes = WordCloudDotRenderer.calculate_font_size(self.graph)
        for s in self.graph.skills.values():
            dg.node(f'S{s.id}', s.name, shape='plaintext', fontsize=str(font_sizes[s.id]))
        return dg

    @staticmethod
    def calculate_font_size(graph: model.Graph, min_font_size: int = 8, max_font_size: int = 24):
        font_range = max_font_size - min_font_size
        max_people = 0
        # Find the skill with the most people
        for skill in graph.skills.values():
            max_people = max(max_people, len(skill.people))
        # Create map with skill id and its normalized prominence
        font_sizes_map = {}
        for skill in graph.skills.values():
            # Value between 0 and 1
            normalized = (len(skill.people) * 100) / max_people
            # Font size between min and max relative to how many people
            font_sizes_map[skill.id] = int(normalized * font_range) + min_font_size
        return font_sizes_map

class PNGRenderer(object):
    """Renders a graph in a PNG image file"""

    def __init__(self, dot_graph: Dot):
        super(PNGRenderer, self).__init__()
        self.dot_graph = dot_graph

    def render(self, path_prefix: str = './graph.dot'):
        return self.dot_graph.render(format="png", filename=path_prefix, view=False)
