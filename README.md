### Version 0.1.0

# Service-AST-ReportBuilder
This service is a Report Builder that uses Abstract Syntax Tree (AST) as JSON pseudocode to generate reports and graphs.

Uses mostly the lib `reportlab` to build the report from the AST and flask to expose the service to the internet.

# Activate your V-env
Run this command to activate the venv: `source .venv/bin/activate`.

If you don't have the venv installed, run: `python3 -m venv .venv` and then activate it.

# How to use

This code is created using **Python 3**

Install the service dependencies with the command: `pip3 install -U -r requirements.txt`

Run the service with the command: `python3 service.py`

# Abstract Syntax Tree (AST)

This document is oriented by node and their content, settings and children.

the root node is `document` <br>
the children nodes are:
- `paragraph`
  - *content*: string
- `horizontal-line-chart`
  - *content*: string
- `table`
  - *content*: string[] # table headers
  - *children*
    - table_row
      - *content*: [] # row values

The example payload is already tested, and it's the structure of the pdf document. 
```json
{
  "node_type": "document",
  "content": [],
  "children": [
    {
      "node_type": "paragraph",
      "content": ["This is a sample PDF generated using an AST."],
      "children": []
    },
    {
      "node_type": "horizontal-line-chart",
      "settings": {
          "pltWidth": 400,
          "pltHeight": 200
      },
      "content": [{
          "xlabel": "X-axis",
          "xdata": ["jan","feb","mar","abr","mai","jun"]
        },{
          "ylabel": "Y-axis",
          "ydata": [
              {
                  "data": [13, 5, 20, 22, 37, 45]
              }, 
              {
                  "data": [5, 20, 46, 38, 23, 21]
              }
           ]
        }
      ],
      "children": []
    },
    {
      "node_type": "paragraph",
      "content": ["This is a sample PDF generated using an AST."],
      "children": []
    },
    {
      "node_type": "table",
      "content": ["Sensor", "Data", "Day"],
      "settings": {
          "colWidth": 100,
          "rowHeights": 16,
          "backgroundColor": "#fff6ff",
          "gridColor": "#fffff0"
      },
      "children": [
        {
          "node_type": "table_row",
          "content": ["Sensor 1", "Value 1", 1],
          "children": []
        },
        {
          "node_type": "table_row",
          "content": ["Sensor 2", "Value 2", 2],
          "children": []
        },
        {
          "node_type": "table_row",
          "content": ["Sensor 3", "Value 3", 3],
          "children": []
        },
        {
          "node_type": "table_row",
          "content": ["Sensor 4", "Value 4", 4],
          "children": []
        }
      ]
    }
  ]
}
```

# Future improvements
- text types (like title, subtitle, caption)
- more settings definitions
- more graphs
- docker container configuration (setup as cloud service)