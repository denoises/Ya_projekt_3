from flask import Flask, render_template
import json

app = Flask(__name__)

with open('car/cars.json') as json_file:
    all = json.load(json_file)


@app.route('/')
@app.route('/BMW')
def bmw():
    name = 'BMW'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Volkswagen')
def volkswagen():
    name = 'Volkswagen'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Mercedes-Benz')
def mercedes_benz():
    name = 'Mercedes-Benz'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Renault')
def renault():
    name = 'Renault'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Audi')
def audi():
    name = 'Audi'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Chery')
def chery():
    name = 'Chery'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Chevrolet')
def chevrolet():
    name = 'Chevrolet'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Ford')
def ford():
    name = 'Ford'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Citroen')
def citroen():
    name = 'Citroen'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Fiat')
def fiat():
    name = 'Fiat'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Lada')
def lada():
    name = 'Lada'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Honda')
def honda():
    name = 'Honda'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Geely')
def geely():
    name = 'Geely'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Haval')
def haval():
    name = 'Haval'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Lexus')
def lexus():
    name = 'Lexus'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Jeep')
def jeep():
    name = 'Jeep'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Infiniti')
def infiniti():
    name = 'Infiniti'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Hyundai')
def hyundai():
    name = 'Hyundai'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Toyota')
def toyota():
    name = 'Toyota'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Uaz')
def uaz():
    name = 'UAZ'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Suzuki')
def suzuki():
    name = 'Suzuki'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Skoda')
def skoda():
    name = 'Skoda'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Lifan')
def lifan():
    name = 'Lifan'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/LandRover')
def landrover():
    name = 'Land Rover'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Mitsubishi')
def mitsubishi():
    name = 'Mitsubishi'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Porsche')
def porsche():
    name = 'Porsche'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Seat')
def seat():
    name = 'SEAT'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Opel')
def opel():
    name = 'Opel'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Nissan')
def nissan():
    name = 'Nissan'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Volvo')
def volvo():
    name = 'Volvo'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Peugeot')
def peugeot():
    name = 'Peugeot'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Jaguar')
def jaguar():
    name = 'Jaguar'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Kia')
def kia():
    name = 'Kia'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Mazda')
def mazda():
    name = 'Mazda'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


@app.route('/Subaru')
def subaru():
    name = 'Subaru'
    return render_template('base.html', title=name, model_src=all[f'{name}']['model'],
                           inf=all[f'{name}']['description'])


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
