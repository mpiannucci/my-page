# Map out the urls to the view controllers
urls = (
    '/', 'Index',
    '/blog/(\d+)', 'Blog',
    '/blog', 'Blog',
    '/view/(.+)', 'View',
    '/new', 'New',
    '/delete/(.+)', 'Delete',
    '/edit/(.+)', 'Edit',
    '/admin', 'Admin',
    '/apps', 'Apps',
    '/github', 'Github',
    '/bio', 'Bio',
    '/logout', 'Logout',
    '/resume', 'Resume',
    '/archive', 'Archive',
    '/tag/(.+)', 'Tagged',
    '/hackwinds', 'HackWinds',
    '/hackwinds_login', 'HackWindsLogin',
    '/hackwinds_create', 'HackWindsCreate'
)