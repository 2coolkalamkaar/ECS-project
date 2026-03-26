from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    return f"""
    <html>
        <head><title>AWS Fargate Demo</title></head>
        <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
            <h1>Hello from AWS Fargate! </h1>
            <p>Your CI/CD pipeline and ECS deployment worked perfectly.</p>
            <p><b>Served by Container ID:</b> {hostname}</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    # Binding to 0.0.0.0 allows external traffic to reach the Flask app
    app.run(host="0.0.0.0", port=80)
