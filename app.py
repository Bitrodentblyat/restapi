from flask import Flask, jsonify, make_response, abort
from flask import request


app = Flask(__name__)


stud = [
    {
        'reg':1,
        'name': u'Rajesh',
        'year': u'2',
        'branch': u'Mechanical'
    },
    {
        'reg':2,
        'name': u'Maria',
        'year': u'2',
        'branch': u'Electrical'
    },
     {
        'reg':3,
        'name': u'Vignesh',
        'year': u'2',
        'branch': u'Mechanical'
    },
      {
        'reg':4,
        'name': u'Rachel',
        'year': u'2',
        'branch': u'Cs'
    },
       {
        'reg':5,
        'name': u'Aditya',
        'year': u'2',
        'branch': u'Mechanical'
    },
        {
        'reg':6,
        'name': u'Alex',
        'year': u'2',
        'branch': u'Mechanical'
    },
        {
        'reg':7,
        'name': u'Sameer',
        'year': u'2',
        'branch': u'Electronics'
    },
  {
        'reg':8,
        'name': u'Ankith',
        'year': u'2',
        'branch': u'Cs'
    }
]
@app.route('/stud/<int:reg_no>', methods=['GET'])
def get_stud(reg_no):
    student= [studs for studs in stud if studs['reg'] == reg_no]
    if len(student) == 0:
        abort(404)
    return jsonify({'stud': student[0]})
