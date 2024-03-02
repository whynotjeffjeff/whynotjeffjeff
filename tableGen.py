import os, time
def t(f):
    ti = os.path.getctime(f)
    til = time.localtime(ti)
    return time.strftime("%Y-%m-%d %H:%M:%S", til)

def t_c(f):
    ti = os.path.getatime(f)
    til = time.localtime(ti)
    return time.strftime("%Y-%m-%d %H:%M:%S", til)

dir = './posts/'
name = os.listdir(dir)
print(">>>File : " + str(len(name)) + " files")
mdline = []
url = 'https://github.com/nthr3ads/nthr3ads/blob/master/posts/'
for i in name:
    link = '[' + i.split('.md')[0] + '](' + url + i + ')'
    mdline.append("|" + t_c(dir + i) + "|" + t(dir + i) + "|" + link)

mdline.sort()
mdline.reverse()

title = """
|created date|lastest modified date|markdown links|
|-|-|-|
"""

rd0 = """# Welcome to my homepage

![nthr3ads's GitHub stats](https://github-readme-stats.vercel.app/api?username=nthr3ads&count_private=true&theme=dark)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs?username=nthr3ads&layout=compact&count_private=true&theme=dark)

## Website [temp use waiting for finishing post sys]
- [https://nthr3ads.github.io](https://nthr3ads.github.io)

## Markdown Table 

"""

rd = open('./README.md', '+w', encoding="utf-8")
rd.write(rd0)
rd.write(title)
for i in mdline:
    rd.write(i + '\n')
rd.close()
print(">>>Info : Success gen table")
