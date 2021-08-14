import requests as r

class Fetcher:

  def __init__(self,agent=None,allow_redirects=True):
    self.agent = agent
    self.allow_redirects = allow_redirects

  def get(self,url):
    headers = {}
    
    if self.agent:
      headers['User-Agent'] = self.agent

    response = r.get(url,headers=headers,allow_redirects=self.allow_redirects)
    
    # for redir in response.history:
    #   print(redir.url)

    return response.content