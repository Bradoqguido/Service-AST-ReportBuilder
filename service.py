from flask import Flask, request, Response
from io import BytesIO
import json
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing, String, PolyLine
from reportlab.graphics.charts.linecharts import HorizontalLineChart

app = Flask(__name__)

# Define a function to build an AST from JSON data
def build_ast_from_json(json_data, explicit_settings=None):
    try:
        ast_data = json.loads(json_data)
        if not isinstance(ast_data, dict):
            raise ValueError("Invalid JSON data format. Expected a dictionary at the root.")

        # Merge explicit settings if provided
        if explicit_settings:
            ast_data["settings"] = explicit_settings

        def build_node(node_data):
            node_type = node_data.get("node_type")
            if not node_type:
                raise ValueError("Missing 'node_type' in node data.")

            # Pass settings to each node if available
            settings = node_data.get("settings")
            if settings:
                node = PDFNode(node_type, settings=settings)
            else:
                node = PDFNode(node_type)

            node.content = node_data.get("content", [])
            node.children = [build_node(child_data) for child_data in node_data.get("children", [])]
            return node

        return build_node(ast_data)

    except (json.JSONDecodeError, ValueError) as e:
        raise ValueError(f"Error parsing JSON data: {str(e)}")

# Define a function to generate a PDF from an AST
def generate_pdf_from_ast(node):
    buffer = BytesIO()

    # Create a PDF document
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Define styles for the PDF
    styles = getSampleStyleSheet()

    # Initialize a list to store the elements (e.g., paragraphs, tables) in the PDF
    elements = []

    # Implement PDF generation logic based on the AST structure
    def render_node(node):
        if node.node_type == 'paragraph':
            # Add a paragraph to the PDF
            elements.append(Paragraph(node.content[0], styles['Normal']))
        elif node.node_type == 'table':
            # Construct a data list for the table
            table_data = [node.content]  # Header row
            for row_node in node.children:
                table_data.append(row_node.content)  # Data rows

            # Create a table and set its style
            table = Table(table_data, colWidths=node.settings.get('colWidth', 100), rowHeights=node.settings.get('rowHeights', 16))

            # Define styles for the column headers, row headers, and table body
            col_header_style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Font for column headers
            ])

            row_header_style = TableStyle([
                ('BACKGROUND', (0, 1), (0, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('FONTNAME', (0, 1), (0, -1), 'Times-Bold'),  # Font for row headers (excluding the first column)
            ])

            table_body_style = TableStyle([
                ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Grid for the table body
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),  # Font for the table body
            ])

            # Apply the styles to the table
            table.setStyle(table_body_style)
            table.setStyle(col_header_style)
            table.setStyle(row_header_style)

            spacer = Spacer(1, 20)  # 20 points of space

            # Add the spacer before the table
            elements.append(spacer)

            # Add the table to the PDF
            elements.append(table)

            # Add the spacer after the table
            elements.append(spacer)
        elif node.node_type == 'pie-chart':
            # Initialize data for the graph
            xlabel = node.content[0].get("xlabel", None)
            xdata = node.content[0].get("xdata", None)
            ylabel = node.content[1].get("ylabel", None)
            ydata = node.content[1].get("ydata", None)

            pltTitle = node.settings.get('pltTitle', '')

            if xlabel is None or ylabel is None or xdata is None or ydata is None:
                raise ValueError("Invalid graph data in the AST")

            # Convert the data to the required format
            data = [(str(label), int(value)) for label, value in zip(xdata, ydata)]

            # Create a drawing for the chart
            chart = Drawing(400, 200)
            pie = Pie()
            pie.x = 150
            pie.y = 50
            pie.width = 100
            pie.height = 100
            pie.data = data
            pie.labels = [String(0, 0, label) for label, _ in data]

            chart.add(pie)

            # Add a title to the chart
            title = String(200, 175, pltTitle)
            title.fontName = 'Helvetica-Bold'
            title.fontSize = 14
            chart.add(title)

            # Add the chart to the PDF elements
            elements.append(chart)
        elif node.node_type == 'horizontal-line-chart':
            # Initialize data for the graph
            xlabel = node.content[0].get("xlabel", None)
            xdata = node.content[0].get("xdata", None)
            ylabel = node.content[1].get("ylabel", None)
            ydata = node.content[1].get("ydata", None)
            pltWidth = node.settings.get('pltWidth', 400)
            pltHeight = node.settings.get('pltHeight', 300)

            if xlabel is None or ylabel is None or xdata is None or ydata is None:
                raise ValueError("Invalid graph data in the AST")

            # Create a drawing for the chart
            chart = Drawing(pltWidth, pltHeight)

            # Get the data from x-axis
            data = []
            minValue = float('inf')  # Initialize minValue to positive infinity
            maxValue = float('-inf')  # Initialize maxValue to negative infinity
            for row in ydata:
                max_in_row = max(row.get("data"))
                min_in_row = min(row.get("data"))
                if max_in_row > maxValue:
                    maxValue = max_in_row
                if min_in_row < minValue:
                    minValue = min_in_row
                data.append(tuple(row.get("data")))

            # Calculate the range of values
            valueRange = maxValue - minValue

            # Determine an appropriate valueStep based on the range and desired number of intervals
            desiredIntervals = 10  # Adjust this number as needed
            valueStep = valueRange / desiredIntervals

            # Create a horizontal line plot
            lc = HorizontalLineChart()
            lc.y = 50
            lc.x = 50
            lc.height = 125
            lc.width = 300
            lc.data = data
            lc.joinedLines = 1
            lc.categoryAxis.categoryNames = xdata
            lc.categoryAxis.labels.boxAnchor = 'n'
            lc.valueAxis.valueMin = 0 # Min value is always 0
            lc.valueAxis.valueMax = maxValue
            lc.valueAxis.valueStep = valueStep
            lc.lines[0].strokeWidth = 1
            lc.lines[1].strokeWidth = 1
            chart.add(lc)

            # Add the chart to the PDF elements
            elements.append(chart)

        for child in node.children:
            render_node(child)

    # Start rendering
    render_node(node)

    # Build the PDF document
    doc.build(elements)

    buffer.seek(0)
    return buffer

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

# Placeholder function to verify the Bearer token
def verify_token(token):
    # Replace this with your token verification logic
    return token == 'Bearer YOUR_AUTH_TOKEN'

@app.route('/report', methods=['POST'])
def generate_pdf():
    # Check the Bearer token for authentication
    #token = request.headers.get('Authorization')

    # Check the token against a stored value or authentication system
    #if not verify_token(token):
    #    return jsonify({'message': 'Unauthorized'}), 401

    # Receive the JSON-based AST from the request
    ast_json = request.get_json()

    # Build the AST from JSON
    ast = build_ast_from_json(json.dumps(ast_json))

    # Generate the PDF based on the AST
    pdf_buffer = generate_pdf_from_ast(ast)

    # Serve the PDF as a downloadable file
    return Response(pdf_buffer.read(),
                    content_type='application/pdf',
                    headers={'Content-Disposition': 'attachment; filename=report.pdf'})

if __name__ == '__main__':
    app.run(debug=True, port=3011)
