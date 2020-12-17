from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from forms import DepartmentForm, EmployeeAssignForm
from .. import db
from ..models import Department, Employee


def check_admin():    
    if not current_user.is_admin:
        abort()


@admin.route('/departments', methods=['GET', 'POST'])
@login_required
def list_departments():
    """
    Listar todos departamentos
    """
    check_admin()

    departments = Department.query.all()

    return render_template('admin/departments/departments.html',
                           departments=departments, title="Departamentos")


@admin.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    """
    Adicionar um departamento ao DB
    """
    check_admin()

    add_department = True

    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data,
                                description=form.description.data)
        try:
            db.session.add(department)
            db.session.commit()
            flash('Voce adicionou com sucesso um novo departamento.')
        except:
            flash('Erro: nome do departamento ja existe.')

        return redirect(url_for('admin.list_departments'))

    return render_template('admin/departments/department.html', action="Add",
                           add_department=add_department, form=form,
                           title="Adicionar Departamento")


@admin.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    """
    Editar um departamento
    """
    check_admin()

    add_department = False

    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        db.session.commit()
        flash('Voce editou com sucesso o departamento.')

        return redirect(url_for('admin.list_departments'))

    form.description.data = department.description
    form.name.data = department.name
    return render_template('admin/departments/department.html', action="Editar",
                           add_department=add_department, form=form,
                           department=department, title="Editar Departamento")


@admin.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    """
    Deletar um departamento do BD
    """
    check_admin()

    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('Voce deletou com sucesso o departamento.')

    return redirect(url_for('admin.list_departments'))

    return render_template(title="Deletar Departamento")


@admin.route('/employees')
@login_required
def list_employees():
    """
    Listar todos Funcionarios
    """
    check_admin()

    employees = Employee.query.all()
    return render_template('admin/employees/employees.html',
                           employees=employees, title='Funcionarios')


@admin.route('/employees/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_employee(id):
    """
    Atribuir um departamento para um funcionario
    """
    check_admin()

    employee = Employee.query.get_or_404(id)

    if employee.is_admin:
        abort()

    form = EmployeeAssignForm(obj=employee)
    if form.validate_on_submit():
        employee.department = form.department.data
        db.session.add(employee)
        db.session.commit()
        flash('O Funcionario foi atribuido com sucesso a um departamento')

        return redirect(url_for('admin.list_employees'))

    return render_template('admin/employees/employee.html',
                           employee=employee, form=form,
                           title='Atribuir um Funcionario')
