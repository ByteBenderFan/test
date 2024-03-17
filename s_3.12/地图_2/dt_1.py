import json
from pyecharts.charts import Map
from pyecharts.options import *

f=open("E:\疫情.txt","r",encoding="UTF-8")
alldate=f.read()
f.close()
date_dict=json.loads(alldate)
province=date_dict["areaTree"][0]["children"]
date_list=[]
for province_date in province:
    province_name=province_date["name"]
    province_confirm=province_date["total"]["confirm"]
    date_list.append((province_name,province_confirm))
map=Map()
map.add("各省份确诊人数",date_list,"china")
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000-4999", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-9999", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999", "color": "#CC3333"},
            {"min": 100000, "lable": "100000+","color": "#990033"}
        ]
    )
)
map.render()
#黑马程序员的资料有问题