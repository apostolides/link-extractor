from fetchers import Fetcher
from filters import filter_dups
from filters import filter_domain
import extractor as ex

def single_url(url,domains_only=False,extract_all=False,agent=None):
    fetcher = Fetcher(agent=agent)
    html = None
    try:
        html = fetcher.get(url)
    except:
        return [[],[],[]]

    links, assets, scripts = ex.extract(html,extract_all=True)

    links = filter_dups(links)
    assets = filter_dups(assets)
    scripts = filter_dups(scripts)

    domains = []
    if domains_only:
        for coll in [links, assets, scripts]:
            doms = []
            for domain in coll:
                if len(filter_domain(domain).strip(' \n\t')) > 1:
                    doms.append(filter_domain(domain)) 
            domains.append(filter_dups(doms))
        return domains
    else:
        return [links, assets, scripts]

def urls_from_file(file,domains_only=False,extract_all=False,agent=None):
    results = []
    with open(file,'r') as f:
        for url in f.readlines():
            results.append(single_url(url.strip('\n'),domains_only=domains_only,extract_all=extract_all,agent=agent))
    return results

