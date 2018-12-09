import urllib2
import json
from conf import KEY, BASE_URL
 

class CTA(object):
    '''Handles all Bus API'''
    def __init__(self):
        self.key = '?key=' + KEY

    def BuildURL(self,command, *args):
        url = BASE_URL + command + self.key
        if args:
            for arg in args:
                url += '&' + arg
        url += '&format=json'
        return url
    def makeRequest(self,url):
        req = urllib2.Request(url)
        opener = urllib2.build_opener()
        f = opener.open(req)
        return json.loads(f.read())
    
    def getRoutes(self):
        url = self.BuildURL('getroutes','rt=N55')
        return self.makeRequest(url)
    
    def getDirections(self,rt):
        url = self.BuildURL('getdirections','rt=' + rt)
        return self.makeRequest(url)
    
    def getStops(self,rt,direction):
        url = self.BuildURL('getstops','rt=' + rt,'dir=' + direction)
        return self.makeRequest(url)

    def getPredictions(self,rt,stpid,top):
        url = self.BuildURL('getpredictions','rt='+ rt,'stpid=' + stpid,'top=' + top)
        return self.makeRequest(url)



if __name__ == '__main__':
    busTime=CTA()
    resp = busTime.getPredictions('49','8417','10')
    print resp
    ''' for bus in resp[u'bustime-response'][u'prd']:
        print 'Route',bus[u'rt'], 'Towards' ,
        print bus[u'des'], 'will arive in',
        print bus[u'prdctdn'], 'minutes'
    '''
