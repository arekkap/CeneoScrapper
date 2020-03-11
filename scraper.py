#import bibliotek
from requests import get
from bs4 import BeautifulSoup

#adres strony z opiniami
url ="https://www.ceneo.pl/86198612#tab=reviews_scroll"

#pobranie kodu HTML strony projektu URL
page = get(url).text
page_tree = BeautifulSoup(page, "html.parser")
#print(page_tree.prettify())



#wybranie kodu strony fragmentów odpowiadających poszczególnym opiniom
opinions = page_tree.select("li.review-box")
print(type(opinions))


#ekstrakcja składowych dla pierwszej opinii z listy
opinion = opinions[0]
opinion_id = opinion["data-entry-id"].pop().string
author = opinion.select('div.reviewer-name-line').pop().string
recommendation = opinion.select('div.product-review-summary > mm').pop().string
stars = opinion.select('span.review-score-count').pop().string
confirmed = opinion.select('div.product-reviev-pz').pop().string
# date_out = opinion.select('span.review-time > time["datetime"]')
# date_buy = opinion.select('span.review-time > time["datetime"]')
useful = opinion.select('button.vote-yes').pop()["data-total-vote"]
print(useful)
useless = opinion.select('button.vote-no').pop()["data-total-vote"]
content = opinion.select('p.product-redev-body').pop().get_text()
# cons = opinion.select('div.cons-cell > ul')
# pros = opinion.select('div.pros-cell > ul')

# - czy potwierdzona zakupem: div.product-reviev-pz
# - data wystawienia: span.review-time > time["datetime"] - pierwsze wystąpienie
# - data zakupu: span.review-time > time["datetime"] - drugie wystąpienie
# - przydatna: button.votes-yes["data-total-vote"]
# - nieprzydatna: button.votes-no["data-total-vote"]
# - treść: p.product-redev-body
# - wady: div.cons-cell > ul
# - zalety: div.pros-cell > ul