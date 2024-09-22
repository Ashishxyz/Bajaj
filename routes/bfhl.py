from flask import Blueprint, request, jsonify
from utils.parser import parse_data
from utils.file_handler import validate_file

bfhl_api = Blueprint('bfhl_api', __name__)

# POST route handling JSON and file processing
@bfhl_api.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.get_json()
    user_id = "your_user_id"

    # Parse input arrays
    numbers, alphabets, highest_lowercase = parse_data(data['data'])

    # Validate the file
    file_valid, mime_type, file_size = validate_file(data.get('file_b64'))

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": "youremail@example.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase,
        "file_valid": file_valid,
        "file_mime_type": mime_type,
        "file_size_kb": file_size
    }

    return jsonify(response)

# GET route that returns an operation code
@bfhl_api.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1})
