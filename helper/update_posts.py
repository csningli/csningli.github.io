
# update_posts.def
# copyright (c) 2018, NiL, csningli@gmail.com

import sys, os

posts_dir = "../posts"
htmls = {}

def update_posts() :
    # print(htmls)
    years = {}
    for name in sorted(htmls.keys(), reverse = True) :
        if name[:4] not in years.keys() :
            years[name[:4]] = []
        years[name[:4]].append((name, htmls[name]))

    with open("../posts.html", 'w') as f :
        f.write(r'''<html>
        <head>
        <link rel="icon" href="../res/icon.png">
        <style>body{width:960px; margin:0 auto;}</style>
        <meta charset="utf-8" />
        <title>Posts</title>
        <script src="//code.jquery.com/jquery-1.10.2.js"></script>
        <script>
        $(function(){
          $("#header").load("header.html");
          $("#footer").load("footer.html");
        });
        </script>
        </head>

        <body>
        <div id="header"></div>
        <br>
        <h1>Posts</h1>
        <br>
        ''')

        for name in sorted(years.keys(), reverse = True) :
            f.write("<h2>%s</h2>\n" % name)
            f.write("<ul>\n")
            for item in years[name] :
                f.write("<li><a href=\"posts/%s\">%s</a></li>\n" % (item[1], item[0]))
            f.write("</ul>\n")


        f.write(r'''<div id="footer"></div>
        </body>
        </html>''')


def create_html(md_filename) :
    html_filename = ".".join(md_filename.split('.')[:-1]) + ".html"
    md = []

    timelabel = html_filename.split('-')[0]
    title = ""

    with open(posts_dir + "/" + md_filename, 'r') as f :
        for line in f :
            md.append(line)
            if title == "" and line.strip()[0] == '#' :
                title = line[1:].strip()
    print(timelabel, "-", title, "-", md)

    with open(posts_dir + "/" + html_filename, 'w') as f :
        f.write(r'''<html>
        <head>
        <link rel="icon" href="../res/icon.png">
        <style>body{width:960px; margin:0 auto;}</style>
        <meta charset="utf-8" />
        ''')
        f.write("<title>%s</title>\n" % title)
        f.write(r'''
        <script src="//code.jquery.com/jquery-1.10.2.js"></script>
        <script src="//cdn.jsdelivr.net/remarkable/1.7.1/remarkable.min.js"></script>
        <script>
        $(function(){
          $("#header").load("../header.html");
          $("#footer").load("../footer.html");
        });
        </script>
        </head>

        <body>
        <div id="header"></div>
        <p id="time"></p>
        <p id="post"></p>

        <script>
        var md = new Remarkable();
        ''')


        f.write("document.getElementById(\"time\").innerHTML = \"[Posted on: %s]\"\n" % timelabel)
        for line in md :
            f.write("document.getElementById(\"post\").innerHTML += md.render(\'%s\');\n" % line.strip('\n'))

        f.write(r'''</script>
        <div id="footer"></div>
        </body>
        </html>''')

    htmls[timelabel + " - " + title] = html_filename

def check_posts() :
    if os.path.isdir(posts_dir) :
        for filename in os.listdir(posts_dir) :
            # print(filename)
            if len(filename.split('.')) > 1 and filename.split('.')[-1] == "md" :
                create_html(filename)


if __name__ == "__main__" :
    check_posts()
    update_posts()
