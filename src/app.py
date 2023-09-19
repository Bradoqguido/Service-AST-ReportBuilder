from flask import Flask, request, Response
from services.auth import Auth
from services.functions import Functions

app = Flask(__name__)

@app.route('/report', methods=['POST'])
def generate_pdf():
    # Check the Bearer token for authentication
    token = request.headers.get('Authorization')
    auth = Auth(token)
    function = Functions()

    # Check the token against a stored value or authentication system
    if not auth.verify_token():
        return {'message': 'Unauthorized'}, 401

    # Receive the JSON-based AST from the request
    json_data = request.get_json()

    # Build the AST from JSON
    ast = function.build_ast_from_json(json_data)

    # Generate the PDF based on the AST
    pdf_buffer = function.generate_pdf_from_ast(ast)

    # Serve the PDF as a downloadable file
    return Response(pdf_buffer.read(),
                    content_type='application/pdf',
                    headers={'Content-Disposition': 'attachment; filename=report.pdf'})

if __name__ == '__main__':
    app.run(debug=True, port=3011)
