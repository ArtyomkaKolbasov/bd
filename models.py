from configuration import db


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    purpose = db.Column(db.String, nullable=False)
    pattern = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    material = db.Column(db.String, nullable=False)
    consump = db.Column(db.String, nullable=False)
    plan = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Model %r>' % self.id


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    pas = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id


class Support(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False, unique=True)
    pas = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Support %r>' % self.id


class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'))

    def __repr__(self):
        return '<Favorites %r>' % self.id


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String, nullable=False)

    user_username = db.Column(db.String, db.ForeignKey('user.username'))
    support_username = db.Column(db.String, db.ForeignKey('support.username'))

    def __repr__(self):
        return '<Message %r>' % self.id
