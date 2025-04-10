def log(message: str):
    from datetime import datetime
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")
