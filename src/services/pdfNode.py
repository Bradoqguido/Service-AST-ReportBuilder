# Define a placeholder class for the PDFNode
class PDFNode:
    def __init__(self, node_type, content=None, settings=None, children=None):
        self.node_type = node_type
        self.content = content if content is not None else []
        self.settings = settings if settings is not None else {
            "colWidth": 100,
            "rowHeight": 16,
            "colHeaderBackgroundColor": "#ffffff",
            "colHeaderTextColor": "#000000",
            "colHeaderTextAlign": "CENTER",
            "rowHeaderBackgroundColor": "#ffffff",
            "rowHeaderTextColor": "#000000",
            "rowHeaderTextAlign": "CENTER",
            "cellBackgroundColor": "#ffffff",
            "cellTextColor": "#000000",
            "cellGridColor": "#000000",
            "cellTextAlign": "CENTER",
            "colHeaderFontName": "Helvetica-Bold",
            "rowHeaderFontName": "Times-Bold",
            "cellFontName": "Helvetica",
            "listColSpam": 6,
            "chartTitle": "",
            "chartWidth": 400,
            "chartHeight": 300,
        }
        self.children = children if children is not None else []

        # Merge JSON settings with explicit settings if both are provided
        if settings is not None:
            self.settings.update(settings)
    def add_child(self, child_node):
        self.children.append(child_node)

    def add_content(self, content):
        self.content.append(content)
