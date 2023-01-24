import os
import random
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['secret_key']
secret = os.environ['key']

homework = []
projects = []


@app.route('/')
def home():
  return render_template('index.html', homework=homework, projects=projects)


@app.route('/create-homework/', methods=('GET', 'POST'))
def create():
  if request.method == 'POST':
    hw_id = random.randint(0, 500)
    hw = request.form['homework']
    due = request.form['due']
    key = request.form['key']

    if not hw:
      flash('homework is required!', 'error')
    elif not due:
      flash('due date is required!', 'error')
    elif key != secret:
      flash('correct key is required!', 'error')
    else:
      homework.append({'id': hw_id, 'title': hw, 'due': due})
      return redirect(url_for('home'))

  return render_template('create-homework.html')


@app.route('/del-homework/', methods=('GET', 'POST'))
def delete():
  if request.method == 'POST':
    key = request.form['key']
    hw_length = len(homework) - 1

    ids = request.form.getlist('checkbox')
    if key != secret:
      flash('correct key is required!')
    else:
      for x in ids:

        if hw_length == 0:
          hw_length += 1
        for i in range(hw_length):
          t_id = homework[i].get('id')

          if int(x) == t_id:
            homework.pop(i)
          i += 1

      return redirect(url_for('home'))

  return render_template('del-homework.html', homework=homework)


@app.route('/create-project/', methods=('GET', 'POST'))
def create_project():
  if request.method == 'POST':
    proj_id = random.randint(500, 1000)
    proj = request.form['proj_title']
    proj_due = request.form['proj_due']
    proj_key = request.form['proj_key']

    if not proj:
      flash('homework is required!', 'error')
    elif not proj_due:
      flash('due date is required!', 'error')
    elif proj_key != secret:
      flash('correct key is required!', 'error')
    else:
      projects.append({'id': proj_id, 'title': proj, 'due': proj_due})
      return redirect(url_for('home'))

  return render_template('create-project.html')


@app.route('/del-project/', methods=('GET', 'POST'))
def delete_project():
  if request.method == 'POST':
    proj_key = request.form['proj_key']
    proj_length = len(projects) - 1

    ids = request.form.getlist('checkbox')
    if proj_key != secret:
      flash('correct key is required!')
    else:
      for x in ids:

        if proj_length == 0:
          proj_length += 1
        for i in range(proj_length):
          t_id = projects[i].get('id')

          if int(x) == t_id:
            projects.pop(i)
          i += 1

      return redirect(url_for('home'))

  return render_template('del-project.html', projects=projects)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
