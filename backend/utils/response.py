from flask import jsonify

def success_response(data=None, message="Success", status_code=200):
    """
    Constructs a standardized success JSON response.
    """
    response = {
        "status": "success",
        "message": message
    }
    if data is not None:
        response["data"] = data
        
    return jsonify(response), status_code

def error_response(message="An error occurred", status_code=400, details=None):
    """
    Constructs a standardized error JSON response.
    """
    response = {
        "status": "error",
        "message": message
    }
    if details is not None:
        response["details"] = details
        
    return jsonify(response), status_code
