from dataclasses import dataclass
from typing import Dict, List, Optional

import requests
from bs4 import BeautifulSoup, Tag

response = requests.get("https://news.ycombinator.com/news")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
article_tags: List[Tag] = soup.find_all("tr")


@dataclass
class Article:
    id: int
    title: Optional[str] = None
    link: Optional[str] = None
    upvote: int = 0


def extract_article_info(article_tag: Tag) -> Optional[Article]:
    if "athing" in article_tag.attrs.get("class", []):
        article_title_tag = article_tag.select_one(".titleline").next_element

        article_id = int(article_tag.attrs.get("id"))
        article_title = article_title_tag.text
        article_link = article_title_tag.get("href")

        return Article(id=article_id, title=article_title, link=article_link)
    return None


def extract_upvote_info(article_tag: Tag, articles_dict: Dict[int, Article]):
    if not article_tag.attrs and article_tag.select_one(".score"):
        article_id = int(article_tag.select_one(".score").attrs.get("id").split("_")[1])
        article_upvote = int(article_tag.select_one(".score").text.split()[0])

        article = articles_dict.get(article_id, None)
        if article:
            article.upvote = article_upvote
        else:
            articles_dict[article_id] = Article(id=article_id, upvote=article_upvote)


articles_dict: Dict[int, Article] = {}

for article_tag in article_tags:
    article = extract_article_info(article_tag)
    if article:
        articles_dict[article.id] = article
    else:
        extract_upvote_info(article_tag, articles_dict)

for a in articles_dict.values():
    print(a.upvote)
