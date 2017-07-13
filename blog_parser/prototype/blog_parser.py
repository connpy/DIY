# 20170714 1日に複数記事があった場合にも対応

import urllib.request
from bs4 import BeautifulSoup
import xlsxwriter

#def show_input():
print('01:石森 虹花')
print('02:今泉 佑唯')
print('03:上村 莉菜')
print('04:尾関 梨香')
print('05:織田 奈那')
print('06:小池 美波')
print('07:小林 由依')
print('08:齋藤 冬優花')
print('09:佐藤 詩織')
print('10:志田 愛佳')
print('11:菅井 友香')
print('12:鈴本 美愉')
print('13:長沢 菜々香')
print('14:土生 瑞穂')
print('15:原田 葵')
print('16:欠番')
print('17:平手 友梨奈')
print('18:守屋 茜')
print('19:米谷 奈々未')
print('20:渡辺 梨加')
print('21:渡邉 理佐')
print('22:長濱 ねる')
print('23:井口 眞緒')
print('24:潮 紗理菜')
print('25:柿崎 芽実')
print('26:影山 優佳')
print('27:加藤 史帆')
print('28:齊藤 京子')
print('29:佐々木 久美')
print('30:佐々木 美玲')
print('31:高瀬 愛奈')
print('32:高本 彩花')
print('33:東村 芽依')

print('対応する番号を入力してください 例:26')
member_id = input('>>> ')

print('取得するデータの開始年月を入力してください 例:20170601 ※01は固定です')
request_date = input('>>> ')
#URL生成のためのメンバー番号と日付を返す
#return member_id, request_date




# ワークブックとワークシートを作成
wb = xlsxwriter.Workbook("blog_data{0}.xlsx".format(member_id))
# フォントをMeiryo UIにセット
meiryo_format = wb.add_format()
meiryo_format.set_font_name('Meiryo UI')
#ハイパーリンク用フォーマット
link_format = wb.add_format({'color': 'blue', 'underline': 1})
ws = wb.add_worksheet("blog_data")



j = 1
#ループで1ヶ月分取得
for i in range(1,31+1):
    print('{0}{1:02d}のブログ情報を取得しています...'.format(request_date[0:6], i))
    try:
        # アクセスするURL
        url = "http://www.keyakizaka46.com/s/k46o/diary/member/list?ima=0000&ct={0}&dy={1}{2:02d}".format(member_id, request_date[0:6], i)
        # URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
        html = urllib.request.urlopen(url)
        # htmlをBeautifulSoupで扱う
        soup = BeautifulSoup(html, "html.parser")
        # タイトル要素を全て取得する
        dayly_titles = soup.find_all(class_='box-ttl')
        title = []
        # タイトル要素を分解　おそらく2-3つ
        for blog_title in dayly_titles:
            # 分解したタイトル要素からリストを作成
            title.append(blog_title.find('a').getText())

        # 本文が記載されているclassを指定し複数のbox-article要素を抽出
        dayly_blogs = soup.find_all(class_='box-article')
        # 1日にブログが複数あった場合のためカウント
        blog_count = 0
        #複数のbox-article要素を一つずつに分解して処理
        for main_messages in dayly_blogs:
            #本文を1行ずつ出力（一つのタグに囲まれた要素毎に出力）
            for string in main_messages.strings:
                #セルAに日付を出力(MeiryoUIフォーマット)
                ws.write('A{0}'.format(j), '{0}/{1}/{2:02d}'.format(request_date[0:4], request_date[4:6], i), meiryo_format)
                #セルBにブログタイトルを出力(hyperlinkフォーマット)
                ws.write_url('B{0}'.format(j), url, link_format, title[blog_count])
                #セルCに本文を出力(MeiryoUIフォーマット)
                ws.write('C{0}'.format(j), string, meiryo_format)
                j += 1
            blog_count += 1
    #ブログが書かれてない日では必ずエラーが出るので無視する
    except AttributeError:
        print('{0}{1:02d}はブログが書かれていません'.format(request_date[0:6], i))

# ワークブックをクローズ
wb.close()

#print('データの取得が完了しました！\n')

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
