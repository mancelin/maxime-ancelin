# -*- coding: utf-8 -*-


from flask import Flask, render_template
import pymongo


def list(db):
    projects_cursor = db.projects.find()
    return render_template('projects.html', projects=projects_cursor, title=' - Projets');

def admin(db):
    projects_cursor = db.projects.find()
    return render_template('admin/projects/list.html', projects=projects_cursor, title='[ADMIN] - Projets');

#def edit()

#def add()

#def delete()
