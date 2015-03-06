def condense(post):
    fb_link = post['actions'][0]['link']
    yield {
        'message': post['message'],
        'facebook-link': link,
        'external-link': post.get('link')
    }
    for comment in post.get('comments', {}).get('data', []):
        yield {
            'message': comment['message'],
            'facebook-link': link,
            'external-link': None,
        }
