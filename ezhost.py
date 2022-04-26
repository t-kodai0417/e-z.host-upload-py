import mimetypes,requests,json

def upload(fileName,key1):
    mimet=mimetypes.guess_type(fileName)[0]
    fileDataBinary = open(fileName, 'rb').read()
    files = {'file': (fileName, fileDataBinary, mimet)}
    headers = {'key': key1,
               'User-Agent':'Share with iOS'
              }
    
    url = 'https://api.e-z.host/files'
    
    response = requests.post(url,headers=headers,files=files)
    
    print(response.status_code)
    
    aa=json.loads(response.content)
    print(aa['imageUrl'])
