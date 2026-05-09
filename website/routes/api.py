from flask import Blueprint, request, jsonify

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/evaluate', methods=['POST'])
def evaluate_image():

    if 'file' not in request.files:
        return jsonify({"error": "Ingen fil hittades"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "Ingen fil är vald ännu"}), 400

    
    mock_data = {
        "success": True,
        "animal": "Gyllene Retriever",
        "accuracy": "98%",
        "fact": "Denna hundras är känd för att vara väldigt samarbetsvillig och vänlig."
    }
    
    return jsonify(mock_data)