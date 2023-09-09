from flask import Flask
from utils import load_candidates

app = Flask(__name__)

candidates = load_candidates()

@app.route('/')
def page_index():
    str_candidates = f'<pre>\n'
    for candidate in candidates.values():
        str_candidates += f"{candidate['name']}\n{candidate['position']}\n{candidate['skills']}\n\n\n"
    str_candidates += f'</pre>\n'
    return str_candidates


@app.route('/candidates/<int:id>/')
def profile(id):
    candidate = candidates[id]

    str_candidates = f"<img src={candidate['picture']}></img> <br><br>{candidate['name']} <br>{candidate['position']} <br>{candidate['skills']} <br><br>"

    return str_candidates



@app.route('/skills/<skill>/')
def skills(skill):
    str_candidates = '<pre>'
    for candidate in candidates.values():
        candidate_skills = candidate['skills'].split(', ')
        candidate_skills = [x.lower() for x in candidate_skills]
        print(candidate_skills)
        if skill in candidate_skills:
            str_candidates += f"{candidate['name']} \n{candidate['position']} \n{candidate['skills']} \n\n"
    str_candidates += f'</pre>\n'

    return str_candidates

#app.add_url_rule('/index/', view_funk=page_index)


app.run(debug = True)

