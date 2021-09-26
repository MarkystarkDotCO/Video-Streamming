from flask import Blueprint

payment_bp = Blueprint('payment',__name__)

@payment_bp.route('/')
def index():
    return "payment homepage"
