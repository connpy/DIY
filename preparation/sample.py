#if ('a' in 'abc') == True:
#    print('seikou')

#if('show_message(y.kageyama, "")')
a = 'show_message( y_kageyama, "あいうえお")'
b = 'show_message("あいうえお")'
#print(a)
starta = a.find('(')
startb = b.find('(')
#print(start)
enda = a.find(',')
endb = b.find(',')

#print(a[start+1:end].strip())
#for i in range(2):
#    if endb == -1:
#        continue
#    print('a')
#print(b[startb+1:endb].strip())
#比較ミスったらutf-8にしておく
c = 'あいう'.encode('utf-8')
d = 'y_kageyama'.replace('_', '')
#show_message(カメラマン,"")対策
if d.isalnum == False:
    continue
#print(c.isalnum())
#print(d.isalnum())
#print(d)
