from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

PATH = 'candidates.json'
candidates = load_candidates_from_json(PATH)

app = Flask(__name__)

@app.route('/')
def get_all_users():
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:x>')
def get_one_person(x):
    item = get_candidate(x, candidates)
    if item:
        return render_template('person.html', item=item)
    return "NOT FOUND"

@app.route('/search/<candidate_name>')
def get_user_by_name(candidate_name):
    persons = get_candidates_by_name(candidate_name, candidates)
    if persons:
        return render_template('search.html', candidates=persons)
    return "NOT FOUND"

@app.route('/skill/<skill_name>')
def get_skill_name(skill_name):
    items = get_candidates_by_skill(skill_name, candidates)
    if items:
        return render_template('skills.html', skill=skill_name, candidates=items)
    return "NOT FOUND"

app.run()
