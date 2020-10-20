from flask import Flask, render_template
import requests
import subprocess

app = Flask(__name__)


@app.route('/')
def root():
    name = "Hello World"
    return render_template('root.html', title='Home')


@app.route('/volume/vol_up')
def vol_up():
    subprocess.Popen('SetVol.exe +10', shell=True)
    return render_template('success.html', title='vol_up Success')


@app.route('/volume/vol_down')
def vol_down():
    subprocess.Popen('SetVol.exe -10', shell=True)
    return render_template('success.html', title='vol_down Success')


@app.route('/volume/vol_mute')
def vol_mute():
    subprocess.Popen('SetVol.exe mute', shell=True)
    return render_template('success.html', title='vol_mute Success')


@app.route('/volume/vol_unmute')
def vol_unmute():
    subprocess.Popen('SetVol.exe unmute', shell=True)
    return render_template('success.html', title='vol_unmuteSuccess')


if __name__ == "__main__":
    app.run()
