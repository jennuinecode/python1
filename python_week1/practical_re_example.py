import re, urllib #used to access stuff from web.

try:
    import urllib.request
except:
    pass

sites = 'google yahoo cnn msn'.split()
pattern = re.compile(r'<title>+.*</title>+', re.I|re.M)

for s in sites:
    print('Searching: ' + s)
    try:
        u = urllib.urlopen('http://' + s + '.com')
    except:
        False
    text = u.read()
    title = re.findall(pattern, str(text))
    print (title)
