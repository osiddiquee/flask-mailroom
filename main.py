import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/add_donation/')
def add():
    if request.method == 'POST':
        # if request.form['donor'] in Donor.select(Donor.name):
        #
        # else:
        donation = Donation(value = request.form['donation'],
                            donor = request.form['donor'])
        donation.save()

        return redirect(url_for('all'))
    else:
        return render_template('add_donation.jinja2')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
