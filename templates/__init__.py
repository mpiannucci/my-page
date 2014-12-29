from web.template import CompiledTemplate, ForLoop, TemplateResult


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
    extend_([u'<h1>Projects</h1>\n'])
    extend_([u'<hr>\n'])
    extend_([u'<div class="row">\n'])
    extend_([u'        <div id="HackWindsCols" class="col-sm-9">\n'])
    extend_([u'                <h2>HackWinds</h2>\n'])
    extend_([u'                <p class="links">Viewing the surf camera for Narragansett, RI has always proved to be tedious on a smartphone. I I started a project to make viewing the surf camera out of conviencence. Now I have made it into a fully featured application. The app shows the live HD stream straight from the beach. It shows forecast info from <a href="http://magicseaweed.com">MagicSeaweed</a>, tide information from <a href="http://www.wunderground.com/?apiref=b80661e4fc362f50">Wunderground</a>, and live buoy data from NOAA. It\'s all of the tools you need to check the surf quickly in Rhode Island.</p> \n'])
    extend_([u'                <p class="links">The Android app is available on Google Play now, and the iOS app is available from the App Store! Finally, feel free to check out the source on my Github by following the links below. Pray for waves!</p>\n'])
    extend_([u'                <center>\n'])
    extend_([u'                        <!-- This is the iOS app screenshots -->\n'])
    extend_([u'                        <img class="ios_screenshots" id="HWios1" src="/static/Images/Hackwinds-ios1.png" alt="Hackwindsios1" />\n'])
    extend_([u'                        <img class="ios_screenshots" id="HWios2" src="/static/Images/Hackwinds-ios2.png" alt="Hackwindsios2" />\n'])
    extend_([u'                        <img class="ios_screenshots" id="HWios3" src="/static/Images/Hackwinds-ios3.png" alt="Hackwindsios3" />\n'])
    extend_([u'                        <img class="ios_screenshots" id="HWios4" src="/static/Images/Hackwinds-ios4.png" alt="Hackwindsios4" />\n'])
    extend_([u'                        <br/>\n'])
    extend_([u'                        <!-- This is the Android app screenshots\n'])
    extend_([u'                        <img class="android_screenshots" id="HWdroid1" src="/static/Images/Hackwinds-android1.png" alt="Hackwindsdroid1" />\n'])
    extend_([u'                        <img class="android_screenshots" id="HWdroid2" src="/static/Images/Hackwinds-android2.png" alt="Hackwindsdroid2" />\n'])
    extend_([u'                        <img class="android_screenshots" id="HWdroid3" src="/static/Images/Hackwinds-android3.png" alt="Hackwindsdroid3" />\n'])
    extend_([u'                        <img class="android_screenshots" id="HWdroid4" src="/static/Images/Hackwinds-android4.png" alt="Hackwindsdroid4" />\n'])
    extend_([u'                        <br/> -->\n'])
    extend_([u'                        <a href="https://play.google.com/store/apps/details?id=com.nucc.hackwinds">\n'])
    extend_([u'                                <img id="googlePlayBadge" alt="Get it on Google Play" src="https://developer.android.com/images/brand/en_generic_rgb_wo_60.png" />\n'])
    extend_([u'                        </a>\n'])
    extend_([u'                        <br/>\n'])
    extend_([u'                        <a href="https://itunes.apple.com/us/app/hackwinds/id945847570?mt=8&uo=4" target="itunes_store" style="display:inline-block;overflow:hidden;background:url(https://linkmaker.itunes.apple.com/htmlResources/assets/en_us//images/web/linkmaker/badge_appstore-lrg.png) no-repeat;width:135px;height:40px;@media only screen{background-image:url(https://linkmaker.itunes.apple.com/htmlResources/assets/en_us//images/web/linkmaker/badge_appstore-lrg.svg);}"></a>\n'])
    extend_([u'                        <br/>\n'])
    extend_([u'                        <ul class="list-inline">\n'])
    extend_([u'                                <li><a href="https://github.com/mpiannucci/HackWinds">Android Source Here</a></li>\n'])
    extend_([u'                                <li><a href="https://github.com/mpiannucci/HackWinds-iOS">iOS Source Here</a></li>\n'])
    extend_([u'                        </ul>\n'])
    extend_([u'                </center>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <div id="OtherCols" class="col-sm-3 text-center">\n'])
    extend_([u'                <h2>Other</h2>\n'])
    extend_([u'                <p>To view many of my smaller projects and meddlings of mine, feel free to browse my projects on Github.</p>\n'])
    extend_([u'                <center>\n'])
    extend_([u'                        <ul class="list-inline">\n'])
    extend_([u'                                <li><a href="/github">View My Github Here</a></li>\n'])
    extend_([u'                        </ul>\n'])
    extend_([u'                </center>       \n'])
    extend_([u'        </div>\n'])
    extend_([u'</div>\n'])

    return self

