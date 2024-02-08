from flask import json, Blueprint
from werkzeug.exceptions import HTTPException


exp = Blueprint('exp', __name__)


@exp.app_errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()

    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response
