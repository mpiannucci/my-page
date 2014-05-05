from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def login_fail (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<h1>Admin Login</h1>\n'])
    extend_([u'<form action="" method="post">\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'</form>\n'])
    extend_([u'<hr>\n'])
    extend_([u'<div id="failedlogin"><h2><font color="red">Invalid Username or Password</font></div>\n'])

    return self

login_fail = CompiledTemplate(login_fail, 'templates/login_fail.html')
join_ = login_fail._join; escape_ = login_fail._escape

# coding: utf-8
def blog (pageNum):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    postCount = 0
    next = pageNum + 1
    prev = pageNum - 1
    posts = get_posts((pageNum-1)*6)
    extend_([u'\n'])
    extend_([u'<div id="blogContainer">\n'])
    extend_([u'  <div id="blogTitle">\n'])
    extend_([u'    <h1>Blog</h1>\n'])
    extend_([u'  </div>\n'])
    extend_([u'  <hr>\n'])
    extend_([u'  <div id="postStream" class="postDisp">\n'])
    extend_([u'    <!-- Loop thourgh all posts in the database and display them as declared below -->\n'])
    for post in loop.setup(posts):
        postCount+=1
        extend_(['    ', u'<h2 class="links"><a href="/view/', escape_(post.url, True), u'">', escape_(post.title, True), u'</a></h2>\n'])
        extend_(['    ', u'<h3>', escape_(datestr(post.date), True), u'</h3>\n'])
        extend_(['    ', u'<div id="postContent">\n'])
        extend_(['    ', u'  ', escape_(post.content, False), u'\n'])
        extend_(['    ', u'</div>\n'])
        extend_(['    ', u'<br/>\n'])
        extend_(['    ', u'<div id="links" class="links">\n'])
        extend_(['    ', u'  <table class="linkTable">\n'])
        extend_(['    ', u'    <tr>\n'])
        extend_(['    ', u'      <td><a href="/view/', escape_(post.url, True), u'">Comment</a></td>\n'])
        extend_(['    ', u'      <td>Tagged &nbsp; <a href="/tag/', escape_(post.tag, True), u'">', escape_(post.tag, True), u'</a></td>\n'])
        extend_(['    ', u'    </tr>\n'])
        extend_(['    ', u'  </table>\n'])
        extend_(['    ', u'</div>\n'])
        extend_(['    ', u'<hr>\n'])
    extend_([u'  </div>\n'])
    extend_([u'  <div id="blogLinks" class="links">\n'])
    if pageNum == 1:
        if postCount < 6:
            extend_(['    ', u'<table class="navTable">\n'])
            extend_(['    ', u'  <tr>\n'])
            extend_(['    ', u'    <td>Page ', escape_(pageNum, True), u'</td>\n'])
            extend_(['    ', u'    <td><a href="/archive">Archive</a></td>\n'])
            extend_(['    ', u'  </tr>\n'])
            extend_(['    ', u'</table>\n'])
        else:
            extend_(['    ', u'<table class="navTable">\n'])
            extend_(['    ', u'  <tr>\n'])
            extend_(['    ', u'    <td>Page ', escape_(pageNum, True), u'</td>\n'])
            extend_(['    ', u'    <td><a href="/blog/', escape_(next, True), u'">Next</a></td>\n'])
            extend_(['    ', u'    <td><a href="/archive">Archive</a></td>\n'])
            extend_(['    ', u'  </tr>\n'])
            extend_(['    ', u'</table>\n'])
    else:
        if postCount < 6:
            extend_(['    ', u'<table class="navTable">\n'])
            extend_(['    ', u'  <tr>\n'])
            extend_(['    ', u'    <td><a href="/blog/', escape_(prev, True), u'">Previous</a></td>\n'])
            extend_(['    ', u'    <td>Page ', escape_(pageNum, True), u'</td>\n'])
            extend_(['    ', u'    <td><a href="/archive">Archive</a></td>\n'])
            extend_(['    ', u'  </tr>\n'])
            extend_(['    ', u'</table>\n'])
        else:
            extend_(['    ', u'<table class="navTable">\n'])
            extend_(['    ', u'  <tr>\n'])
            extend_(['    ', u'    <td><a href="/blog/', escape_(prev, True), u'">Previous</a></td>\n'])
            extend_(['    ', u'    <td>Page ', escape_(pageNum, True), u'</td>\n'])
            extend_(['    ', u'    <td><a href="/blog/', escape_(next, True), u'">Next</a></td>\n'])
            extend_(['    ', u'    <td><a href="/archive">Archive</a></td>\n'])
            extend_(['    ', u'  </tr>\n'])
            extend_(['    ', u'</table>\n'])
    extend_([u'  </div>\n'])
    extend_([u'</div>\n'])

    return self

blog = CompiledTemplate(blog, 'templates/blog.html')
join_ = blog._join; escape_ = blog._escape

# coding: utf-8
def edit (post, form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<h1>Edit ', escape_(form.d.title, True), u'</h1>\n'])
    extend_([u'\n'])
    extend_([u'<form action="" method="post">\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'</form>\n'])
    extend_([u'\n'])
    extend_([u'\n'])
    extend_([u'<h2>Delete post</h2>\n'])
    extend_([u'<form action="/delete/', escape_(post.url, True), u'" method="post">\n'])
    extend_([u'    <input type="submit" value="Delete post"/>\n'])
    extend_([u'</form>\n'])

    return self

edit = CompiledTemplate(edit, 'templates/edit.html')
join_ = edit._join; escape_ = edit._escape

# coding: utf-8
def view (post):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<div id="viewContainer" class="postDisp">\n'])
    extend_([u'        <h1>', escape_(post.title, True), u'</h1>\n'])
    extend_([u'        <h3>', escape_(datestr(post.date), True), u'</h3>\n'])
    extend_([u'        <div id="viewContent">\n'])
    extend_([u'                ', escape_(post.content, False), u'\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <br/>\n'])
    extend_([u'        <div id="links" class="links">\n'])
    extend_([u'                <table class="linkTable">\n'])
    extend_([u'                        <tr>\n'])
    extend_([u'                                <td><a href="/view/', escape_(post.url, True), u'">Link</a></td>\n'])
    extend_([u'                                <td>Tagged &nbsp; <a href="/tag/', escape_(post.tag, True), u'">', escape_(post.tag, True), u'</a></td>\n'])
    extend_([u'                        </tr>\n'])
    extend_([u'                </table>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <br/>\n'])
    extend_([u'        <div id="commentSection">\n'])
    extend_([u'        <div id="disqus_thread"></div>\n'])
    extend_([u'        <script type="text/javascript">\n'])
    extend_([u'                /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */\n'])
    extend_([u"                var disqus_shortname = 'matthewiannucci'; // required: replace example with your forum shortname\n"])
    extend_([u'\n'])
    extend_([u"                /* * * DON'T EDIT BELOW THIS LINE * * */\n"])
    extend_([u'                (function() {\n'])
    extend_([u"                var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;\n"])
    extend_([u"                dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';\n"])
    extend_([u"                (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);\n"])
    extend_([u'                })();\n'])
    extend_([u'        </script>\n'])
    extend_([u'        <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>\n'])
    extend_([u'        <a href="http://disqus.com" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])

    return self

view = CompiledTemplate(view, 'templates/view.html')
join_ = view._join; escape_ = view._escape

# coding: utf-8
def bio():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="contactContainer">\n'])
    extend_([u'        <div id="contactTitle">\n'])
    extend_([u'                <h1>Bio</h1>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <hr/>\n'])
    extend_([u'        <div id="contactBody">\n'])
    extend_([u'                <div id="bioPhoto">\n'])
    extend_([u'                        <img id="bioPic" src="/static/Images/melaptop.png" alt="bioPic" />\n'])
    extend_([u'                </div>\n'])
    extend_([u'                <div id="bioText">\n'])
    extend_([u'                        <h2>About Me</h2>\n'])
    extend_([u'                        <p>Hello, my name is Matthew Iannucci. I am currently a Senior Ocean Engineering student at the University of Rhode Island. I have a strong background in computer engineering and software development.  I plan to graduate in the Spring of 2014 and join the workforce as an educated, motivated engineer.</p>\n'])
    extend_([u'                </div>\n'])
    extend_([u'                <div id="contactLinks" class="links">\n'])
    extend_([u'                        <h3><a href="/resume">Resume</a></h3>\n'])
    extend_([u'                        <h3><a href="/github">Github</a></h3>\n'])
    extend_([u'                        <h3><a href="mailto:rhodysurf13@gmail.com">Email</a></h3>\n'])
    extend_([u'                        <h3><a href="http://www.linkedin.com/pub/matthew-iannucci/7a/884/64a/">LinkedIn</a></h3>\n'])
    extend_([u'                </div>\n'])
    extend_([u'        </div>\n'])
    extend_([u'</div>\n'])

    return self

bio = CompiledTemplate(bio, 'templates/bio.html')
join_ = bio._join; escape_ = bio._escape

# coding: utf-8
def new (form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<h1>New Blog Post</h1>\n'])
    extend_([u'<form action="" method="post">\n'])
    extend_([escape_(form.render(), False), u'\n'])
    extend_([u'</form>\n'])

    return self

new = CompiledTemplate(new, 'templates/new.html')
join_ = new._join; escape_ = new._escape

# coding: utf-8
def admin (user, posts):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<div id="adminContainer">\n'])
    extend_([u'        <h3>Edit the blog entries</h3>\n'])
    extend_([u'        <ul>\n'])
    for post in loop.setup(posts):
        extend_(['                ', u'<li>\n'])
        extend_(['                ', u'        <a href="/view/', escape_(post.url, True), u'">', escape_(post.title, True), u'</a> \n'])
        extend_(['                ', u'        from ', escape_(datestr(post.date), True), u' \n'])
        extend_(['                ', u'        <a href="/edit/', escape_(post.url, True), u'">Edit</a>\n'])
        extend_(['                ', u'        <form action="/delete/', escape_(post.url, True), u'" method="post">\n'])
        extend_(['                ', u'        <input type="submit" value="Delete post"/>\n'])
        extend_(['                ', u'        </form>\n'])
        extend_(['                ', u'</li>\n'])
    extend_([u'        </ul>\n'])
    extend_([u'        <div id="bottomAdmin" class="links">\n'])
    extend_([u'        <a href="/new">New Post</a></li>\n'])
    extend_([u'        <br/><br/>\n'])
    extend_([u'        <p>Logged in as ', escape_(user, True), u'</p>\n'])
    extend_([u'        <a href="/logout">Log Out</a>\n'])
    extend_([u'        </div>\n'])
    extend_([u'</div>\n'])

    return self

admin = CompiledTemplate(admin, 'templates/admin.html')
join_ = admin._join; escape_ = admin._escape

# coding: utf-8
def apps():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="projectContainer">\n'])
    extend_([u'        <div id="projectTitle">\n'])
    extend_([u'                <h1>Apps</h1>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <hr>\n'])
    extend_([u'        <div id="project1">\n'])
    extend_([u'                <h2 id="simpleSolverTitle">SimpleSolver</h2>\n'])
    extend_([u'                <p>As an engineering student, it has frustrated me that were no quadratic equation solving applications with an elegant user interface. I strived to create a simple, but useful app with a user interface that matched these characteristics. Thus, SimpleSolver for Android was born. This application is now available on Google Play for free.</p>\n'])
    extend_([u'                <center>\n'])
    extend_([u'                        <!-- This is the app screenshots -->\n'])
    extend_([u'                        <img class="screenshots" id="SSscreen2" src="/static/Images/SSscreen2.png" alt="SSscreen2" />\n'])
    extend_([u'                        <img class="screenshots" id="SSscreen1" src="/static/Images/SSscreen1.png" alt="SSscreen1" />\n'])
    extend_([u'                        <br/>\n'])
    extend_([u'                        <!-- This is the Google Play button -->\n'])
    extend_([u'                        <a href="https://play.google.com/store/apps/details?id=com.nucc.simplesolver">\n'])
    extend_([u'                                <img id="googlePlayBadge" alt="Get it on Google Play" src="https://developer.android.com/images/brand/en_generic_rgb_wo_60.png" />\n'])
    extend_([u'                        </a>\n'])
    extend_([u'                </center>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <div id="project2">\n'])
    extend_([u'                <h2>HackWinds</h2>\n'])
    extend_([u'                <p>Viewing the surf camera for Narragansett, RI has always proved to be tedious on a phone. Especially because there is specific mobile layout or application. So, in the name of simplicity I decided to hack together a small Android app that simply shows the surf camera images with no frills. Recently, I have added a second feature, wheer the user can see the predicted conditions for the current day and the two next days.</p>\n'])
    extend_([u'                <center>\n'])
    extend_([u'                        <!-- This is the app screenshots -->\n'])
    extend_([u'                        <img class="screenshots" id="HWscreen1" src="/static/Images/HWscreen1.png" alt="HWscreen1" />\n'])
    extend_([u'                        <img class="screenshots" id="HWscreen2" src="/static/Images/HWscreen2.png" alt="HWscreen2" />\n'])
    extend_([u'                        <br/>\n'])
    extend_([u'                        <h3 class="links"><a href="/static/Misc/hackWinds.apk">Download Here</a> | <a href="https://github.com/mpiannucci/HackWinds">Source Here</a></h3>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <div id="project3">\n'])
    extend_([u'                <h2>Other</h2>\n'])
    extend_([u'                <p>To view many of my smaller projects and meddlings of mine, feel free to browse my projects on Github.</p>\n'])
    extend_([u'                <center>\n'])
    extend_([u'                        <h3 class="links"><a href="/github">View My Github Here</a></h3>\n'])
    extend_([u'                </center>\n'])
    extend_([u'        </div>\n'])
    extend_([u'</div>\n'])

    return self

apps = CompiledTemplate(apps, 'templates/apps.html')
join_ = apps._join; escape_ = apps._escape

# coding: utf-8
def index():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div id="homeContainer"> \n'])
    extend_([u'        <div id="topImageRow">\n'])
    extend_([u'        <img id="homeImage" src="/static/Images/bigturn.jpg">\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div id="welcomeFoot">\n'])
    extend_([u'        <h2>Welcome..</h2>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])

    return self

index = CompiledTemplate(index, 'templates/index.html')
join_ = index._join; escape_ = index._escape

# coding: utf-8
def base (page):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<html>\n'])
    extend_([u'<head>\n'])
    extend_([u'    <meta name="google-site-verification" content="-azLgyDbTQ6EY0zdkcRBc8Q5f0jSV4cd552gcq44N98" />\n'])
    extend_([u'    <title>Matthew Iannucci</title>\n'])
    extend_([u'    <link rel="stylesheet" type="text/css" href="/static/Styles/mobile.css" media="only screen and (max-device-width: 767px)" />\n'])
    extend_([u'    <link rel="stylesheet" type="text/css" href="/static/Styles/screen.css" media="only screen and (min-device-width: 768px)" />\n'])
    extend_([u'    <link rel="shortcut icon" type="image/x-icon" href="/static/favicon.ico" />\n'])
    extend_([u'</head>\n'])
    extend_([u'<body>\n'])
    extend_([u'        <!-- Define the header for the page -->\n'])
    extend_([u'        <div id="header">\n'])
    extend_([u'                <h1><a href="/">Matthew Iannucci</a></h1>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <!-- Create the three coloumn layout.-->\n'])
    extend_([u'        <div class="colmask threecol">\n'])
    extend_([u'                <div class="colmid">\n'])
    extend_([u'                        <div class="colleft">\n'])
    extend_([u'                                <div class="col1">\n'])
    extend_([u'                                        <!-- Column 1 start -->\n'])
    extend_([u'                                        <!-- Get the page data as declared in code.py -->\n'])
    extend_([u'                                        ', escape_(page, False), u'\n'])
    extend_([u'                                        <!-- Column 1 end -->\n'])
    extend_([u'                                </div>\n'])
    extend_([u'                                <div class="col2">\n'])
    extend_([u'                                        <!-- Column 2 start -->\n'])
    extend_([u'                        <div id="menu">\n'])
    extend_([u'                                <h2><a href="/">Home</a></h2>\n'])
    extend_([u'                                <h2><a href="/blog/1">Blog</a></h2>\n'])
    extend_([u'                                <h2><a href="/apps">Apps</a></h2>\n'])
    extend_([u'                                <h2><a href="/bio">Bio</a></h2>\n'])
    extend_([u'                            </div>\n'])
    extend_([u'                                        <div id="sideTitle" class="leftBar">\n'])
    extend_([u'                                                <h2><a href="/archive">Archive</a></h2>\n'])
    extend_([u'                                                <h2><a href="/tag/surf">Surf</a></h2>\n'])
    extend_([u'                                                <h2><a href="/tag/software">Software</a></h2>\n'])
    extend_([u'                                                <h2><a href="/tag/electronics">Electronics</a></h2>\n'])
    extend_([u'                                                <h2><a href="/tag/else">Else</a></h2>\n'])
    extend_([u'                        </div>\n'])
    extend_([u'                                        <!-- Column 2 end -->\n'])
    extend_([u'                                </div>\n'])
    extend_([u'                                <div class="col3">\n'])
    extend_([u'                                        <!-- Column 3 start -->\n'])
    extend_([u'                                        <!-- Column 3 end -->\n'])
    extend_([u'                                </div>\n'])
    extend_([u'                        </div>\n'])
    extend_([u'                </div>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <!-- Ends the three column layout-->\n'])
    extend_([u'        <!-- Define the footer for the page -->\n'])
    extend_([u'        <div id="footer">\n'])
    extend_([u'                <center>        \n'])
    extend_([u'                        <div id="copyright">\n'])
    extend_([u'                                <h3>Copyright 2013, Matthew Iannucci</h3>\n'])
    extend_([u'                        </div>\n'])
    extend_([u'                        <div id="siteinfo">\n'])
    extend_([u'                                <p>Site created with web.py, version 0.3 <br/>Updated November 3, 2013</p>\n'])
    extend_([u'                        </div>\n'])
    extend_([u'                </center>\n'])
    extend_([u'        </div>\n'])
    extend_([u'</div>\n'])
    extend_([u'<!-- End the page layout -->\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

base = CompiledTemplate(base, 'templates/base.html')
join_ = base._join; escape_ = base._escape

# coding: utf-8
def archive (posts):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<div id="archiveContainer">\n'])
    extend_([u'    <div id="archiveTitle">\n'])
    extend_([u'        <h1>Archive</h1>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <hr>\n'])
    extend_([u'    <div id="postList">\n'])
    extend_([u'        <table class="archive">\n'])
    for post in loop.setup(posts):
        extend_(['            ', u'<tr>\n'])
        extend_(['            ', u'    <td>\n'])
        extend_(['            ', u'        <h3 class="links"><a href="/view/', escape_(post.url, True), u'">', escape_(post.title, True), u'</a></h3> \n'])
        extend_(['            ', u'    </td>\n'])
        extend_(['            ', u'    <td>\n'])
        extend_(['            ', u'        <h3 id="archiveTime">&nbsp; ', escape_(datestr(post.date), True), u'</h3>\n'])
        extend_(['            ', u'    </td>\n'])
        extend_(['            ', u'</tr>\n'])
    extend_([u'        </table>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])

    return self

archive = CompiledTemplate(archive, 'templates/archive.html')
join_ = archive._join; escape_ = archive._escape

# coding: utf-8
def tagged (tag, posts):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<div id="archiveContainer">\n'])
    extend_([u'    <div id="archiveTitle">\n'])
    extend_([u'        <h1>Posts tagged "', escape_(tag, True), u'"</h1>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <hr>\n'])
    extend_([u'    <div id="postList">\n'])
    extend_([u'        <table class="archive">\n'])
    for post in loop.setup(posts):
        extend_(['            ', u'<tr>\n'])
        extend_(['            ', u'    <td>\n'])
        extend_(['            ', u'        <h3 class="links"><a href="/view/', escape_(post.url, True), u'">', escape_(post.title, True), u'</a></h3> \n'])
        extend_(['            ', u'    </td>\n'])
        extend_(['            ', u'    <td>\n'])
        extend_(['            ', u'        <h3 id="archiveTime">&nbsp; ', escape_(datestr(post.date), True), u'</h3>\n'])
        extend_(['            ', u'    </td>\n'])
        extend_(['            ', u'</tr>\n'])
    extend_([u'        </table>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])

    return self

tagged = CompiledTemplate(tagged, 'templates/tagged.html')
join_ = tagged._join; escape_ = tagged._escape

# coding: utf-8
def login (user, form):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<p>You are not logged in.</p>\n'])
    extend_([u'        <p>\n'])
    extend_([u'        <form name="login" method="POST"> \n'])
    extend_([u'        ', escape_(form.render(), False), u'\n'])
    extend_([u'        <input type="submit" name="button" value="Login" />\n'])
    extend_([u'        </form>\n'])
    extend_([u'    </p>\n'])
    extend_([u'    <p> user: ', escape_(user, True), u'</p>\n'])
    extend_([u'\n'])

    return self

login = CompiledTemplate(login, 'templates/login.html')
join_ = login._join; escape_ = login._escape

