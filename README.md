### Version 0.1.5

# Service-AST-ReportBuilder
This service is a Report Builder that uses Abstract Syntax Tree (AST) as JSON pseudocode to generate reports and graphs.

Uses mostly the lib `reportlab` to build the report from the AST and flask to expose the service to the internet.

# Activate your V-env
Run this command to activate the venv: `source venv/bin/activate`.

If you don't have the venv installed, run: `python3 -m venv venv` and then activate it.

# How to use

This code is created using **Python 3**

Install the service dependencies with the command: `pip3 install -U -r requirements.txt`

Run the service with the command: `python3 service.py`

# Docker commands
Build container: `docker-compose -f docker-compose.yml build`
Run container: `docker-compose -f docker-compose.yml up`

# Abstract Syntax Tree (AST)

This document is oriented by node and their content, settings and children.

the root node is `document` <br>
the children nodes are:
- `title`
  - *content*: string
  - *settings*: object
- `paragraph`
  - *content*: array
    - *chartXData*: array
    - *chatYData*: array
      - *row*: array
  - *settings*: object
- `horizontal-line-chart`
  - *content*: array
    - *chartXData*: array
    - *chatYData*: array
      - *row*: array
  - *settings*: object
- `table`
  - *content*: string[]
  - *children*
    - table_row
      - *content*: []
- `list`
  - *content*: string[]
  - *children*
    - line_row
      - *content*: string[]

The example payload is already tested, and it's the structure of the pdf document. 
```json
{
  "node_type": "document",
  "children": [
    {
      "node_type": "title",
      "content": ["This is a AST Report."],
      "settings": {
        "spaceAfter": 20
      }
    },
    {
      "node_type": "paragraph",
      "content": ["It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."]
    },
    {
      "node_type": "table",
      "content": ["Sensor", "Data", "Day", "Sensor 1", "Sensor 2", "Sensor 3"],
      "settings": {
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
        "cellFontName": "Helvetica"
      },
      "children": [
        {
          "node_type": "table_row",
          "content": ["Sensor 1", "Value 1", 1,2,3,4]
        },
        {
          "node_type": "table_row",
          "content": ["Sensor 2", "Value 2", 2,2,3,4]
        },
        {
          "node_type": "table_row",
          "content": ["Sensor 3", "Value 3", 3,2,3,4]
        },
        {
          "node_type": "table_row",
          "content": ["Sensor 4", "Value 4", 4,2,3,4]
        }
      ]
    },
    {
      "node_type": "list",
      "content": ["Sensors"],
      "settings": {
        "colWidth": 100,
        "rowHeight": 16,
        "cellBackgroundColor": "#ffffff",
        "cellTextColor": "#000000",
        "cellGridColor": "#ffffff",
        "listColSpam": 6,
        "colHeaderTextAlign": "CENTER",
        "cellTextAlign": "LEFT",
        "cellFontName": "Helvetica"
      },
      "children": [
        {
          "node_type": "line_row",
          "content": ["It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."]
        },
        {
          "node_type": "line_row",
          "content": ["It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."]
        },
        {
          "node_type": "line_row",
          "content": ["It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."]
        },
        {
          "node_type": "line_row",
          "content": ["It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."]
        }
      ]
    },
    {
      "node_type": "horizontal-line-chart",
      "settings": {
        "chartWidth": 400,
        "chartHeight": 200,
        "chartTitle": "Graph of most used words",
        "spaceBefore": 20
      },
      "content": [{
        "chartXData": ["1","2","3","4","5","6"]
      },{
        "chatYData": [
          {
            "row": [13, 5, 20, 22, 37, 45]
          },
          {
            "row": [5, 20, 46, 38, 23, 21]
          },
          {
            "row": [32, 0, 15, 30, 32.5, 33]
          },
          {
            "row": [22, 16, 15, 30, 33.5, 7]
          }
        ]
      }
      ]
    }
  ]
}
```

# Future improvements
- more graphs