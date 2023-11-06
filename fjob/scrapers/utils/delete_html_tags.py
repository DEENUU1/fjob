from typing import Optional


def delete_html_tags(description: str) -> Optional[str]:
    """
    Delete HTML tags from description
    """
    if not description:
        return None

    return (
        description.replace("<p>", " ")
        .replace("</p>", " ")
        .replace("<strong>", " ")
        .replace("</strong>", " ")
        .replace("<li>", " ")
        .replace("</li>", " ")
        .replace("<ul>", " ")
        .replace("</ul>", " ")
        .replace("<br />", " ")
    )
