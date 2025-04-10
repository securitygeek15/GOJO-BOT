from flask import Flask, render_template_string, request, redirect
import json
import os

app = Flask(__name__)

# Load config for bot data
with open('config.json') as f:
    config = json.load(f)

@app.route('/')
def home():
    return render_template_string("""
    <h1>🤖 ModCore Dashboard</h1>
    <p>Prefix: <strong>{{ prefix }}</strong></p>
    <p>Owner ID: <strong>{{ owner }}</strong></p>
    <a href="/servers">View Servers</a>
    """, prefix=config['PREFIX'], owner=config['OWNER_ID'])

@app.route('/servers')
def servers():
    # In production, you'd use OAuth2 to fetch user's servers + bot's servers
    dummy_servers = ["Test Server A", "Dev Guild B", "ModCore Playground"]
    return render_template_string("""
    <h2>🧠 Bot is in these servers:</h2>
    <ul>
      {% for server in servers %}
        <li>{{ server }}</li>
      {% endfor %}
    </ul>
    <a href="/">← Back</a>
    """, servers=dummy_servers)

@app.route('/send', methods=["GET", "POST"])
def send_message():
    if request.method == "POST":
        content = request.form['msg']
        # You'd send this message using bot API
        print(f"[DASHBOARD] Simulated message: {content}")
        return redirect('/send')

    return render_template_string("""
    <h2>Send Message</h2>
    <form method="POST">
      <textarea name="msg" rows="4" cols="50"></textarea><br>
      <input type="submit" value="Send">
    </form>
    <a href="/">← Back</a>
    """)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
