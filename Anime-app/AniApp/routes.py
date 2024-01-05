
from flask import render_template, Blueprint, current_app
from .scraper.mal_scraper import anime_data

main_bp = Blueprint('main', __name__)

@main_bp.route('/')

def index():
    base_url = current_app.config['BASE_URL']
    return render_template('index.html', anime_data=anime_data, base_url=base_url)
