# scrape hackernews.com
# by number of votes

# using the library - 'beautiful soup"

import requests  # allows us initially to download the html
from bs4 import BeautifulSoup  # allows to use html and grab the data - in obj parser
import pprint  # print pretty

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.titleline>a')  # using css selectors
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline>a')  # using css selectors
subtext2 = soup2.select('.subtext')
# print(votes[0].get('id'))

mega_links = links+links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    # sort the dictionary using lambda function
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        # None a s a default if no link found
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > int(99):
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


# pprint.pprint(create_custom_hn(links, subtext))

pprint.pprint(create_custom_hn(mega_links, mega_subtext))
# print(create_custom_hn(links, subtext))
