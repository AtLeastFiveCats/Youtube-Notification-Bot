import xml.etree.ElementTree as ET
'''
a function for testing from a local file
def xml_parse():
    tree = ET.parse('testxml.xml')
    root = tree.getroot()
    return root
'''

testxml = '''
<feed xmlns:yt="http://www.youtube.com/xml/schemas/2015"
         xmlns="http://www.w3.org/2005/Atom">
  <link rel="hub" href="https://pubsubhubbub.appspot.com"/>
  <link rel="self" href="https://www.youtube.com/xml/feeds/videos.xml?channel_id=CHANNEL_ID"/>
  <title>YouTube video feed</title>
  <updated>2015-04-01T19:05:24.552394234+00:00</updated>
  <entry>
    <id>yt:video:VIDEO_ID</id>
    <yt:videoId>VIDEO_ID</yt:videoId>
    <yt:channelId>CHANNEL_ID</yt:channelId>
    <title>Video title</title>
    <link rel="alternate" href="http://www.youtube.com/watch?v=VIDEO_ID"/>
    <author>
     <name>Channel title</name>
     <uri>http://www.youtube.com/channel/CHANNEL_ID</uri>
    </author>
    <published>2015-03-06T21:40:57+00:00</published>
    <updated>2015-03-09T19:05:24.552394234+00:00</updated>
  </entry>
</feed>

'''

#This function should accept an xml formatted document and return the video title, channel, and url

def xml_parser(testxml):
    xml_content = ET.fromstring(testxml)
    for entry in xml_content.iter():
        print(entry)

xml_parser(testxml)

