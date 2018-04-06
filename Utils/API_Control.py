import json
import urllib.request
import datetime
import time
import configparser

LONGITUDE = '34.7289'
LATITUDE = '135.413'
UNITS = 'si'
EXCLUDE = 'currently,minutely,daily,alerts,flags'

# start,end書式：yyyymmdd
startdate = '20180328'
enddate = '20180405'

inifile = configparser.ConfigParser()
inifile.read('../etc/init.txt')
APIKEY = inifile['darksky']['APIKEY']

print (APIKEY)

def get_forecast():
    try:
        url = 'https://api.darksky.net/forecast/' + APIKEY + '/' + LONGITUDE + ',' + LATITUDE + '?' + 'units=' + UNITS + '&exclude=' + EXCLUDE
        res = urllib.request.urlopen(url)
        # json_loads() でPythonオブジェクトに変換
        data = json.loads(res.read().decode('utf-8'))
        print(r'dataの取得を完了しました。')
    except urllib.error.HTTPError as e:
        print('HTTPError: ', e)
    except json.JSONDecodeError as e:
        print('JSONDecodeError: ', e)

    return data


def get_historicaldata():
    try:
        start = convert_JST_to_Unix(startdate)
        end = convert_JST_to_Unix(enddate)
        url = 'http://history.openweathermap.org/data/2.5/history/city?id=' + LOCATEID + '&type=hour' + '&start=' + start + '&end=' + end + '&appid=' + APIKEY
        res = urllib.request.urlopen(url)
        # json_loads() でPythonオブジェクトに変換
        data = json.loads(res.read().decode('utf-8'))
        print(r'dataの取得を完了しました。')
    except urllib.error.HTTPError as e:
        print('HTTPError: ', e)
    except json.JSONDecodeError as e:
        print('JSONDecodeError: ', e)

    return data


def get_currentweatherdata():
    try:
        start = convert_JST_to_Unix(startdate)
        end = convert_JST_to_Unix(enddate)
        url = 'http://api.openweathermap.org/data/2.5/weather?id=' + LOCATEID + '&units=' + UNITS + '&appid=' + APIKEY
        res = urllib.request.urlopen(url)
        # json_loads() でPythonオブジェクトに変換
        data = json.loads(res.read().decode('utf-8'))
        print(r'current_dataの取得を完了しました。')
    except urllib.error.HTTPError as e:
        print('HTTPError: ', e)
    except json.JSONDecodeError as e:
        print('JSONDecodeError: ', e)

    return data


def convert_JST_to_Unix(date):
    try:
        ans = time.mktime(datetime.datetime.strptime(date, '%Y%m%d').timetuple())
        # print('JSTからUnixTimeに変換しました。')
        return ans

    except:
        print('なんかエラー')


def convert_Unix_to_JST(date):
    try:
        ans = datetime.datetime.fromtimestamp(date)
        # print('UnixからJSTに変換しました。')
        return ans

    except:
        print('なんかエラー')

