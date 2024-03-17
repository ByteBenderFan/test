import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts

f_us = open("E:/美国.txt", "r", encoding="UTF-8")
f_usnew = f_us.read()
f_usnew = f_usnew.replace("jsonp_1629344292311_69436(", "")
f_usnew = f_usnew[:-2]
us = json.loads(f_usnew)
us_trend_data = us['data'][0]['trend']

us_x_data = us_trend_data['updateDate'][:314]

us_y_data = us_trend_data['list'][0]['data'][:314]

f_YD = open("E:/印度.txt", "r", encoding="UTF-8")
f_YDnew = f_YD.read()
f_YDnew = f_YDnew.replace("jsonp_1629350745930_63180(", "")
f_YDnew = f_YDnew[:-2]
YD = json.loads(f_YDnew)
YD_trend_data = YD['data'][0]['trend']

YD_x_data = YD_trend_data['updateDate'][:314]

YD_y_data = YD_trend_data['list'][0]['data'][:314]

f_jp = open("E:/日本.txt", "r", encoding="UTF-8")
f_jpnew = f_jp.read()
f_jpnew = f_jpnew.replace("jsonp_1629350871167_29498(", "")
f_jpnew = f_jpnew[:-2]
jp = json.loads(f_jpnew)
jp_trend_data = jp['data'][0]['trend']

jp_x_data = jp_trend_data['updateDate'][:314]

jp_y_data = jp_trend_data['list'][0]['data'][:314]

line = Line()
line.add_xaxis(us_x_data)
line.add_yaxis("美国确诊人数", us_y_data)
line.add_yaxis("印度确诊人数", YD_y_data)
line.add_yaxis("日本确诊人数", jp_y_data)
line.set_global_opts(
    title_opts=TitleOpts(title="2020美日印三国确诊人数折现对比", pos_left="center", pos_bottom="1%")
)
line.render()
f_us.close()

f_YD.close()
f_jp.close()