import os
dir = './posts/'
mds = os.listdir(dir)
mds.sort()
lis = []
url = 'https://github.com/whynotjeffjeff/whynotjeffjeff/blob/master/md/'
for i in mds:
    st = '- [' + i.split('.md')[0] + '](' + url + i + ')'
    lis.append(st)
lis.sort()

rd0 = """# Welcome to my homepage

![whynotjeffjeff's GitHub stats](https://github-readme-stats.vercel.app/api?username=whynotjeffjeff&count_private=true&theme=dark)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs?username=whynotjeffjeff&layout=compact&count_private=true&theme=dark)

## Website [temp use waiting for finishing post sys]
- [https://whynotjeffjeff.github.io](https://whynotjeffjeff.github.io)


## Markdown Tree 

"""

rd = open('./README.md', '+w')
rd.write(rd0)
for i in lis:
    rd.write(i + '\n')
rd.close()