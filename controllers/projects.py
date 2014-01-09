# -*- coding: utf-8 -*-


from bson.objectid import ObjectId
from flask import Flask, redirect, render_template
import json
import pymongo
from slugify import slugify


def admin(db, request):
    if request.method == 'POST':
        remove_selected(db, request.form.values())
    projects_cursor = db.projects.find()
    return render_template('admin/projects/list.html', projects=projects_cursor, title='[ADMIN] - Projets');

def create_or_edit(db, request, slug=None):
    data = error = inputs = None
    form = request.form
    if slug:
        project = db.projects.find_one({'slug': slug})
        if project is None:
            error = "Invalid slug."
            return render_template('admin/projects/error.html', error=error);
    else:
        project = {}
    if request.method == 'GET':
        return render_template('admin/projects/create.html', error=None, project=project);
    if request.method == 'POST':
        if form['btn'] == u'save':
            inputs = {
                key: form.get(key)
                for key in [
                    'btn', 'date', 'description', 'name', 'readme', 'run_url', 'source_url', 'tags'
                ]
            }
            project = inputs.copy()
            project['slug'] = slugify(project['name'])
            project['tags'] = project['tags'].split(',')
            if project['slug'] == '':
                error = "Name required.".format(slug)
            elif project['slug'] == slug:
                project['_id'] = db.projects.find_one({'slug': project['slug']})['_id']
                db.projects.save(project, safe=True)
                return redirect("/ADMIN")
            elif db.projects.find_one({'slug': project['slug']}):
                error = u'A projet with the same name already exist.'
            if error is not None:
                return render_template('admin/projects/create.html', error=error, project=project);
            else:
                db.projects.insert(project)
                return redirect("/ADMIN")
        elif form['btn'] == u'remove':
            remove(db, slug)
            return redirect("/ADMIN")
        print "TAGS\n"
        pprint(form['tags'])


# remove project from form
def remove(db, slug):
    db.projects.remove({'slug': slug})

# remove selected projects (checkbox)
def remove_selected(db, id_list):
    for id in id_list:
        if(id != 'toogle_select_all'):
            db.projects.remove(ObjectId(id))

# return json with distinc tags sorted
def tags(db):
    tags = db.projects.distinct('tags')
    tags.sort()
    return json.dumps(tags, encoding='utf-8', ensure_ascii=False, indent=2)
