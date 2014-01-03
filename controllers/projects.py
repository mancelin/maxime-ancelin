# -*- coding: utf-8 -*-


from flask import Flask, render_template
import json
import pymongo


def list(db):
    projects_cursor = db.projects.find()
    return render_template('projects.html', projects=projects_cursor, title=' - Projets');

def admin(db):
    projects_cursor = db.projects.find()
    return render_template('admin/projects/list.html', projects=projects_cursor, title='[ADMIN] - Projets');

def create(db, method):
    print method
    tags = db.projects.distinct('tags')
    return render_template('admin/projects/create.html', tags=tags, title='[ADMIN] - Nouveau Projet');

#def edit()


#def delete()

# return json with distinc tags sorted
def tags(db):
    tags = db.projects.distinct('tags')
    tags.sort()
    return json.dumps(tags, encoding='utf-8', ensure_ascii=False, indent=2)
