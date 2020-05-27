from flask import jsonify
from src import app

# json 
@app.route("/jobs/")
def jobs_api():
    data = {'job_id': 123, 'task': [123, 45, 545]}
    return jsonify(data)

@app.route("/jobs/<job_id>/")
def jobs(job_id):
    return "<h1>Hello {job_id}</h1>".format(job_id=job_id)


