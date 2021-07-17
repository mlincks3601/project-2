from .app import db


class cities(db.Model):
    __tablename__ = 'cities'

    
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    lat = db.Column(db.Float)
    long = db.Column(db.Float)
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<cities %r>' % (self.name)

class cities(db.Model):
    __tablename__ = 'tours'

    city_id = db.Column(db.Integer, foreign_key=True)
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    country = db.Column(db.String(60))
    year = db.Column(db.Integer)
    band = db.Column(db.String(100))
    

    def __repr__(self):
        return '<tours %r>' % (self.name)
