from flask import Flask, render_template
from flask import Flask, request, render_template
from syn_atno import get_meaning,get_synonyms,get_sentence

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

      return render_template('index.html')
@app.route('/search',methods=['GET','POST'])
def search():
    if request.method =='POST':
        try:
            name = str(request.form.get('search_element'))
            m = get_meaning(name)
            s = get_synonyms(name)
            sent=get_sentence(name)
            return render_template('show.html',name=name,meaning=m,syno=s,sentence=sent)
        except:
            name = request.form.get('search_element')
            return render_template('show.html',name=name,meaning=m,syno=s,sentence='none')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('page_error.html'), 404
if __name__ == "__main__":
        app.run(debug=True)
