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

    @app.route("/c/<text>")
    def cName(text):
        """
            return the text variable with a C.
        """
        formatted_text = text.replace('_', ' ')
        return f'C {formatted_text}'

    @app.route('/python/', defaults={'text': 'is_cool'})
    @app.route("/python/<text>")
    def PythonName(text='is cool'):
        """
            return the text variable with a C.
        """
        format_text = text.replace('_', ' ')
        return f'Python {format_text}'

    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
