import logging

from flask import Flask, render_template, request

from .config import BASE_URLS, LIBRARIES, SEARCH_URLS
from .scraper import search_library

app = Flask(__name__, template_folder="../templates")

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)


@app.route("/")
def index():
    return render_template("index.html", libraries=LIBRARIES)


@app.route("/search")
def search():
    try:
        query = request.args.get("query")
        library_keys = request.args.getlist("libraries")
        results = {}

        for key in library_keys:
            results[key] = search_library(query, key, SEARCH_URLS, BASE_URLS)

        return render_template(
            "results.html",
            query=query,
            results=results,
            libraries=LIBRARIES,
            base_urls=BASE_URLS,
            search_urls=SEARCH_URLS,
        )
    except Exception as e:
        app.logger.error("An error occurred during search: %s", e, exc_info=True)
        raise
