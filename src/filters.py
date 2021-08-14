from urllib.parse import urlparse

def filter_dups(li):
    if li:
        return list(dict.fromkeys(li))
    return []

def filter_domain(link):
    return urlparse(link).netloc