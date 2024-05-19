#!/usr/bin/env python
from website import create_app

# Create app
app = create_app()

# Run webserver
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)