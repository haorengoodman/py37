# 1.pyinstaller 打包命令
```
pyinstaller -F -w weather_info.py
```

# 2.exe 执行失败的调试方法
```
# 1. 打包
pyinstaller -D weather_info.py
# 2. 控制台执行
weather_info.exe
```

# 3.注意事项
> 打包之后，需要将city_code.json 与weather_info.exe 放在同一个路径下，weather_info.exe即可执行

# 4.中国城市编码文件
> https://dev.heweather.com/docs/refer/city