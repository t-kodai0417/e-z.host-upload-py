import mimetypes,requests,json

def upload(fileName,key1):
    #mimetypeを変数に入れる
    mimet=mimetypes.guess_type(fileName)[0]
    #画像を読み込み
    fileDataBinary = open(fileName, 'rb').read()
    #e-z.hostへfileを送る引数はfileだった。fileの名前、fileのデータ、mimetypeを入れる。
    files = {'file': (fileName, fileDataBinary, mimet)}
    #一応、iOSから送信したことにしている。keyはUploadKeyで、dashboardで確認できる。
    headers = {'key': key1,
               'User-Agent':'Share with iOS'
              }
    #fileの送る先
    url = 'https://api.e-z.host/files'
    
    response = requests.post(url,headers=headers,files=files)
    #一応、ステータスコードを出力
    print(response.status_code)
    #jsonからurlを取得。
    aa=json.loads(response.content)
    #ここからは自分用に組んでいる。urlを出力したあとにtxtファイルにurlを書き込む。
    print(aa['imageUrl'])
    f=open('text.txt',"w")
    f.write(aa['imageUrl'])
    f.close()
