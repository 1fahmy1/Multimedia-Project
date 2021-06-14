from flask import Flask, request, send_from_directory, jsonify, redirect , url_for
from search import searchVideo
# set the "static" directory as the static folder.
# this will ensure that all the static files are under one folder
app = Flask(__name__, static_url_path='/static')

# serving some static html files
@app.route('/data/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  print(path)
  return app.send_static_file(path)


@app.route('/upload', methods=['POST'])
def upload_file():
    # checking if the file is present or not.
    if 'file' not in request.files:
        return "No file found"
    file = request.files['file']
    print (file.filename)
    file.save("uploadedFiles/"+file.filename)
    # TODO: call cbvr function this is written for response files
    response_filenames = searchVideo(file.filename)
    #
    # print (response_filenames)
    # response_filenames = ['data/CAR/car (21).avi', 'data/CAR/car (21).avi', 'data/CAR/car (14).avi', 'data/CAR/car (13).avi', 'data/WALK/Movie_0042.avi', 'data/CAR/car (13).avi', 'data/WALK/Movie_0042.avi', 'data/MISC/Movie_0025 (2).avi', 'data/CAR/car (11).avi', 'data/CAR/car (18).avi', 'data/CAR/car (7).avi', 'data/CAR/car (7).avi']

    return jsonify(response_filenames)
    # return redirect('result_video')
    # return "file uploaded"
    # [/Geek/Desktop/CBVR/1/CBVR-master/data/BIKE/cycle1.avi, /Geek/Desktop/CBVR/1/CBVR-master/data/BIKE/cycle1.avi]


@app.route('/result')
def result_video():
    return '<h1> results are here </h1>'



if __name__ == "__main__":
    app.run(port=3333)
