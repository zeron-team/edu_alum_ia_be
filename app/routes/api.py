from flask import Blueprint, jsonify, request, current_app
from app.services.openai_service import generar_explicacion

api_bp = Blueprint('api', __name__)

@api_bp.route('/explicacion', methods=['POST'])
def obtener_explicacion():
    data = request.json
    tema = data.get('tema')
    nivel = data.get('nivel')
    area = data.get('area')
    explicacion = generar_explicacion(nivel, area, tema)
    return jsonify({'explicacion': explicacion})
