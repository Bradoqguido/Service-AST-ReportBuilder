import json

# Define a placeholder class for the PDFNode
class PDFNode:
    def __init__(self, node_type, content=None, settings=None, children=None):
        self.node_type = node_type
        self.content = content if content is not None else []
        self.settings = settings if settings is not None else {
            "colWidth": 100,
            "rowHeights": 16,
            "backgroundColor": "#ffffff",
            "gridColor": "#ffffff",
            "pltTitle": "",
            "pltWidth": 400,
            "pltHeight": 300,
        }
        self.children = children if children is not None else []

        # Merge JSON settings with explicit settings if both are provided
        if settings is not None:
            self.settings.update(settings)
    def add_child(self, child_node):
        self.children.append(child_node)

    def add_content(self, content):
        self.content.append(content)
