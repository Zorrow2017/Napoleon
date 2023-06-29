nplz
========================


fir
------------------------
"Sunday June 25 2023 11:30:48 GMT+0800 (China Standard Time)"
<br/>
https://gitee.com/jimvon
<br/>
https://gitee.com/jimvon/nplz.git
<br/>
https://github.com/zorrow2017
<br/>
jimvoncn@163.com


commit
------------------------
GIT: first initial git vscode by jim 2023-06-25
GIT: some gitee operation 0625
GIT: gitee ok 0625
GIT: add py and html template 0629


```powershell
## 命令行的注释符号是## 或者是::
cd E:\java\nplz0625
git clone https://gitee.com/jimvon/nplz.git
cd nplz
git checkout develop

##(2).修改 修改 E:\java\nplz0625\nplz 文件夹下的文件

git add .
git commit -m "message text about this commit"
git push https://gitee.com/jimvon/nplz.git develop:develop

##(3).上传 git push --force 是用本地修改强制覆盖掉<远程文件夹>
##(1).下载 git clone 是把<远程文件夹>复制到本地电脑(要下载git软件)，也可在网页下载压缩包(要登录)
## 需要用户名密码认证登录<远程服务器>
## repository branch auth commit release
## develop1234是各试验分支，master是合并的正式分支
##(4).版本控制 把dev的各种修改，合并到master正式分支，合并失败则手动解决
git checkout master
git merge develop
git push https://gitee.com/jimvon/nplz.git master:master
```



current
------------------------
当前进度：
nplz.md.txt 半成品20%
tool\clickTimeInterval.py 已完成
tool\regex-half.html 半成品30%
other 未开始








