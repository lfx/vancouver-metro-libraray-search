# Metro Vancouver Library Search

A simple web application to search for books in various libraries across Metro Vancouver. This application allows users to enter a book title and search for its availability in the following libraries:

*   Vancouver Public Library
*   Burnaby Public Library
*   Coquitlam Public Library
*   Port Moody Public Library
*   Port Coquitlam (Terry Fox) Public Library

## Features

*   Search for books by title across multiple libraries.
*   View book details including title, author, resource type, and availability.
*   See a thumbnail image of the book cover.
*   Click on a book title to open the book's page on the library's website in a new tab.
*   Click on the library name to perform a new search on the library's website with the same query.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/libsearch.git
    cd libsearch
    ```
2.  **Create a virtual environment and install dependencies:**
    ```bash
    uv venv
    uv pip install .
    ```
3.  **Run the application:**
    ```bash
    just run
    ```
    Or to run in debug mode:
    ```bash
    just debug
    ```

## Usage

1.  Open your web browser and navigate to `http://127.0.0.1:5000`.
2.  Enter a book title in the search box.
3.  Select the libraries you want to search.
4.  Click the "Search" button.

## Technologies Used

*   **Backend:** Python, Flask
*   **Frontend:** HTML, Pico.css
*   **Web Scraping:** Requests, BeautifulSoup
*   **Package Management:** uv
*   **Task Runner:** just
*   **Testing:** pytest, pytest-cov
*   **Linting:** ruff

---

## Go Implementation

This project also includes a Go implementation of the library search application. It provides the same features as the Python version.

### Running the Go Version

1.  **Navigate to the `go-libsearch` directory:**
    ```bash
    cd go-libsearch
    ```
2.  **Run the application:**
    ```bash
    go run .
    ```
    The application will be available at `http://127.0.0.1:5001`.

### Go Libraries Used

*   **Web Framework:** `net/http`
*   **Web Scraping:** `github.com/gocolly/colly/v2`
*   **HTML Templates:** `html/template`
