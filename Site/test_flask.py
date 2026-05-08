try:
    from flask import Flask
    print("Flask is installed successfully")
    
    # Test creating a simple app
    app = Flask(__name__)
    
    @app.route('/')
    def hello():
        return "Flask is working!"
    
    print("Flask app created successfully")
    print("You can run the main app with: python app.py")
    print("Then visit: http://127.0.0.1:5000")
    
except ImportError:
    print("Flask is not installed. Install it with: pip install flask")
except Exception as e:
    print(f"An error occurred: {e}")