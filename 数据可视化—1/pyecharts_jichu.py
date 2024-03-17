from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
line=Line()
line.add_xaxis(["中国","美国","英国"])#添加X轴元素
line.add_yaxis("GTP",[30,20,10])#添加y轴元素
line.set_global_opts(
    title_opts=TitleOpts("GTP展示",pos_left="center",pos_bottom="1%"),
    legend_opts= LegendOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True)
)
line.render()#生成网页
