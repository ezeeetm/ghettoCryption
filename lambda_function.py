#!/usr/bin/env python
import requests

def HexMeBro(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '%')
        if len(hv) == 1:
            hv = '0'+hv
        if hv == '%a':
            continue
        lst.append(hv)

    return reduce(lambda x,y:x+y, lst)

def lambda_handler ( event, context ):
    domain = event['domain']
    url = "http://www.%s.com" % ( domain )
    resp = requests.get( url )
    content = resp.content
    hexContent = HexMeBro ( content )
    resp = """<Script Language=\'Javascript\'>
    <!--
    document.write(unescape(\'%s\'));
    //-->
    </Script>""" % (hexContent)
    return resp

'''
in API Gateway
request mapping:
{
    "url": "$input.params('url')"
}

response mapping (leave as application/json):
#set($inputRoot = $input.path('$'))
$inputRoot
'''
