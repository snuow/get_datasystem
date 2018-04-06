import Utils.API_Control as apcon
import Utils.procdata as proc
import pandas as pd
import datetime as dt

FILEPATH = r'../output'

if __name__ == '__main__':
    try:

        data = apcon.get_forecast()
        df = proc.combine_data(data, ['date', '温度'])
        df.to_csv(FILEPATH + '/' + dt.datetime.strftime(dt.datetime.now(), '%Y%m%d%H') + '.csv', encoding='SHIFT-JIS')
        print('Complete!')

    except:

        print('FAILED')

