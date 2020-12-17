from flask import abort, render_template
from flask_login import current_user, login_required

from . import home


@home.route('/')
def homepage():
    """
    Renderiza o template da homepage na rota / 
    """
    return render_template('home/index.html', title="Welcome")


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Renderiza o template do dashboard na rota /dashboard
    """
    return render_template('home/dashboard.html', title="Dashboard")


@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    
    if not current_user.is_admin:
        abort()

    return render_template('home/admin_dashboard.html', title="Dashboard")
