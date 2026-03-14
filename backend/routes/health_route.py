from flask import Blueprint
from utils.response import success_response

health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    """
    Simple health check endpoint to verify the API is running.
    """
    return success_response(
        message="Dany API is healthy and running",
        data={"version": "1.0.0"}
    )
