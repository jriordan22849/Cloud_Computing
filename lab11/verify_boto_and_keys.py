import boto
import urllib2

response = urllib2.urlopen('https://github.com/paulfdoyle/cc-lab11-aws-sqs.git')

html = response.read().split(':')
accessID = html[0]
accessKEY = html[1]

print(accessID)
print(accessKEY)
print(boto.Version)
