from . import db

# Define database model
class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    complete = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"ToDo('{self.name}: {self.complete}')"