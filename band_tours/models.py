from .app import db


class Cities(db.Model):
    __tablename__ = 'cities'

    
    city = db.Column(db.String(40))
    state = db.Column(db.String(40))
    lat = db.Column(db.String(10))
    long = db.Column(db.String(10))
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<cities %r>' % (self.name)

class Tours(db.Model):
    __tablename__ = 'tours'

    city_id = db.Column(db.Integer, foreign_key=True)
    city = db.Column(db.String(40))
    state = db.Column(db.String(40))
    country = db.Column(db.String(40))
    year = db.Column(db.Integer)
    band = db.Column(db.String(50))
    

    def __repr__(self):
        return '<tours %r>' % (self.name)
