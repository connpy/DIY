import glob

# 配下のフォルダから.txtファイルをリストとして返す
def text_finder():
    # ./はカレントディレクトリ、**は配下のディレクトリを対象にする3系以降でサポート
    text_files = glob.glob('./**/*.txt')
    return text_files

#.txtファイルをopenして行毎のリストで返す
def read_text(text_file):
    with open('{0}'.format(text_file), 'r', encoding='utf-8') as f:
        s = f.readlines()
    return s

#追記した行毎のリストであるoutputを書き込み
def write_text(text_file, output):
    with open('{0}'.format(text_file), 'w', encoding='utf-8') as f:
        f.write(output)

def show_input():
    print('検索文字列の次の行にテキストを挿入するスクリプトです')
    print('検索対象の文字列を入力してください 例:show_message')
    query = input('>>> ')
    print('挿入するテキストを入力してください 例:scene_end_continue()')
    insert_text = input('>>> ')
    return query, insert_text

query, insert_text = show_input()
text_files = text_finder()

#テキストファイル群をファイル毎に処理
for text_file in text_files:
    #ファイルを行単位で処理するための準備
    lines = read_text(text_file)
    #書き込み用の配列とフラグを準備
    output = []
    keyword_count = 0
    #ファイルを行単位で処理
    for line in lines:
        #基本的に読み込んだ行を書き込み用配列に追加
        output.append(line)
        #検索対象文字列があった場合のみ1行追記
        if ('show_message' in line) == True:
            output.append("scene_end_continue()\n")
            keyword_count += 1
    #1ファイル分の読み込みが完了後、追記分があれば書き込み
    if keyword_count > 0:
        write_text(text_file, output)
    #debug
    print(lines)


#debug
#print(text_files[0])

#debug
#print(s)

#※検索対象が2行に渡って書かれていたら誤作動
#コメント対応が必要、先に//検索して見つけたらスルー的な処理
