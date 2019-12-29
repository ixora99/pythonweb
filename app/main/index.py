from flaskimport Blueprint, request, render_template, flash, redirect, url_for
from flaskimport current_app as app


main= Blueprint('main', __name__, url_prefix='/')

@main.route('/main', methods=['GET'])
def index():
      return render_template('/main/index.html')
