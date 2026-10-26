import urllib.request, urllib.error

req = urllib.request.Request(
        'https://www.pudim.com.br/', 
        headers={'User-Agent': 'Mozilla/5.0'}
    )

try:
    pudim = urllib.request.urlopen(req)
    print('\033[32mPudim foi acessado com sucesso!\033[0m')
except urllib.error.URLError as erro:
    print('\033[31mNão foi possível acessar pudim.\033[0m')
