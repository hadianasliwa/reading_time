from bs4 import BeautifulSoup
from bs4.element import Comment
import requests


def tag_visible(element):
    """
    removing unwanted tags
    Arguments:
        element: text, or web-text
    Returns:
        booleans: false if is in wanted tags, otherwise true
    """
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(url):
    """
    extracts all text from html
    Arguments:
        body: html text
    Returns:
        only text of the html
    """
    res = None
    try: 
        res = requests.get(url)
        body = res.text
        soup = BeautifulSoup(body, 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = filter(tag_visible, texts)  
        return u" ".join(t.strip() for t in visible_texts)
    except:  
        return None
