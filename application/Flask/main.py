from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import cv2
import tensorflow as tf
from PIL import Image
import numpy as np



app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'


model = tf.keras.models.load_model("c:/Users/Vikhas/Downloads/unsus_keras.pb")

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")


def process_video(file):
    frameNr = 0
    capture = cv2.VideoCapture(file)
    while (True):
        success, frame = capture.read()
        if success:
            cv2.imwrite(f'static/files/frames/frame_{frameNr}.jpg', frame)
        else:
            break
        frameNr = frameNr+1
    capture.release()

def predict_frames(frame_path):
    classes = {'accident':0,
           'animal_cruelty':0,
           'crowding':0,
           'explosion':0,
           'fight':0,
           'weapon_usage':0 }
    lst = ['weapon_usage',
           'animal_cruelty',
           'crowding',
           'explosion',
           'fight',
           'accident']
    image_files=os.listdir(frame_path)
    image_path=[]
    for i in range(len(image_files)):
        p=frame_path+"/"+image_files[i]
        image_path.append(p)
    
    for i in range(0,len(image_path),10):
        # Load the input image
        image = Image.open(image_path[i])
        # Resize the image to 256x256
        image = image.resize((256, 256))
        # Convert the image to a numpy array and add a batch dimension
        image = np.array(image)
        image = np.expand_dims(image, axis=0) 
        pre=model.predict(image)
        classes[lst[np.argmax(pre[0])]]+=1
    Keymax = max(zip(classes.values(), classes.keys()))[1]
    print(Keymax)
    return Keymax



@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        video_path="static/files/"+ file.filename
        process_video(video_path) #newly added
        frame_path="static/files/frames"
        pr = "Prediction Result: "+predict_frames(frame_path)
        return pr
    return render_template('index.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)