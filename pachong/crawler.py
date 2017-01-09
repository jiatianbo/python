# coding: utf-8
import urllib2
import sys
import gzip
from StringIO import StringIO
reload(sys)
sys.setdefaultencoding('utf-8')
import httplib
httplib.HTTPConnection._http_vsn = 10
httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'

def urlopen(url):
	headers, url = makeRequestInfo(url)
	request = urllib2.Request(url = url, headers = headers)
	try:
		response = urllib2.urlopen(request)
		if 'Content-Encoding' in response.headers and response.headers['Content-Encoding'] == "gzip":
			buf = StringIO(response.read())
			f = gzip.GzipFile(fileobj=buf)
			data = f.read()
		else:
			data = response.read()
		response.close()
		return data
	except urllib2.HTTPError, e:
		print "The server couldn't fulfill the request"
    	print "Error code:", e.code
    	return e.code

def spaceConvert(url):
	return url.replace(' ', '%20')

def makeRequestInfo(url):
	headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
	url = spaceConvert(url)
	return headers, url
