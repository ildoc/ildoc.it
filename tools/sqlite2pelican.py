# -*- coding: utf-8 -*-
import sqlite3
import codecs
import os


class Post:
    def __init__(self, id, title, content, slug, status, pub_date, created, modified, filename):
        self.id = id
        self.title = title
        self.content = content
        self.slug = slug
        self.status = status
        self.pub_date = pub_date
        self.created = created
        self.modified = modified
        self.filename = filename


db = sqlite3.connect('blog.sqlite')
cursor = db.cursor()
cursor.execute('''select id, title, content, slug, status, pub_date, case when created > pub_date then pub_date else created end as created, modified, date(pub_date) || '-' || slug || '.md' as filename from blog_post''')
all_rows = cursor.fetchall()
blog_posts = []

for row in all_rows:
    blog_posts.append(Post(row[0], row[1], row[2],
                           row[3], row[4], row[5], row[6], row[7], row[8]))

for post in blog_posts:
    filename = './content/' + post.filename
    with codecs.open(filename, 'w', encoding='utf-8') as f:
        tag_cursor = db.cursor()
        tag_cursor.execute('''select t.title from blog_post p
            left join blog_post_tags pt on pt.post_id = p.id
            left join blog_tag t on t.id = pt.tag_id
            where p.id = ''' + str(post.id))
        all_tags = tag_cursor.fetchall()
        tags = []
        for tag in all_tags:
            if tag[0] is not None:
                tags.append(tag[0].lower())

        f.write('Title: ' + post.title.replace(r'\r', '') + '\n')
        f.write('Date: ' + post.created + '\n')
        f.write('Modified: ' + post.modified + '\n')
        if len(tags) > 0:
            f.write('Tags: ' + ', '.join(tags) + '\n')
        f.write('Slug: ' + post.slug + '\n')
        f.write('Author: Doc\n')
        if post.status == 2:
            f.write('Status: Draft\n')
        if post.status == 3:
            f.write('Status: Hidden\n')
        f.write('\n')
        f.write(post.content
                .replace(r'\r\n', '\n')
                .replace(r'\"', '"')
                .replace(r'\\', '\\')
                )

db.close()
