import os

from flask_cloudflared import run_with_cloudflared

from app import app


run_with_cloudflared(app)
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5055")), debug=False)
