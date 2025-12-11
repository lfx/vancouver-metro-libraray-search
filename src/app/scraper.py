import requests
from bs4 import BeautifulSoup


def search_library(query, library_key, search_urls, base_urls):
    search_url_template = search_urls.get(library_key)
    base_url = base_urls.get(library_key)
    if not search_url_template or not base_url:
        return {"error": "Invalid library key."}

    search_url = search_url_template.format(query=query)

    try:
        response = requests.get(search_url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return {"error": f"Error fetching data from the library: {e}"}

    soup = BeautifulSoup(response.content, "html.parser")
    items = []

    for item in soup.find_all("div", class_="cp-search-result-item-content"):
        title_element = item.find("h3", class_="cp-title").find("a")
        title = title_element.text.strip() if title_element else "N/A"
        relative_link = title_element["href"] if title_element else "#"
        full_link = f"{base_url}{relative_link}" if relative_link != "#" else "#"

        author_element = item.find("span", class_="cp-by-author-block")
        author = (
            author_element.text.replace("by", "").strip() if author_element else "N/A"
        )

        resource_type_element = item.find("span", class_="cp-format-indicator-name")
        resource_type = (
            resource_type_element.text.strip() if resource_type_element else "N/A"
        )

        availability_element = item.find("span", class_="cp-availability-status")
        availability = (
            availability_element.text.strip() if availability_element else "N/A"
        )

        thumbnail_element = item.find("img", class_="cp-thumbnail")
        if thumbnail_element:
            thumbnail = thumbnail_element["src"]
        else:
            jacket_cover = item.find("div", class_="jacket-cover-wrap")
            if jacket_cover:
                img_tag = jacket_cover.find("img")
                if img_tag:
                    thumbnail = img_tag.get("src")
                else:
                    thumbnail = None
            else:
                thumbnail = None

        items.append(
            {
                "title": title,
                "author": author,
                "resource_type": resource_type,
                "availability": availability,
                "link": full_link,
                "thumbnail": thumbnail,
            }
        )

    return {"items": items}
