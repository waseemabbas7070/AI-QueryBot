from flask import Flask
from document_processor import process_documents
from vector_store import create_vector_store
from chat_chain import create_chat_chain

def create_app():
    app = Flask(__name__, static_folder='../Frontend', static_url_path='')
    
    # Initialize the AI components
    texts = process_documents()
    retriever = create_vector_store(texts)
    app.chat_chain = create_chat_chain(retriever)
    
    # Register blueprints
    from .routes import api_bp
    app.register_blueprint(api_bp)
    
    return app