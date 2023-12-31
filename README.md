### Version 0.1.7

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
- *settings*: object
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
      - *children*
        - table_cell
        - *content*: string
        - *settings*: object
- `list`
  - *content*: string[]
  - *children*
    - line_row
      - *content*: string[]
- `page-break`

The example payload is already tested, and it's the structure of the pdf document. 
```json
{
  "node_type": "document",
  "settings": {
    "orientation": "landscape"
  },
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
      "content": ["It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."],
      "settings": {
        "spaceAfter": 20
      }
    },

    {
      "node_type": "table",
      "content": ["Sensor", "Data", "Day", "Sensor 1", "Sensor 2", "Sensor 3", "Sensor 3"],
      "settings": {
        "colWidth": 100,
        "rowHeight": 16,
        "colHeaderBackgroundColor": "#ffffff",
        "colHeaderTextColor": "#000000",
        "colHeaderTextAlign": "CENTER",
        "rowHeaderBackgroundColor": "#ffffff",
        "rowHeaderTextColor": "#000000",
        "rowHeaderTextAlign": "CENTER",
        "colHeaderFontName": "Helvetica-Bold",
        "rowHeaderFontName": "Times-Bold",
        "spaceAfter": 20
      },
      "children": [
        {
          "node_type": "table_row",
          "content": [],
          "children": [
            {
              "node_type": "table_cell",
              "content": "Row 1"
            },
            {
              "node_type": "table_cell",
              "content": "Value 1"
            },
            {
              "node_type": "table_cell",
              "content": "1",
              "settings": {
                "cellTextColor": "#FF0000"
              }
            },
            {
              "node_type": "table_cell",
              "content": "2",
              "settings": {
                "cellTextColor": "#FF0000"
              }
            },
            {
              "node_type": "table_cell",
              "content": "3",
              "settings": {
                "cellTextColor": "#FF0000"
              }
            },
            {
              "node_type": "table_cell",
              "content": "4",
              "settings": {
                "cellTextColor": "#FF0000"
              }
            },
            {
              "node_type": "table_cell",
              "content": "Value 1",
              "settings": {
                "cellBackgroundColor": "#03ff45"
              }
            }
          ]
        },
        {
          "node_type": "table_row",
          "content": [],
          "children": [
            {
              "node_type": "table_cell",
              "content": "Row 2"
            },
            {
              "node_type": "table_cell",
              "content": "Value 2"
            },
            {
              "node_type": "table_cell",
              "content": "1",
              "settings": {
                "cellTextColor": "#FF0000"
              }
            },
            {
              "node_type": "table_cell",
              "content": "2",
              "settings": {
                "cellTextColor": "#FF0000"
              }
            },
            {
              "node_type": "table_cell",
              "content": "3",
              "settings": {
                "cellTextColor": "#FF0000"
              }
            },
            {
              "node_type": "table_cell",
              "content": "4",
              "settings": {
                "cellTextColor": "#FF0000"
              }
            },
            {
              "node_type": "table_cell",
              "content": "Value 1"
            }
          ]
        },
        {
          "node_type": "table_row",
          "content": [],
          "children": [
            {
              "node_type": "table_cell",
              "content": "Row 3"
            },
            {
              "node_type": "table_cell",
              "content": "Value 3",
              "settings": {
                "cellBackgroundColor": "#035f45"
              }
            },
            {
              "node_type": "table_cell",
              "content": "1",
              "settings": {
                "cellTextColor": "#FF0000"
              }
            },
            {
              "node_type": "table_cell",
              "content": "2",
              "settings": {
                "cellTextColor": "#FF0000"
              }
            },
            {
              "node_type": "table_cell",
              "content": "3",
              "settings": {
                "cellTextColor": "#FF0000"
              }
            },
            {
              "node_type": "table_cell",
              "content": "4",
              "settings": {
                "cellTextColor": "#FF0000"
              }
            },
            {
              "node_type": "table_cell",
              "content": "Value 1"
            }
          ]
        },
        {
          "node_type": "table_row",
          "content": [],
          "children": [
            {
              "node_type": "table_cell",
              "content": "Row 4"
            },
            {
              "node_type": "table_cell",
              "content": "Value 4"
            },
            {
              "node_type": "table_cell",
              "content": "1",
              "settings": {
                "cellTextColor": "#FF0000"
              }
            },
            {
              "node_type": "table_cell",
              "content": "2",
              "settings": {
                "cellTextColor": "#FF0000",
                "cellBackgroundColor": "#071f61"
              }
            },
            {
              "node_type": "table_cell",
              "content": "3",
              "settings": {
                "cellTextColor": "#FF0000"
              }
            },
            {
              "node_type": "table_cell",
              "content": "4",
              "settings": {
                "cellTextColor": "#FF0000"
              }
            },
            {
              "node_type": "table_cell",
              "content": "Value 1"
            }
          ]
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
        "colHeaderFontName": "Helvetica-Bold",
        "cellTextAlign": "CENTER",
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
      "node_type": "page-break"
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
    },
    {
      "node_type": "page-break"
    },
    {
      "node_type": "pie-chart",
      "settings": {
        "chartTitle": "Pie Graph of most used words"
      },
      "content": [{
        "chartLabels": ["a","b","c","d","e","f"]
      },{
        "chartData": [10,20,30,40,50,60]
      }
      ]
    }
  ]
}
```

# Future improvements
- more graphs