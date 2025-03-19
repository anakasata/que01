import datetime
from dateutil.relativedelta import relativedelta
import pywikibot

site = pywikibot.Site('ja', 'wikipedia')

def hantei01(page): # 1タイトルから記事種別判定検索
    try:
        text = page.get()
        return 1
    except pywikibot.exceptions.NoPageError as ne:
        return 2
    except Exception as e:
        return e

today = datetime.date.today()
t1 = today + relativedelta(days=+2)
y1=t1.year
m1=t1.month
d1=t1.day

title="プロジェクト:カテゴリ関連/議論/{}年/{}月{}日".format(y1,m1,d1)
page = pywikibot.page.BasePage(site, title)
n1=hantei01(page)
if int(n1)==2:
    text="<noinclude>{{プロジェクト:カテゴリ関連/議論/見出し|年=%s|月=%s|日=%s }}\n\n__NEWSECTIONLINK__\n\n= [[プロジェクト:カテゴリ関連/議論/%s年/%s月%s日|カテゴリ]] =\n</noinclude><includeonly>= [[プロジェクト:カテゴリ関連/議論/%s年/%s月%s日|%s月%s日]] =</includeonly>\n<!-- 新規の議論は一番下に記入してください。 -->" %(y1,m1,d1,y1,m1,d1,y1,m1,d1,m1,d1)
    pywikibot.diff.PatchManager("",text).print_hunks()
    page.text=text
    page.save("''BOT: 議論ページの作成''")
elif int(n1)==1:
    print("プロジェクト:カテゴリ関連/議論/{}年/{}月{}日作成済み".format(y1,m1,d1))
else:
    print(n1)