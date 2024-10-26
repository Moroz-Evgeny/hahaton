import requests
from flask import Blueprint, render_template, session, flash, redirect, url_for, request


prof = Blueprint('prof', __name__)
@prof.route('/profile')
def profile():
  return render_template('profile.html')