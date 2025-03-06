import os

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from process_miner import process_miner

UPLOAD_FOLDER = os.path.join('..', 'frontend', 'uploads')
ALLOWED_EXTENSIONS = {'xes'}

# Flask configurations
app = Flask(__name__, template_folder='../frontend/web', static_folder='../frontend/web/static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'f3cfe9ed8fae309f02079dbf'


@app.route("/")
@app.route("/index.html")
def homepage():
    return render_template('index.html')


@app.route("/explanation.html")
def explanation():
    return render_template('explanation.html')


@app.route("/info.html")
def info():
    return render_template('info.html')


def allowed_file(filename):
    """ Function checking file extension
        Input: filename
        Output: Boolean"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/process_discovery_upload.html", methods=['GET', 'POST'])
def process_discovery_upload():
    """ Function defining the landing page
        Input:  Possible POST variables [File and name of algorithm ]
        Logic:  1. Checks if POST variables are includet
                    YES:    1. Uploads file to webserver
                            2. Calls the process miner function
                            3. Outputs Display page
                    NO:  Outputs upload page again
        Output: Upload/Display page Depending on POST variables """

    # Check if POST variables are preset
    if request.method == 'POST':
        # check if a pre uploaded file is being used
        if 'pre-def-file' in request.form:
            algorithm = request.form["algorithm"]
            filename = request.form['pre-def-file']

            # Call the process_miner function to generate the Petri net
            print_steps = process_miner("datasets/" + filename, algorithm)

            # Pass the Petri net to the render_template function
            return render_template('process_discovery_display.html', filename=filename, algorithm=algorithm,
                                   print_steps=print_steps)

        # check if the post request includes a file
        if 'file' not in request.files:
            return render_template('process_discovery_upload.html')
        file = request.files['file']

        # If the user does not select a file, the browser submits an empty file without a filename.
        if file.filename == '':
            render_template('process_discovery_upload.html')

        # upload the file and redirect towards the process discovery page
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(os.path.dirname(__file__), os.pardir, 'frontend', 'uploads', filename))
            algorithm = request.form["algorithm"]

            # Call the process_miner function to generate the Petri net
            print_steps = process_miner(filename, algorithm)

            # Pass the Petri net to the render_template function
            return render_template('process_discovery_display.html', filename=filename, algorithm=algorithm,
                                   print_steps=print_steps)

    return render_template('process_discovery_upload.html')


if __name__ == "__main__":
    app.run(host="::1", port=9005)
