import subprocess

def handler(request):
    # Start Streamlit server
    subprocess.Popen(["streamlit", "run", "app.py", "--server.port", "8000"])
    return {
        "statusCode": 200,
        "body": "Streamlit app started!"
    }
