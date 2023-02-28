from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data analyst',
    'location': 'Nairobi, Kenya',
    'salary': 'KES 120000'
  },
  {
    'id': 2,
    'title': 'Data scientist',
    'location': 'Mombasa, Kenya',
    'salary': 'KES 125000'
  },
  {
    'id': 3,
    'title': 'Architectural Engineer',
    'location': 'Kisumu, Kenya',
    'salary': 'KES 180000'
  },
  {
    'id': 4,
    'title': 'Front End Engineer',
    'location': 'Remote',
    'salary': 'KES 80,000'
  },
]


@app.route("/")
def hello_jovian():
  return render_template("home.html", jobs=JOBS, company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run('0.0.0.0', debug=True)
