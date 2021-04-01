
## 主要功能
--------------------
-  抖音用户视频下载

## 运行环境
--------------------
- windows
- python3

## 第三方库
--------------------
- 需要使用到的库已经放在requirements.txt，使用pip安装的可以使用指令
pip install -r requirements.txt
- 如果国内安装第三方库比较慢，可以使用以下指令进行清华源加速 pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

## 使用教程
--------------------

1. 手机打开抖音用户界面，找到用户链接。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210401152647949.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lleWVkZXdlbg==,size_16,color_FFFFFF,t_70)
2. 在浏览器打开刚刚复制的链接，然后在按F12打开检查元素，找到ajax中比较长的链接。复制下来。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210401152845878.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lleWVkZXdlbg==,size_16,color_FFFFFF,t_70)
3. 把程序中的sec_uid值改成复制的链接中sec_uid的值，程序链接url的&uid也全部替换。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210401153420372.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lleWVkZXdlbg==,size_16,color_FFFFFF,t_70)

5. 最后一步，修改文件夹名称，下载的视频放在该文件夹下
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210401154326414.png)