apps = CompiledTemplate(apps, 'templates/apps.html')
join_ = apps._join; escape_ = apps._escape

# coding: utf-8
def archive (posts):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<h1>Archive</h1>\n'])
    extend_([u'<hr>\n'])
    extend_([u'<div class="row">\n'])
    extend_([u'    <div id="postList" class="col-lg-12">\n'])
    extend_([u'        <ul class="list-inline">\n'])
    for post in loop.setup(posts):
        extend_(['            ', u'<li><h3 class="links"><a href="/view/', escape_(post.url, True), u'">', escape_(post.title, True), u'</a></h3></li>\n'])
        extend_(['            ', u'<li><h3 id="archiveTime">&nbsp; ', escape_(datestr(post.date), True), u'</h3></li>\n'])
    extend_([u'        </ul>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])

    return self

archive = CompiledTemplate(archive, 'templates/archive.html')
join_ = archive._join; escape_ = archive._escape

# coding: utf-8
def base (page):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<!DOCTYPE html>\n'])
    extend_([u'<html>\n'])
    extend_([u'<head>\n'])
    extend_([u'    <meta name="google-site-verification" content="-azLgyDbTQ6EY0zdkcRBc8Q5f0jSV4cd552gcq44N98" />\n'])
    extend_([u'    <meta name="viewport" content="width=device-width, initial-scale=1">\n'])
    extend_([u'    <title>Matthew Iannucci</title>\n'])
    extend_([u'    <link rel="shortcut icon" type="image/x-icon" href="/static/favicon.ico" />\n'])
    extend_([u'        <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">\n'])
    extend_([u'        <link rel="stylesheet" href="/static/Scripts/mpi.css">\n'])
    extend_([u'        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>\n'])
    extend_([u'        <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>\n'])
    extend_([u'</head>\n'])
    extend_([u'<body> \n'])
    extend_([u'<div  class="container">\n'])
    extend_([u'    <!-- Navigation Bar -->\n'])
    extend_([u'    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u'            <!-- Brand and toggle get grouped for better mobile display -->\n'])
    extend_([u'            <div class="navbar-header">\n'])
    extend_([u'                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n'])
    extend_([u'                    <span class="sr-only">Toggle navigation</span>\n'])
    extend_([u'                    <span class="icon-bar"></span>\n'])
    extend_([u'                    <span class="icon-bar"></span>\n'])
    extend_([u'                    <span class="icon-bar"></span>\n'])
    extend_([u'                </button>\n'])
    extend_([u'                <a class="navbar-brand" href="/">Matthew Iannucci</a>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <!-- Collect the nav links, forms, and other content for toggling -->\n'])
    extend_([u'            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n'])
    extend_([u'                <ul class="nav navbar-nav">\n'])
    extend_([u'                    <li>\n'])
    extend_([u'                        <a href="/blog">Blog</a>\n'])
    extend_([u'                    </li>\n'])
    extend_([u'                    <li>\n'])
    extend_([u'                        <a href="/apps">Projects</a>\n'])
    extend_([u'                    </li>\n'])
    extend_([u'                    <li>\n'])
    extend_([u'                        <a href="/bio">About</a>\n'])
    extend_([u'                    </li>\n'])
    extend_([u'                </ul>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <!-- /.navbar-collapse -->\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <!-- /.container -->\n'])
    extend_([u'    </nav>\n'])
    extend_([u'        <!-- Create the main coloumn layout.-->\n'])
    extend_([u'        <div id="mainContent">\n'])
    extend_([u'                <!-- Main column start -->\n'])
    extend_([u'                <!-- Get the page data as declared in code.py -->\n'])
    extend_([u'                ', escape_(page, False), u'\n'])
    extend_([u'                <!-- Main column end -->\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <!-- Ends the three column layout-->\n'])
    extend_([u'        <!-- Define the footer for the page -->\n'])
    extend_([u'        <div class="row">\n'])
    extend_([u'        <div class="col-lg-12 text-center">\n'])
    extend_([u'                <ul class="list-unstyled">\n'])
    extend_([u'                                <li>Copyright 2013, Matthew Iannucci</li>\n'])
    extend_([u'                                <li>Site created with web.py, version 0.3</li>\n'])
    extend_([u'                                <li>Updated January 2015</li>\n'])
    extend_([u'                        </ul>\n'])
    extend_([u'                </div>\n'])
    extend_([u'        </div>\n'])
    extend_([u'</div>\n'])
    extend_([u'<!-- End the page layout -->\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

base = CompiledTemplate(base, 'templates/base.html')
join_ = base._join; escape_ = base._escape

# coding: utf-8
def bio():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<h1>Bio</h1>\n'])
    extend_([u'<hr>\n'])
    extend_([u'<div class="row">\n'])
    extend_([u'        <div id="bioPhoto" class="col-sm-6">\n'])
    extend_([u'                <img id="bioPic" src="/static/Images/mecomp.jpg" alt="bioPic" />\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <div id="bioText" class="col-sm-6">\n'])
    extend_([u'                <h2>About Me</h2>\n'])
    extend_([u"                <p>Hello, my name is Matthew Iannucci. I am an Engineer from Rhode Island with a Bachelor's of Science in Ocean Engineering from the University of Rhode Island. I focused on software development and robotics. I currently work as an Engineer at Navatek, Ltd.</p>\n"])
    extend_([u'                <p>I enjoy surfing and skiing in my free time, as well as working on many different software projects.</p>\n'])
    extend_([u'                <ul class="list-inline">\n'])
    extend_([u'                        <li><a href="/resume">Resume</a></li>\n'])
    extend_([u'                        <li><a href="https://github.com/mpiannucci">Github</a></li>\n'])
    extend_([u'                        <li><a href="mailto:rhodysurf13@gmail.com">Email</a></li>\n'])
    extend_([u'                        <li><a href="http://www.linkedin.com/pub/matthew-iannucci/7a/884/64a/">LinkedIn</a></li>\n'])
    extend_([u'                </ul>\n'])
    extend_([u'        </div>\n'])
    extend_([u'</div>\n'])

    return self

bio = CompiledTemplate(bio, 'templates/bio.html')
join_ = bio._join; escape_ = bio._escape

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
    extend_([u'<h1>Blog</h1>\n'])
    extend_([u'<hr>\n'])
    extend_([u'<!-- Loop thourgh all posts in the database and display them as declared below -->\n'])
    for post in loop.setup(posts):
        postCount+=1
        extend_([u'    <div class="row">\n'])
        extend_([u'        <div class="col-lg-12">\n'])
        extend_([u'            <h2 class="links"><a href="/view/', escape_(post.url, True), u'">', escape_(post.title, True), u'</a></h2>\n'])
        extend_([u'            <h3>', escape_(datestr(post.date), True), u'</h3>\n'])
        extend_([u'            ', escape_(post.content, False), u'\n'])
        extend_([u'            <br/>\n'])
        extend_([u'            <div id="links" class="links">\n'])
        extend_([u'                <ul class="list-inline">\n'])
        extend_([u'                    <li><a href="/view/', escape_(post.url, True), u'">Comment</a></li>\n'])
        extend_([u'                    <li>Tagged &nbsp; <a href="/tag/', escape_(post.tag, True), u'">', escape_(post.tag, True), u'</a></li>\n'])
        extend_([u'                </ul>\n'])
        extend_([u'            </div>\n'])
        extend_([u'        </div>\n'])
        extend_([u'    </div>\n'])
    extend_([u'<hr>\n'])
    extend_([u'<div id="blogLinks" class="row">\n'])
    extend_([u'    <div class="col-lg-12">\n'])
    if pageNum == 1:
        if postCount < 6:
            extend_(['        ', u'<ul class="list-inline">\n'])
            extend_(['        ', u'    <li>Page ', escape_(pageNum, True), u'</li>\n'])
            extend_(['        ', u'    <li><a href="/archive">Archive</a></li>\n'])
            extend_(['        ', u'</ul>\n'])
        else:
            extend_(['        ', u'<ul class="list-inline">\n'])
            extend_(['        ', u'    <li>Page ', escape_(pageNum, True), u'</li>\n'])
            extend_(['        ', u'    <li><a href="/blog/', escape_(next, True), u'">Next</a></li>\n'])
            extend_(['        ', u'    <li><a href="/archive">Archive</a></li>\n'])
            extend_(['        ', u'</ul>\n'])
    else:
        if postCount < 6:
            extend_(['        ', u'<ul class="list-inline">\n'])
            extend_(['        ', u'    <li><a href="/blog/', escape_(prev, True), u'">Previous</a></li>\n'])
            extend_(['        ', u'    <li>Page ', escape_(pageNum, True), u'</li>\n'])
            extend_(['        ', u'    <li><a href="/archive">Archive</a></li>\n'])
            extend_(['        ', u'</ul>\n'])
        else:
            extend_(['        ', u'<ul class="list-inline">\n'])
            extend_(['        ', u'    <li><a href="/blog/', escape_(prev, True), u'">Previous</a></li>\n'])
            extend_(['        ', u'    <li>Page ', escape_(pageNum, True), u'</li>\n'])
            extend_(['        ', u'    <li><a href="/blog/', escape_(next, True), u'">Next</a></li>\n'])
            extend_(['        ', u'    <li><a href="/archive">Archive</a></li>\n'])
            extend_(['        ', u'</ul>\n'])
    extend_([u'    </div>\n'])
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
def index():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div class="row">\n'])
    extend_([u'    <div class="col-lg-12 text-center">\n'])
    extend_([u'        <img id="homeImage" src="/static/Images/stillsurf.jpg">\n'])
    extend_([u'        <h2>Welcome..</h2>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])

    return self

index = CompiledTemplate(index, 'templates/index.html')
join_ = index._join; escape_ = index._escape

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
def tagged (tag, posts):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<h1>Posts tagged "', escape_(tag, True), u'"</h1>\n'])
    extend_([u'<hr>\n'])
    extend_([u'<div class="row">\n'])
    extend_([u'    <div id="postList" class="col-lg-12">\n'])
    extend_([u'        <ul class="list-inline">\n'])
    for post in loop.setup(posts):
        extend_(['            ', u'<li><h3 class="links"><a href="/view/', escape_(post.url, True), u'">', escape_(post.title, True), u'</a></h3></li>\n'])
        extend_(['            ', u'<li><h3 id="archiveTime">&nbsp; ', escape_(datestr(post.date), True), u'</h3></li>\n'])
    extend_([u'        </ul>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])

    return self

tagged = CompiledTemplate(tagged, 'templates/tagged.html')
join_ = tagged._join; escape_ = tagged._escape

# coding: utf-8
def view (post):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<div class="row">\n'])
    extend_([u'    <div class="col-lg-12">\n'])
    extend_([u'        <h1>', escape_(post.title, True), u'</h1>\n'])
    extend_([u'        <h3>', escape_(datestr(post.date), True), u'</h3>\n'])
    extend_([u'        ', escape_(post.content, False), u'\n'])
    extend_([u'        <br/>\n'])
    extend_([u'        <div id="links" class="links">\n'])
    extend_([u'            <ul class="list-inline">\n'])
    extend_([u'                <li><a href="/view/', escape_(post.url, True), u'">Link</a></li>\n'])
    extend_([u'                <li>Tagged &nbsp; <a href="/tag/', escape_(post.tag, True), u'">', escape_(post.tag, True), u'</a></li>\n'])
    extend_([u'            </ul>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])
    extend_([u'<br/>\n'])
    extend_([u'<div id="commentSection">\n'])
    extend_([u'    <div id="disqus_thread"></div>\n'])
    extend_([u'    <script type="text/javascript">\n'])
    extend_([u'        /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */\n'])
    extend_([u"        var disqus_shortname = 'matthewiannucci'; // required: replace example with your forum shortname\n"])
    extend_([u'\n'])
    extend_([u"        /* * * DON'T EDIT BELOW THIS LINE * * */\n"])
    extend_([u'        (function() {\n'])
    extend_([u"            var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;\n"])
    extend_([u"            dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';\n"])
    extend_([u"            (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);\n"])
    extend_([u'        })();\n'])
    extend_([u'    </script>\n'])
    extend_([u'    <noscript>Please enable JavaScript to view the <a href="http://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>\n'])
    extend_([u'    <a href="http://disqus.com" class="dsq-brlink">comments powered by <span class="logo-disqus">Disqus</span></a>\n'])
    extend_([u'</div>\n'])

    return self

view = CompiledTemplate(view, 'templates/view.html')
join_ = view._join; escape_ = view._escape

