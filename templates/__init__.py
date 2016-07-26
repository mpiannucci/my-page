from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def admin (user, posts):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'\n'])
    extend_([u'<div id="adminContainer" class="row">\n'])
    extend_([u'    <div class="col-lg-12">\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u'            <h3>Logged in as <em>', escape_(user, True), u'</em></h3>\n'])
    extend_([u'            <a class="btn btn-primary" href="/new">New Post</a>\n'])
    extend_([u'            <a class="btn btn-danger" href="/logout">Log Out</a>\n'])
    extend_([u'            <hr>\n'])
    extend_([u'            <h3>Edit posts</h3>\n'])
    for post in loop.setup(posts):
        extend_(['                ', u'<div class="postlist">\n'])
        extend_(['                ', u'    <p><a href="/view/', escape_(post.url, True), u'">', escape_(post.title, True), u'</a> ', escape_(datestr(post.date), True), u'</p>\n'])
        extend_(['                ', u'    <ul class="list-inline">\n'])
        extend_(['                ', u'        <li><a class="btn btn-default" href="/edit/', escape_(post.url, True), u'">Edit</a></li>\n'])
        extend_(['                ', u'        <li><form action="/delete/', escape_(post.url, True), u'" method="post">\n'])
        extend_(['                ', u'            <input type="submit" class="btn btn-danger" value="Delete post" />\n'])
        extend_(['                ', u'        </form></li>\n'])
        extend_(['                ', u'    </ul>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])

    return self

admin = CompiledTemplate(admin, 'templates/admin.html')
join_ = admin._join; escape_ = admin._escape

# coding: utf-8
def apps():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div class="row">\n'])
    extend_([u'<div id="HackWindsCols" class="col-lg-12 jumbotron hackwinds-jumbotron">\n'])
    extend_([u'    <div class="container">\n'])
    extend_([u'        <div class="col-sm-2">\n'])
    extend_([u'            <img class="img-responsive apps-page-screenshot" src="/static/Images/hackwinds-logo.png" />\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <div class="col-sm-10">\n'])
    extend_([u'            <h1>HackWinds</h1>\n'])
    extend_([u'            <p>The easiest way to check the surf in Rhode Island</p>\n'])
    extend_([u'            <a href="/hackwinds" class="btn btn-primary">Download it Now!</a>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])
    extend_([u'<div id="RhodyCastCols" class="col-lg-12 jumbotron rhodycast-jumbotron">\n'])
    extend_([u'    <div class="container">\n'])
    extend_([u'        <div class="col-sm-2">\n'])
    extend_([u'            <img class="img-responsive" src="/static/Images/rhodycast-logo.png" />\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <div class="col-sm-10">\n'])
    extend_([u'            <h1>RhodyCast</h1>\n'])
    extend_([u'            <p>Simple Rhode Island surf forecasting web site using NOAA WaveWatch III</p>\n'])
    extend_([u'            <a href="https://rhodycast.appspot.com" class="btn btn-primary">Check It Out</a>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])
    extend_([u'<div id="SwellScoreCols" class="col-lg-12 jumbotron swellscore-jumbotron">\n'])
    extend_([u'    <div class="container">\n'])
    extend_([u'        <div class="col-sm-2">\n'])
    extend_([u'            <img class="img-responsive" src="/static/Images/swellscore-logo.png" />\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <div class="col-sm-10">\n'])
    extend_([u'            <h1>SwellScore</h1>\n'])
    extend_([u'            <p>Track your surf sessions and observations so you know the best spot for future swells</p>\n'])
    extend_([u'            <a href="https://swellscore-1093.appspot.com" class="btn btn-primary">Learn More</a>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])
    extend_([u'<div id="MapgetterCols" class="col-lg-12 jumbotron mapgetter-jumbotron">\n'])
    extend_([u'    <div class="container">\n'])
    extend_([u'        <h1>MapGetter</h1>\n'])
    extend_([u'        <p>Get static images of a central area with coordinates in meters</p>\n'])
    extend_([u'        <a href="http://mapgetter.mpiannucci.com" class="btn btn-primary">Try It!</a>\n'])
    extend_([u'        <a href="https://github.com/mpiannucci/MapGetter" class="btn btn-info">View the Source</a>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])
    extend_([u'<div id="OtherCols" class="col-lg-12 jumbotron github-jumbotron">\n'])
    extend_([u'    <div class="container">\n'])
    extend_([u'        <h2>Other</h2>\n'])
    extend_([u'        <p>To view many of my smaller projects and medlings of mine, feel free to browse my projects on Github.</p>\n'])
    extend_([u'        <a class="btn btn-primary" href="/github">View My Github Here</a>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])
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
    extend_([u'<div class="row">\n'])
    extend_([u'    <div id="postList" class="col-lg-12">\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u'            <h1>Archive</h1>\n'])
    extend_([u'            <hr> \n'])
    for post in loop.setup(posts):
        extend_(['                ', u'<ul class="list-inline">\n'])
        extend_(['                ', u'    <li>\n'])
        extend_(['                ', u'        <h3 class="links"><a href="/view/', escape_(post.url, True), u'">', escape_(post.title, True), u'</a></h3>\n'])
        extend_(['                ', u'    </li>\n'])
        extend_(['                ', u'    <li>\n'])
        extend_(['                ', u'        <h3 id="archiveTime">&nbsp; ', escape_(datestr(post.date), True), u'</h3>\n'])
        extend_(['                ', u'    </li>\n'])
        extend_(['                ', u'</ul>\n'])
    extend_([u'        </div>\n'])
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
    extend_([u'\n'])
    extend_([u'<head>\n'])
    extend_([u'    <meta name="google-site-verification" content="-azLgyDbTQ6EY0zdkcRBc8Q5f0jSV4cd552gcq44N98" />\n'])
    extend_([u'    <meta name="viewport" content="width=device-width, initial-scale=1">\n'])
    extend_([u'    <title>Matthew Iannucci</title>\n'])
    extend_([u'    <link rel="shortcut icon" type="image/x-icon" href="/static/favicon.ico" />\n'])
    extend_([u'    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">\n'])
    extend_([u'    <link rel="stylesheet" href="/static/Styles/mpi.css">\n'])
    extend_([u'    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>\n'])
    extend_([u'    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>\n'])
    extend_([u'</head>\n'])
    extend_([u'\n'])
    extend_([u'<body>\n'])
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
    extend_([u'                </ul>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <!-- /.navbar-collapse -->\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <!-- /.container -->\n'])
    extend_([u'    </nav>\n'])
    extend_([u'    <div id="contentContainer" class="container-fluid">\n'])
    extend_([u'        <!-- Create the Main Content layout.-->\n'])
    extend_([u'        <!-- Get the Main Content from the server -->\n'])
    extend_([u'        ', escape_(page, False), u'\n'])
    extend_([u'        <!-- Ends Main Content Layout -->\n'])
    extend_([u'        <!-- Begin the Footer Layout -->\n'])
    extend_([u'        <div id="footerRow" class="row">\n'])
    extend_([u'            <div class="col-lg-12 text-center">\n'])
    extend_([u'                <ul class="list-unstyled">\n'])
    extend_([u'                    <li>Copyright 2013, Matthew Iannucci</li>\n'])
    extend_([u'                    <li>Site created with web.py, version 0.3</li>\n'])
    extend_([u'                    <li>Updated January 2015</li>\n'])
    extend_([u'                </ul>\n'])
    extend_([u'            </div>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <!-- End the Footer layout -->\n'])
    extend_([u'    <script type="text/javascript">\n'])
    extend_([u'/* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */\n'])
    extend_([u"var disqus_shortname = 'matthewiannucci'; // required: replace example with your forum shortname\n"])
    extend_([u'\n'])
    extend_([u"/* * * DON'T EDIT BELOW THIS LINE * * */\n"])
    extend_([u'(function () {\n'])
    extend_([u"var s = document.createElement('script'); s.async = true;\n"])
    extend_([u"s.type = 'text/javascript';\n"])
    extend_([u"s.src = '//' + disqus_shortname + '.disqus.com/count.js';\n"])
    extend_([u"(document.getElementsByTagName('HEAD')[0] || document.getElementsByTagName('BODY')[0]).appendChild(s);\n"])
    extend_([u'}());\n'])
    extend_([u'</script>\n'])
    extend_([u'\n'])
    extend_([u'</body>\n'])
    extend_([u'\n'])
    extend_([u'</html>\n'])

    return self

base = CompiledTemplate(base, 'templates/base.html')
join_ = base._join; escape_ = base._escape

# coding: utf-8
def bio():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div class="row">\n'])
    extend_([u'    <div id="bioPhoto" class="col-sm-6 jumbotron">\n'])
    extend_([u'        <img id="bioPic" src="/static/Images/me_surf.jpg" alt="bioPic" />\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div id="bioText" class="col-sm-6">\n'])
    extend_([u'            <h2>About Me</h2>\n'])
    extend_([u"            <p>Hello, my name is Matthew Iannucci. I am an Engineer from Rhode Island with a Bachelor's of Science in Ocean Engineering from the University of Rhode Island. I focused on software development and robotics. I currently work as an Engineer at Navatek, Ltd.</p>\n"])
    extend_([u'            <p>I enjoy surfing and skiing in my free time, as well as working on many different software projects.</p>\n'])
    extend_([u'            <ul class="list-inline">\n'])
    extend_([u'                <li><a href="/resume">Resume</a>\n'])
    extend_([u'                </li>\n'])
    extend_([u'                <li><a href="https://github.com/mpiannucci">Github</a>\n'])
    extend_([u'                </li>\n'])
    extend_([u'                <li><a href="mailto:rhodysurf13@gmail.com">Email</a>\n'])
    extend_([u'                </li>\n'])
    extend_([u'                <li><a href="http://www.linkedin.com/pub/matthew-iannucci/7a/884/64a/">LinkedIn</a>\n'])
    extend_([u'                </li>\n'])
    extend_([u'            </ul>\n'])
    extend_([u'    </div>\n'])
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
    extend_([u'<!-- Loop thourgh all posts in the database and display them as declared below -->\n'])
    for post in loop.setup(posts):
        postCount+=1
        extend_([u'    <div class="row">\n'])
        extend_([u'        <div class="col-lg-12">\n'])
        extend_([u'            <div class="container">\n'])
        extend_([u'            <h2 class="links"><a href="/view/', escape_(post.url, True), u'">', escape_(post.title, True), u'</a></h2>\n'])
        extend_([u'            <h3>', escape_(datestr(post.date), True), u'</h3>\n'])
        if len(post.content) > 500:
            extend_(['            ', escape_(post.content[:500], False), u'\n'])
            extend_(['            ', u'... <a href="/view/', escape_(post.url, True), u'">View Whole Post</a>\n'])
        else:
            extend_(['            ', escape_(post.content, False), u'\n'])
        extend_([u'            <br/>\n'])
        extend_([u'            <div id="links" class="links">\n'])
        extend_([u'                <ul class="list-inline">\n'])
        url = post.url + "#disqus_thread"
        extend_([u'                    <li><a href="/view/', escape_(url, True), u'">Comment</a></li>\n'])
        extend_([u'                    <li>\n'])
        extend_([u'                        Tags: &nbsp; \n'])
        for tag in loop.setup(post.tag):
            extend_(['                        ', u'<a href="/tag/', escape_(tag, True), u'">', escape_(tag, True), u'</a>\n'])
        extend_([u'                    </li>\n'])
        extend_([u'                </ul>\n'])
        extend_([u'            </div>\n'])
        extend_([u'            </div>\n'])
        extend_([u'        </div>\n'])
        extend_([u'    </div>\n'])
        extend_([u'    <hr>\n'])
    extend_([u'<div id="blogLinks" class="row">\n'])
    extend_([u'    <div class="col-lg-12">\n'])
    extend_([u'        <div class="container">\n'])
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
    extend_([u'        </div>\n'])
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
    extend_([u'<div class="row">\n'])
    extend_([u'    <div class="col-lg-12">\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u'            <h1>Edit Post: ', escape_(form.d.title, True), u'</h1>\n'])
    extend_([u'            <form action="" method="post">\n'])
    extend_([u'                ', escape_(form.render_css(), False), u'\n'])
    extend_([u'            </form>\n'])
    extend_([u'            <form action="/delete/', escape_(post.url, True), u'" method="post">\n'])
    extend_([u'                <input type="submit" value="Delete post" class="btn btn-danger" style="margin-top:10px;" />\n'])
    extend_([u'            </form>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])

    return self

edit = CompiledTemplate(edit, 'templates/edit.html')
join_ = edit._join; escape_ = edit._escape

# coding: utf-8
def hackwinds():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<!-- Jumbotron Header -->\n'])
    extend_([u'<div class="row">\n'])
    extend_([u'    <div class="col-lg-12 jumbotron hackwinds-jumbotron hackwinds-landing">\n'])
    extend_([u'        <div class="col-lg-6">\n'])
    extend_([u'            <img class="hackwinds_landing_screenshots" src="/static/Images/hackwinds-landing.png" />\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <div class="col-lg-6">\n'])
    extend_([u'            <h1>HackWinds</h1>\n'])
    extend_([u'            <p>The easiest way to check the waves in Rhode Island</p>\n'])
    extend_([u'            <a href="https://geo.itunes.apple.com/us/app/hackwinds/id945847570?mt=8" style="display:inline-block;overflow:hidden;background:url(http://linkmaker.itunes.apple.com/images/badges/en-us/badge_appstore-lrg.svg) no-repeat;width:165px;height:40px;"></a>\n'])
    extend_([u'            <br/>\n'])
    extend_([u'            <a href="https://play.google.com/store/apps/details?id=com.nucc.hackwinds&hl=en&utm_source=global_co&utm_medium=prtnr&utm_content=Mar2515&utm_campaign=PartBadge&pcampaignid=MKT-AC-global-none-all-co-pr-py-PartBadges-Oct1515-1"><img alt="Get it on Google Play" src="https://play.google.com/intl/en_us/badges/images/apps/en-play-badge.png" style="width:135px;"/></a>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])
    extend_([u'<div class="row">\n'])
    extend_([u'    <div class="col-lg-3 hackwinds-feature-col">\n'])
    extend_([u'        <span class="glyphicon glyphicon-picture"></span>\n'])
    extend_([u'        <h3>Live HD Images</h2>\n'])
    extend_([u'        <p>View the HD camera images straight from Narragansett Beach wherever you are, curtesy of <a href="http://www.warmwinds.com/">Warm Winds Surf Shop</a></p>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div class="col-lg-3 hackwinds-feature-col">\n'])
    extend_([u'        <span class="glyphicon glyphicon-tasks"></span>\n'])
    extend_([u'        <h3>5 Day Forecast</h3>\n'])
    extend_([u'        <p>Get the latest forecast information for the upcoming 7 days straight from <a href="http://forecast.mpiannucci.com">RhodyCast</a>, the only surf forecast made exclusively for Rhode Island</p>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div class="col-lg-3 hackwinds-feature-col">\n'])
    extend_([u'        <span class="glyphicon glyphicon-stats"></span>\n'])
    extend_([u'        <h3>Live Buoy Data</h3>\n'])
    extend_([u'        <p>Get the latest NOAA buoy reports, showing the current swell in the water. Convienently view the current wave spectra breakdown from Block Island, Montauk, and Nantucket.</p>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div class="col-lg-3 hackwinds-feature-col">\n'])
    extend_([u'        <span class="glyphicon glyphicon-calendar"></span>\n'])
    extend_([u'        <h3>Tide Information</h3>\n'])
    extend_([u'        <p>View the upcoming tides, as well as the sunrise and sunset for the day so you can plan whether to dawn patrol or leave work early.</p>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])
    extend_([u'\n'])
    extend_([u'<!-- Page Features -->\n'])
    extend_([u'<!-- <div class="row text-center ">\n'])
    extend_([u'    <div class="col-lg-12 hero-feature">\n'])
    extend_([u'        <h1>Features</h1>\n'])
    extend_([u'        <ul class="nav nav-pills center-pills">\n'])
    extend_([u'            <li class="active"><a data-toggle="tab" href="#iosScreenshots">iOS</a></li>\n'])
    extend_([u'            <li><a data-toggle="tab" href="#androidScreenshots">Android</a></li>\n'])
    extend_([u'        </ul>\n'])
    extend_([u'    </div>\n'])
    extend_([u'    <div class="tab-content">\n'])
    extend_([u'        <div class="tab-pane active" id="iosScreenshots">\n'])
    extend_([u'            <div class="col-md-4 col-sm-6 hero-feature">\n'])
    extend_([u'                <div class="thumbnail">\n'])
    extend_([u'                    <img class="hackwinds_landing_screenshots" src="/static/Images/Screenshots/hackwinds-ios-live.png" alt="Live Screenshot">\n'])
    extend_([u'                    <div class="caption">\n'])
    extend_([u'                        <h3>Live Beach View</h3>\n'])
    extend_([u'                        <p>View the HD camera images straight from Narragansett Beach wherever you are.</p>\n'])
    extend_([u'                    </div>\n'])
    extend_([u'                </div>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="col-md-4 col-sm-6 hero-feature">\n'])
    extend_([u'                <div class="thumbnail">\n'])
    extend_([u'                    <img class="hackwinds_landing_screenshots" src="/static/Images/Screenshots/hackwinds-ios-forecast.png" alt="Forecast Screenshot">\n'])
    extend_([u'                    <div class="caption">\n'])
    extend_([u'                        <h3>5 Day Forecast</h3>\n'])
    extend_([u'                        <p>Get the latest forecast information for the upcoming 7 days straight from <a href="http://forecast.mpiannucci.com">RhodyCast</a>.</p>\n'])
    extend_([u'                    </div>\n'])
    extend_([u'                </div>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="col-md-4 col-sm-6 hero-feature">\n'])
    extend_([u'                <div class="thumbnail">\n'])
    extend_([u'                    <img class="hackwinds_landing_screenshots" src="/static/Images/Screenshots/hackwinds-ios-chart.png" alt="Detail Forecast Screenshot">\n'])
    extend_([u'                    <div class="caption">\n'])
    extend_([u'                        <h3>Animated Forecast Charts</h3>\n'])
    extend_([u'                        <p>View animated wave, wind, and period forecast charts for each day of the upcoming week.</p>\n'])
    extend_([u'                    </div>\n'])
    extend_([u'                </div>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="col-md-offset-2 col-md-4 col-sm-6 hero-feature">\n'])
    extend_([u'                <div class="thumbnail">\n'])
    extend_([u'                    <img class="hackwinds_landing_screenshots" src="/static/Images/Screenshots/hackwinds-ios-buoy.png" alt="Buoy Screenshot">\n'])
    extend_([u'                    <div class="caption">\n'])
    extend_([u'                        <h3>Live Buoy Data</h3>\n'])
    extend_([u'                        <p>Get the latest NOAA buoy reports, showing the current swell in the water. Convienently view the current wave spectra breakdown from Block Island, Montauk, and Nantucket.</p>\n'])
    extend_([u'                    </div>\n'])
    extend_([u'                </div>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="col-md-4 col-sm-6 hero-feature">\n'])
    extend_([u'                <div class="thumbnail">\n'])
    extend_([u'                    <img class="hackwinds_landing_screenshots" src="/static/Images/Screenshots/hackwinds-ios-tide.png" alt="Tide Screenshot">\n'])
    extend_([u'                    <div class="caption">\n'])
    extend_([u'                        <h3>Tide Information</h3>\n'])
    extend_([u'                        <p>View the upcoming tides, as well as the sunrise and sunset for the upcoming 4 days so you can plan whether to dawn patrol or leave work early.</p>\n'])
    extend_([u'                    </div>\n'])
    extend_([u'                </div>\n'])
    extend_([u'            </div>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        <div class="tab-pane" id="androidScreenshots">\n'])
    extend_([u'            <div class="col-md-4 col-sm-6 hero-feature">\n'])
    extend_([u'                <div class="thumbnail">\n'])
    extend_([u'                    <img class="hackwinds_landing_screenshots" src="/static/Images/Screenshots/hackwinds-android-live.png" alt="Live Screenshot">\n'])
    extend_([u'                    <div class="caption">\n'])
    extend_([u'                        <h3>Live Beach View</h3>\n'])
    extend_([u'                        <p>View the HD camera images straight from Narragansett Beach wherever you are.</p>\n'])
    extend_([u'                    </div>\n'])
    extend_([u'                </div>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="col-md-4 col-sm-6 hero-feature">\n'])
    extend_([u'                <div class="thumbnail">\n'])
    extend_([u'                    <img class="hackwinds_landing_screenshots" src="/static/Images/Screenshots/hackwinds-android-forecast.png" alt="Forecast Screenshot">\n'])
    extend_([u'                    <div class="caption">\n'])
    extend_([u'                        <h3>7 Day Forecast</h3>\n'])
    extend_([u'                        <p>Get the latest forecast information for the upcoming 7 days straight from <a href="http://forecast.mpiannucci.com">RhodyCast</a>.</p>\n'])
    extend_([u'                    </div>\n'])
    extend_([u'                </div>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="col-md-4 col-sm-6 hero-feature">\n'])
    extend_([u'                <div class="thumbnail">\n'])
    extend_([u'                    <img class="hackwinds_landing_screenshots" src="/static/Images/Screenshots/hackwinds-android-chart.png" alt="Charts Screenshot">\n'])
    extend_([u'                    <div class="caption">\n'])
    extend_([u'                        <h3>Animated Forecast Charts</h3>\n'])
    extend_([u'                        <p>View animated wave, wind, and period forecast charts for each day of the upcoming week.</p>\n'])
    extend_([u'                    </div>\n'])
    extend_([u'                </div>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="col-md-offset-2 col-md-4 col-sm-6 hero-feature">\n'])
    extend_([u'                <div class="thumbnail">\n'])
    extend_([u'                    <img class="hackwinds_landing_screenshots" src="/static/Images/Screenshots/hackwinds-android-buoy.png" alt="Buoy Screenshot">\n'])
    extend_([u'                    <div class="caption">\n'])
    extend_([u'                        <h3>Live Buoy Data</h3>\n'])
    extend_([u'                        <p>Get the latest NOAA buoy reports, showing the current swell in the water. Convienently view the current wave spectra breakdown from Block Island, Montauk, and Nantucket.</p>\n'])
    extend_([u'                    </div>\n'])
    extend_([u'                </div>\n'])
    extend_([u'            </div>\n'])
    extend_([u'            <div class="col-md-4 col-sm-6 hero-feature">\n'])
    extend_([u'                <div class="thumbnail">\n'])
    extend_([u'                    <img class="hackwinds_landing_screenshots" src="/static/Images/Screenshots/hackwinds-android-tide.png" alt="Tide Screenshot">\n'])
    extend_([u'                    <div class="caption">\n'])
    extend_([u'                        <h3>Tide Information</h3>\n'])
    extend_([u'                        <p>View the upcoming tides, as well as the sunrise and sunset for the day so you can plan whether to dawn patrol or leave work early.</p>\n'])
    extend_([u'                    </div>\n'])
    extend_([u'                </div>\n'])
    extend_([u'            </div>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div> -->\n'])
    extend_([u'<!-- /.row -->\n'])
    extend_([u'<!-- Github -->\n'])
    extend_([u'<div class="row">\n'])
    extend_([u'    <div class="col-lg-12 text-center jumbotron">\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u'            <h1 id="githubHeader">Open Source</h1>\n'])
    extend_([u"            <p>Both the Android and iOS versions of the app are totally open sourced! Hack away and add any features you want to see in the app, and I'll be happy to add them in. Or simply help development by reporting bugs or possible new features.</p>\n"])
    extend_([u'            <a href="https://github.com/mpiannucci/HackWinds-iOS" class="btn btn-info hackwinds-github-button">View the iOS Source</a>\n'])
    extend_([u'            <a href="https://github.com/mpiannucci/HackWinds-Android" class="btn btn-info hackwinds-github-button">View the Android Source</a>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])
    extend_([u'<!-- /.row -->\n'])

    return self

hackwinds = CompiledTemplate(hackwinds, 'templates/hackwinds.html')
join_ = hackwinds._join; escape_ = hackwinds._escape

# coding: utf-8
def index():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div class="row">\n'])
    extend_([u'    <div class="col-lg-12 jumbotron jumbotron-index">\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u'            <h1 class="welcomeMessage">Hello, I\'m Matt</h1>\n'])
    extend_([u'\n'])
    extend_([u"            <p>I am an Engineer from Rhode Island with a Bachelor's of Science in Ocean Engineering from the University of Rhode Island. Growing up in Rhode Island, I was drawn to the ocean. While my heart still lives with the sea, my interests shifted in college, driving me towards electronics and software development. I have forged my own path by layering software development talent on top of traditional engineering principles.</p>\n"])
    extend_([u'\n'])
    extend_([u'            <p>I have worked on a variety of projects including autonomous robotic boats, embedded wireless bridge health monitoring systems, mobile apps, and Naval Ship design software.</p>\n'])
    extend_([u'\n'])
    extend_([u'            <a href="/resume" class="btn btn-primary bio-buttons">Resume</a>\n'])
    extend_([u'            <a href="https://github.com/mpiannucci" class="btn btn-primary bio-buttons">Github</a>\n'])
    extend_([u'            <a href="mailto:rhodysurf13@gmail.com" class="btn btn-primary bio-buttons">Email</a>\n'])
    extend_([u'            <a href="http://www.linkedin.com/pub/matthew-iannucci/7a/884/64a/" class="btn btn-primary bio-buttons">LinkedIn</a>\n'])
    extend_([u'        </div>\n'])
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
    extend_([u'<div class="row">\n'])
    extend_([u'    <div class="col-lg-12">\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u'            <h1>New Blog Post</h1>\n'])
    extend_([u'            <form action="" method="post">\n'])
    extend_([u'                ', escape_(form.render_css(), False), u'\n'])
    extend_([u'            </form>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])

    return self

new = CompiledTemplate(new, 'templates/new.html')
join_ = new._join; escape_ = new._escape

# coding: utf-8
def tagged (tag, posts):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<div class="row">\n'])
    extend_([u'    <div class="col-lg-12">\n'])
    extend_([u'        <div class="container">\n'])
    extend_([u'            <h1>Posts tagged <em>"', escape_(tag, True), u'"</em></h1>\n'])
    extend_([u'            <hr> \n'])
    for post in loop.setup(posts):
        extend_(['                ', u'<ul class="list-inline">\n'])
        extend_(['                ', u'    <li>\n'])
        extend_(['                ', u'        <h3 class="links"><a href="/view/', escape_(post.url, True), u'">', escape_(post.title, True), u'</a></h3>\n'])
        extend_(['                ', u'    </li>\n'])
        extend_(['                ', u'    <li>\n'])
        extend_(['                ', u'        <h3 id="archiveTime">&nbsp; ', escape_(datestr(post.date), True), u'</h3>\n'])
        extend_(['                ', u'    </li>\n'])
        extend_(['                ', u'</ul>\n'])
    extend_([u'        </div>\n'])
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
    extend_([u'        <div class="container">\n'])
    extend_([u'        <h1>', escape_(post.title, True), u'</h1>\n'])
    extend_([u'        <h3>', escape_(datestr(post.date), True), u'</h3>\n'])
    extend_([u'        <hr>\n'])
    extend_([u'        ', escape_(post.content, False), u'\n'])
    extend_([u'        <br/>\n'])
    extend_([u'        <div id="links" class="links">\n'])
    extend_([u'            <ul class="list-inline">\n'])
    extend_([u'                <li><a href="/view/', escape_(post.url, True), u'">Link</a></li>\n'])
    extend_([u'                <li>\n'])
    extend_([u'                    Tags: &nbsp;\n'])
    for tag in loop.setup(post.tag):
        extend_(['                    ', u'<a href="/tag/', escape_(tag, True), u'">', escape_(tag, True), u'</a>\n'])
    extend_([u'                </li>\n'])
    extend_([u'            </ul>\n'])
    extend_([u'        </div>\n'])
    extend_([u'        </div>\n'])
    extend_([u'    </div>\n'])
    extend_([u'</div>\n'])
    extend_([u'<br/>\n'])
    extend_([u'<div id="commentSection">\n'])
    extend_([u'    <div class="container">\n'])
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
    extend_([u'</div>\n'])

    return self

view = CompiledTemplate(view, 'templates/view.html')
join_ = view._join; escape_ = view._escape

