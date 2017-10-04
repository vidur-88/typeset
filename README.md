Overview
========

This is APIs for creating a blogs.
It supports comments on paragraphs. Not comments on the blog, but on a specific paragraph.
There are 3 tables for storing blogs that are blog, paragraph, comment.

Blog:

| id | title |
| -- | ----- |

Paragraph:

| id | text | priority | blog_id |
| -- | ---- | -------- | ------- |

Comment:

| id | text | paragraph_id |
| -- | ---- | ------------ |

You can check schema in blogs/migrations/0001_initial.py


The following are general instructions for running the this project locally.

Python Environment
------------------
Your python environment should be set up with at least:

+   **Python 2.6.5 or greater, but not Py3k**

    http://www.python.org/

+   **pip 1.0.2 or greater (comes with setuptools 0.6c11)**

    http://pypi.python.org/pypi/pip  

+   **virtualenv 1.6.4 or greater**

    http://www.virtualenv.org/en/latest/index.html

Please use [PIP](http://pypi.python.org/pypi/pip) to manage your python environment. Most environments come with easy\_install pre-installed. You can use easy\_install to install pip.

Run
---

  `python manage.py makemigration`

  `python manage.py migrate`
  
  `python manage.py runserver 0.0.0.0:8000`

Hit http://localhost:8000 in your browser

APIs
----
Example:

+   **Blogs list**

    /blogs/all (GET call)

    response: `{"data": ["list of all blogs"]}`

+   **Particular Blog**

    /blogs/get_blog?blog_id=2 (GET call)

    response: `{"paragraph_id": "paragraph_text"}`

+   **All comments for a blog**

    /blogs/blog_comments?blog_id=2 (GET call)

    response: `{"paragraph_id": ["list of comments"]}`

+   **Create a new blog**

    /blogs/create_blog (POST call)

    params: `{'title': 'xxxxxxx', 'texts': 'xxxxxxxxxxxxxxxxxxxxx'}`

    response: `{"blog_id": xxx, "paragraph": {paragraph_id_: {"priority": xxx, "text": "xxxxxx"}}}`

+   **Add paragraph**

    /blogs/add_blog_paragraph (POST Call)

    params: `{"blog_id": xxx, "prev_priority": xxx, "next_priority": xxxx, "text": "xxxxx"}`

    response: `{paragraph_id: {"priority": xxx, "text": "xxxxxxxxx"}}`

+   **Paragraph updation for a blog**

    /blogs/update_blog_paragraph (POST call)

    params: `{"paragraph_id": xxxx, "text": "xxxxxxx"}`

    response: `{paragraph_id: "xxxxxxxxxxxxx"}`

+   **Add comment for a paragraph**

    /blogs/add_comment (POST call)

    params: `{"paragraph_id": xxx, "text": "xxxxxxxxxx"}`

    response: `{"text": "xxxxxxxxxx", "comment_id": xxx}`

+   **Update comment**

    /blogs/update_blog_paragraph (POST call)

    params: `{"paragraph_id": xxx, "text": "xxxxxxxxxxxxx"}`

    response: `{"text": "xxxxxxxxxxxxx", "comment_id": xxx}`
