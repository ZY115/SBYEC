"""
Flask API for SBYEC Chatbot
Provides REST API endpoints for web integration
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from rag_chatbot_web_ready import SBYECChatbotWebReady
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for web integration

# Initialize chatbot (singleton)
chatbot = None


def get_chatbot():
    """Get or create chatbot instance"""
    global chatbot
    if chatbot is None:
        chatbot = SBYECChatbotWebReady(data_directory="data")
    return chatbot


@app.route('/')
def home():
    """Health check endpoint"""
    return jsonify({
        'status': 'online',
        'service': 'SBYEC Chatbot API',
        'version': '1.0',
        'timestamp': datetime.now().isoformat()
    })


@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Main chat endpoint

    Expected JSON body:
    {
        "question": "What programs do you offer?",
        "auto_refresh": false  (optional)
    }

    Returns:
    {
        "answer": "...",
        "timestamp": "..."
    }
    """
    try:
        data = request.get_json()

        if not data or 'question' not in data:
            return jsonify({
                'error': 'Missing required field: question'
            }), 400

        question = data['question'].strip()
        auto_refresh = data.get('auto_refresh', False)

        if not question:
            return jsonify({
                'error': 'Question cannot be empty'
            }), 400

        # Get answer from chatbot
        bot = get_chatbot()
        answer = bot.ask(question, auto_refresh=auto_refresh)

        return jsonify({
            'answer': answer,
            'timestamp': datetime.now().isoformat()
        })

    except Exception as e:
        return jsonify({
            'error': f'Internal server error: {str(e)}'
        }), 500


@app.route('/api/refresh', methods=['POST'])
def refresh():
    """
    Manually trigger knowledge base refresh

    Returns:
    {
        "status": "success",
        "message": "Knowledge base refreshed",
        "timestamp": "..."
    }
    """
    try:
        bot = get_chatbot()
        bot.refresh_knowledge_base()

        return jsonify({
            'status': 'success',
            'message': 'Knowledge base refreshed successfully',
            'timestamp': datetime.now().isoformat()
        })

    except Exception as e:
        return jsonify({
            'error': f'Refresh failed: {str(e)}'
        }), 500


@app.route('/api/status', methods=['GET'])
def status():
    """
    Get chatbot status information

    Returns:
    {
        "status": "ready",
        "last_loaded": "...",
        "updates_available": false
    }
    """
    try:
        bot = get_chatbot()

        return jsonify({
            'status': 'ready',
            'last_loaded': bot.last_loaded.isoformat() if bot.last_loaded else None,
            'updates_available': bot.check_for_updates(),
            'timestamp': datetime.now().isoformat()
        })

    except Exception as e:
        return jsonify({
            'error': f'Status check failed: {str(e)}'
        }), 500


if __name__ == '__main__':
    # For development
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
