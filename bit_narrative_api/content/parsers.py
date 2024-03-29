import urllib2
import json
import re


readability_api_token = '04aa48d7c5552b8a45c3f87db1d61274f1242241'


def parse_content(url, version='v1'):
    '''
    Parse URL to extract relevent content information

    Reference:
        https://www.readability.com/developers/api/parser

    Returns:
        {
            'domain',
            'title',
            'date_published',
            'author',
            'excerpt',
            'content',
            'word_count',
            'lead_image_url',
            'url'
        }
    '''
    url = url.replace("#", "%23")
    endpoint = 'http://readability.com/api/content/' \
        + version + '/parser?url=' \
        + url + '&token=' + readability_api_token
    try:
        req = urllib2.urlopen(endpoint)
        res = json.loads(req.read())
    except Exception:
        print "[EXCEPTION]:\tParser Error"
        res = None
    return res


def strip_tags(s):
    """
    removes all < * > </ * > tags
    """
    return re.sub("<.*?>", " ", s)


def parse_bits(s):
    """
    breaks a text into bits
    """
    return re.split("\. ", s)
