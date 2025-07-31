# vuln_app_clean.py
from flask import Flask, request, jsonify
import ast

app = Flask(__name__)

@app.route('/api/v1/validate/code', methods=['POST'])
def validate_code():
    data = request.get_json(force=True)
    source = data.get('code', '')
    try:
        # Validate Python syntax first
        ast.parse(source)

        # Compile and execute the code
        exec_globals = {}
        exec(compiled := compile(source, '<input>', 'exec'), exec_globals)

        # If the user payload stored command output in 'result', return it
        output = exec_globals.get('result', '')
        return jsonify({'status': 'ok', 'output': output}), 200

    except Exception as e:
        # Return the error if something goes wrong, with 400
        return jsonify({'status': 'error', 'error': str(e).strip()}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

