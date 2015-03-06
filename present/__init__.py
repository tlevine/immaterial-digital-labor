import re, csv, sys

def main():
    sys.stdout.write('<table>\n')
    sys.stdout.write(HEAD)
    for datum in csv.DictReader(sys.stdin):
        datum['external-links'] = find_links(datum['message'])
        for tr in format_links(datum):
            sys.stdout.write(tr)
    sys.stdout.write('</table>\n')

def find_links(datum):
    links = re.findall('https?://[^ ]+', datum['message'])
    if datum['external-link'] and datum['external-link'] not in links:
        links.append(datum['external-link'])
    return links

HEAD = '''
<tr>
  <th>Link</th>
  <th>Posted by</th>
  <th>Original post</th>
</tr>
'''
BODY = '''
<tr>
  <td><a href="%(external-link)s">%(external-link)s</a></td>
  <td><a href="https://facebook.com/%(from-id)s">%(from-name)s</a></td>
  <td><a href="%(facebook-link)s">%(facebook-link-post-id)s</a></td>
</tr>
'''

def format_body(datum):
    args = dict(datum)
    args['facebook-link-post-id'] = facebook-link.split('/')[-1]
    for external_link in datum['external_links']:
        args['external-link'] = external_link
        yield BODY % datum
