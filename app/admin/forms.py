from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from ..models import Department


class DepartmentForm(FlaskForm):
    """
    Formato para o admin adicionar ou editar departamentos
    """
    nome = StringField('Nome', validators=[DataRequired()])
    codigo = StringField('Codigo', validators=[DataRequired()])
    submeter = SubmitField('Submeter')

class EmployeeAssignForm(FlaskForm):
    """
    Formato para o admin Atribuir departamento para os funcionarios
    """
    department = QuerySelectField(query_factory=lambda: Department.query.all(),
                                  get_label="nome")
    submit = SubmitField('Submit')
