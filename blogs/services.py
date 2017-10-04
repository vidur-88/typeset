from blogs.models import Paragraph, Blog, Comment


PRIORITY = 10000


def get_all_blogs():
    blogs = Blog.objects.all()
    resp = list()

    for blog in blogs:
        resp.append({'title': blog.title, 'id': blog.id})
    return resp


def add_blog(params):
    try:
        title = params['title']
        texts = params.get('texts')
    except Exception:
        raise Exception('Bad Input')

    resp = dict()
    blog = Blog.objects.create(title=title)
    resp['blog_id'] = blog.id
    if texts:
        resp['paragraph'] = add_paragraph(texts, blog)
    return resp


def add_paragraph(texts, blog):
    texts = texts.split('\n\n\n')

    resp = dict()
    for ind, text in enumerate(texts):
        p = Paragraph.objects.create(text=text, priority=PRIORITY*ind, blog=blog)
        resp[p.id] = {'text': p.text, 'priority': p.priority}
    return resp


def get_blog(params):
    try:
        blog_id = int(params['blog_id'])
    except Exception:
        raise Exception('Bad Input')

    resp = dict()
    paragraphs = Paragraph.objects.filter(blog__id=blog_id)
    for paragraph in paragraphs:
        resp[paragraph.id] = paragraph.text
    return resp


def add_blog_paragraph(params):
    try:
        blog_id = params['blog_id']
        text = params['text']
        prev_priority = params.get('prev_priority')
        next_priority = params.get('next_priority')
    except Exception:
        raise Exception('Bad Input')

    resp = dict()
    if not prev_priority and prev_priority != 0:
        priority = next_priority / PRIORITY / 2
    elif not next_priority or prev_priority == 0:
        priority = prev_priority + PRIORITY
    else:
        priority = (prev_priority + next_priority) / 2
    blog = Blog.objects.filter(id=blog_id).first()
    paragraph = Paragraph.objects.create(text=text, priority=priority,
                                 blog=blog)
    resp[paragraph.id] = {'text': paragraph.text,
                          'priority': paragraph.priority}
    return resp


def update_blog_paragraph(params):
    try:
        paragraph_id = params['paragraph_id']
        text = params['text']
    except Exception:
        raise Exception('Bad Input')

    resp = dict()
    paragraph = Paragraph.objects.filter(id=paragraph_id).update(text=text)
    resp[paragraph_id] = text
    return resp


def add_comment(params):
    try:
        paragraph_id = params['paragraph_id']
        text = params['text']
    except Exception:
        raise Exception('Bad Input')

    paragraph = Paragraph.objects.filter(id=paragraph_id).first()
    comment = Comment.objects.create(text=text, paragraph=paragraph)
    return {'comment_id': comment.id, 'text': comment.text}


def update_comment(params):
    try:
        comment_id = params['comment_id']
        text = params['text']
    except Exception:
        raise Exception('Bad Input')

    comment = Comment.objects.filter(id=comment_id).update(text=text)
    return {'comment_id': comment_id, 'text': text}


def get_blog_comment(params):
    try:
        blog_id = params['blog_id']
    except Exception:
        raise Exception('bad Input')

    comments = Comment.objects.filter(paragraph__blog__id=blog_id)
    resp = dict()

    for comment in comments:
        if comment.paragraph.id in resp:
            resp[comment.paragraph.id].append(comment.text)
        else:
            resp[comment.paragraph.id] = [comment.text]
    return resp
