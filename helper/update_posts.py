
# update_posts.def
# copyright (c) 2018, NiL, csningli@gmail.com

import sys, os

posts_dir = "../posts"
htmls = {}

# def update_posts() :


def create_html(md_filename) :
    html_filename = ".".join(md_filename.split('.')[:-1]) + ".html"
    md = ""

    timelabel = html_filename.split('-')[0]
    title = ""

    with open(posts_dir + "/" + md_filename, 'r') as f :
        for line in f :
            if title == "" and line.strip()[0] == '#' :
                title = line[1:].strip()
        md = f.read()

    with open(posts_dir + "/" + html_filename, 'w') as f :
        f.write(r'''<html>
        <head>
        <link rel="icon" href="../res/icon.png">
        <style>body{width:960px; margin:0 auto;}</style>
        <meta charset="utf-8" />
        <title>Posts</title>
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
        <div id="post"></div>

        <script>
        var md = new Remarkable();
        ''')

        f.write("document.getElementById(\"post\").innerHTML = md.render(%s)" % md)
        f.write(r'''</script>
        <div id="footer"></div>
        </body>
        </html>''')

    htmls[timelabel + " " + title] = html_filename

def check_posts() :
    if os.path.isdir(posts_dir) :
        for filename in os.listdir(posts_dir) :
            # print(filename)
            if len(filename.split('.')) > 1 and filename.split('.')[-1] == "md" :
                create_html(filename)


if __name__ == "__main__" :
    check_posts()
