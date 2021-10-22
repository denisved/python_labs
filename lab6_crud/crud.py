from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String, unique=True)
    wheel_formula = db.Column(db.String, unique=True)
    mileage = db.Column(db.Float, unique=True)
    fuel_consumption_per_hour = db.Column(db.Float, unique=True)

    def __init__(self, model, wheel_formula, mileage, fuel_consumption_per_hour):
        self.model = model
        self.wheel_formula = wheel_formula
        self.mileage = mileage
        self.fuel_consumption_per_hour = fuel_consumption_per_hour


class MachineSchema(ma.Schema):
    class Meta:
        fields = ('model', 'wheel_formula', 'mileage', 'fuel_consumption_per_hour')


machine_schema = MachineSchema()
machines_schema = MachineSchema(many=True)


@app.route("/machine", methods=["POST"])
def add_machine():
    data = MachineSchema().load(request.json)
    new_machine = Machine(**data)

    db.session.add(new_machine)
    db.session.commit()

    return machine_schema.jsonify(new_machine)


@app.route("/machine", methods=["GET"])
def get_machines():
    all_machines = Machine.query.all()
    result = machines_schema.dump(all_machines)
    return jsonify(result)


@app.route("/machine/<id>", methods=["GET"])
def get_machine(id):
    machine = Machine.query.get(id)

    if machine is None:
        abort(404)

    return machine_schema.jsonify(machine)


@app.route("/machine/<id>", methods=["PUT"])
def machine_update(id):
    machine = Machine.query.get(id)

    if machine is None:
        abort(404)

    model = request.json['model']
    wheel_formula = request.json['wheel_formula']
    mileage = request.json['mileage']
    fuel_consumption_per_hour = request.json['fuel_consumption_per_hour']

    machine.model = model
    machine.wheel_formula = wheel_formula
    machine.mileage = mileage
    machine.fuel_consumption_per_hour = fuel_consumption_per_hour

    db.session.commit()
    return machine_schema.jsonify(machine)


@app.route("/machine/<id>", methods=["DELETE"])
def machine_delete(id):
    machine = Machine.query.get(id)

    if machine is None:
        abort(404)

    db.session.delete(machine)
    db.session.commit()

    return machine_schema.jsonify(machine)


if __name__ == '__main__':
    app.run(debug=True)