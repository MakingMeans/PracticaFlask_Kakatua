from flask import render_template, request
from decimal import Decimal
from models import Registro, db


def register_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        result = None
        if request.method == 'POST':
            n1 = Decimal(request.form['num1'])
            n2 = Decimal(request.form['num2'])
            op = request.form['operation']

            if op == 'add':
                result = n1 + n2
            elif op == 'subtract':
                result = n1 - n2
            elif op == 'multiply':
                result = n1 * n2
            elif op == 'divide':
                result = n1 / n2 if n2 != 0 else None

            # Guardar en tabla de auditoría
            registro = Registro(num1=n1, num2=n2, operacion=op)
            db.session.add(registro)
            db.session.commit()

        return render_template('index.html', result=result)

    @app.route('/registers')
    def show_registers():
        registros = Registro.query.order_by(Registro.timestamp.desc()).all()
        return render_template('registers.html', registros=registros)
