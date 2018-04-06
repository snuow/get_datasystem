import numpy as np
import pandas as pd
import Utils.API_Control as apcon


def combine_data(data, itemlist):
    df = pd.DataFrame(columns=itemlist)
    for icnt in np.arange(0, len(data['hourly']['data']), 1):
        add_weather_forecastser = pd.Series([str(apcon.convert_Unix_to_JST(data['hourly']['data'][icnt]['time'])),
                                             data['hourly']['data'][icnt]['temperature']],
                                            index=df.columns)
        df = df.append(add_weather_forecastser, ignore_index=True)

    df.index = df['date']
    df = df.drop('date', axis=1)

    return df


