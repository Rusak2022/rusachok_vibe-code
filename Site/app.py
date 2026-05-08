from flask import Flask, render_template
# Create the Flask application instance
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def index():
    """
    Render the main page template
    """
    return render_template('index.html')

# Run the application when the script is executed
if __name__ == '__main__':
    print("Starting Vibe-Coding Magic Website...")
    print("Access the site at: http://127.0.0.1:8080")
    
    try:
        app.run(
            host='127.0.0.1',
            port=8080,
            debug=True,  # Enabled debug mode for automatic reloading
            threaded=True
        )
    except Exception as e:
        print(f"Error starting the server: {e}")
        input("Press Enter to exit...")