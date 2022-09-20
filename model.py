from flask import Flask, send_file, render_template
app = Flask(__name__)
 
@app.route('/')
def upload_form():
	return render_template('index.html')

@app.route('/download')
def download_file():

	path = "STUDENTS-LIST.pdf"

	return send_file(path, as_attachment=True)

if __name__ == '__main__':  
   app.run(host='0.0.0.0',port=8080,debug = False)  