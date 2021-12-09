from graphviz import Digraph, Graph
from graphviz.dot import Dot
import model

class RenderConstants:
    CLOUD_FONT = "Source Serif Pro"
    ELLIPSE_COLOR = "#B66AD6"
    RECTANGLE_COLOR = "#FF3864"

class FullGraphDotRenderer(object):
    """Renders the full graph into a graphviz.Digraph object"""

    def __init__(self, graph: model.Graph):
        super(FullGraphDotRenderer, self).__init__()
        self.graph = graph

    def render(self):
        graph_attributes = [
            ('overlap', 'false'),
            ('layout', 'sfdp'),
            ('ranksep', '3'),
            ('bgcolor', 'black'),
            ('K', '0.6'),
            ('repulsiveforce', '1.5'),
            ('fontname', RenderConstants.CLOUD_FONT),
        ]
        edge_attributes = [
            ('color', 'white'),
            ('fontname', RenderConstants.CLOUD_FONT),
        ]
        node_attributes = [
            ('fontname', RenderConstants.CLOUD_FONT),
        ]
        font_sizes = WordCloudDotRenderer.calculate_font_size(self.graph)
        dg = Digraph(comment='Skill Graph', graph_attr=graph_attributes, edge_attr=edge_attributes, node_attr=node_attributes)
        for p in self.graph.people.values():
            dg.node(f'P{p.id}', p.name, shape="ellipse", color=RenderConstants.ELLIPSE_COLOR, style='filled')
        for s in self.graph.skills.values():
            dg.node(f'S{s.id}', s.name, shape="rectangle", color=RenderConstants.RECTANGLE_COLOR, style='filled', fontsize=str(font_sizes[s.id]))
        for p, s in self.graph.people_skills:
            dg.edge(f'P{p.id}', f'S{s.id}')
        return dg

class SubGraphDotRenderer(object):
    """Renders a partial graph into a graphviz.Digraph object"""

    def __init__(self, graph: model.Graph):
        super(SubGraphDotRenderer, self).__init__()
        self.graph = graph

    def render(self):
        graph_attributes = [
            ('overlap', 'false'),
            ('layout', 'sfdp'),
            ('ranksep', '3'),
            ('bgcolor', 'black'),
            ('K', '0.6'),
            ('repulsiveforce', '1.5'),
            ('fontname', RenderConstants.CLOUD_FONT),
        ]
        edge_attributes = [
            ('color', 'white'),
            ('fontname', RenderConstants.CLOUD_FONT),
        ]
        node_attributes = [
            ('fontname', RenderConstants.CLOUD_FONT),
        ]
        dg = Graph(comment='Skill Graph', graph_attr=graph_attributes, edge_attr=edge_attributes, node_attr=node_attributes)
        for p in self.graph.people.values():
            dg.node(f'P{p.id}', p.name, shape="ellipse", color=RenderConstants.ELLIPSE_COLOR, style='filled')
        for s in self.graph.skills.values():
            dg.node(f'S{s.id}', s.name, shape="rectangle", color=RenderConstants.RECTANGLE_COLOR, style='filled')
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
            ('fontname', RenderConstants.CLOUD_FONT),
        ]
        node_attributes = [
            ('fontname', RenderConstants.CLOUD_FONT),
        ]
        dg = Graph(comment='Skills Word Cloud', graph_attr=graph_attributes, node_attr=node_attributes)
        font_sizes = WordCloudDotRenderer.calculate_font_size(self.graph)
        for s in self.graph.skills.values():
            dg.node(f'S{s.id}', s.name, shape='plaintext', fontsize=str(font_sizes[s.id]))
        return dg

    @staticmethod
    def calculate_font_size(graph: model.Graph, min_font_size: int = 14, max_font_size: int = 36):
        font_range = max_font_size - min_font_size
        max_people = 0
        # Find the skill with the most people
        for skill in graph.skills.values():
            max_people = max(max_people, len(skill.people))
        # Create map with skill id and its normalized prominence
        font_sizes_map = {}
        for skill in graph.skills.values():
            # Value between 0 and 1, non-linear
            normalized = (len(skill.people) / max_people)**2
            # Font size between min and max relative to how many people
            font_size = int(normalized * font_range) + min_font_size
            font_sizes_map[skill.id] = font_size
            # print(f'{skill.name}: {len(skill.people)} (max: {max_people}) -> {normalized} -> {font_size}')
        return font_sizes_map

class ImageFileRenderer(object):
    """Renders a graph into an image file"""

    def __init__(self, dot_graph: Dot):
        super(ImageFileRenderer, self).__init__()
        self.dot_graph = dot_graph

    def render(self, path_prefix: str = './graph.dot', image_format: str = 'jpg'):
        return self.dot_graph.render(format=image_format, filename=path_prefix, view=False)
