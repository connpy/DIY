import urllib.request
from bs4 import BeautifulSoup
import xlsxwriter

print('データを取得しています...\n')


# ワークブックとワークシートを作成
wb = xlsxwriter.Workbook("blog_data.xlsx")
ws = wb.add_worksheet("blog_data")

j = 1
#ループで1月分取得
for i in range(1,31+1):
    try:
        # アクセスするURL
        url = "http://www.keyakizaka46.com/s/k46o/diary/member/list?ima=0000&ct=26&dy=201609{0:02d}".format(i)

        # URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
        html = urllib.request.urlopen(url)

        # htmlをBeautifulSoupで扱う
        soup = BeautifulSoup(html, "html.parser")

        # タイトル要素を取得する
        title = soup.find(class_='box-ttl').find('a')

        # 本文が記載されているclassを指定しその中のaタグ内を抽出
        main_message = soup.find(class_='box-article')

        #本文を1行ずつ出力（一つのタグに囲まれた要素毎に出力）
        for string in main_message.strings:
            #セルAに日付を出力
            ws.write('A{0}'.format(j), '2017-09-{0:02d}'.format(i))
            #セルBにブログタイトルを出力
            ws.write('B{0}'.format(j), title.getText())
            #セルCに本文を出力
            ws.write('C{0}'.format(j), string)
            j += 1
    #ブログが書かれてない日では必ずエラーが出るので無視する
    except AttributeError:
        pass

# ワークブックをクローズ
wb.close()

print('データの取得が完了しました！\n')

#for tag in main_message:
#    tag.extract()
#print(main_message.getText())
#print(main_message.string)

#本文を1行ずつ出力（一つのタグに囲まれた要素毎に出力）
#for string in main_message.strings:
#    print((string))







#正規表現でタグ除去
#untag_message = re.compile(r"<[^>]*?>")

#untag_message.sub("", main_message)

#print(untag_message)
