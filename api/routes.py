from flask import Blueprint, request, jsonify

api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def index():
    return api_bp.send_static_file('index.html')

@api_bp.route('/api/ask', methods=['POST'])
def ask_question():
    try:
        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({'error': 'No question provided'}), 400
            
        question = data['question']
        answer = api_bp.chat_chain.invoke({"input": question})["answer"]
        
        return jsonify({
            'answer': answer,
            'status': 'success'
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@api_bp.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'API is running'
    })