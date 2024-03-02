import os
dir = './posts/'
mds = os.listdir(dir)
mds.sort()
lis = []
url = 'https://github.com/nthr3ads/nthr3ads/blob/master/md/'
for i in mds:
    st = '- [' + i.split('.md')[0] + '](' + url + i + ')'
    lis.append(st)
lis.sort()

rd0 = """# Welcome to my homepage

![nthr3ads's GitHub stats](https://github-readme-stats.vercel.app/api?username=nthr3ads&count_private=true&theme=dark)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs?username=nthr3ads&layout=compact&count_private=true&theme=dark)

## Website [temp use waiting for finishing post sys]
- [https://nthr3ads.github.io](https://nthr3ads.github.io)


## Markdown Tree 

"""

rd = open('./README.md', '+w')
rd.write(rd0)
for i in lis:
    rd.write(i + '\n')
rd.close()