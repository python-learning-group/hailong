from urllib import request

urls = "https://query1.finance.yahoo.com/v7/finance/download/%5EDJI?period1=1499255531&period2=1501933931&interval=1d&events=history&crumb=QRpgsbJI8Rk"

def download_file(url):
    response = request.urlopen(url)
    csv = response.read()
    csv_str = str(csv)
    print(csv_str)
    lines = csv_str.split('\\n')
    dest_url = r'files.csv'
    fx = open(dest_url,'w')
    for line in lines:
        fx.write(line + '\n')

    fx.close()

download_file(urls)