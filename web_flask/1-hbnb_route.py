#!/usr/bin/python3
"""
    main program.
"""
if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def helloBnb():
        """
            returns "Hello HBNB!"
        """
        return "Hello HBNB!"

    @app.route("/hbnb")
    def hbnb():
        """
            return "HBNB"
        """
        return "HBNB"

    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
