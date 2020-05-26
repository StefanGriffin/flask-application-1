from src import app


@app.route("/jobs/<job_id>/")
def jobs(job_id):
    return "<h1>Hello {job_id}</h1>".format(job_id=job_id)


