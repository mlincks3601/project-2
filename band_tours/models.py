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
    __tablename__ = 'tour'
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer)
    city = db.Column(db.String(40))
    state = db.Column(db.String(40))
    country = db.Column(db.String(40))
    year = db.Column(db.Integer)
    band = db.Column(db.String(50))
    lat = db.Column(db.String(10))
    long = db.Column(db.String(10))
    

    def __repr__(self):
        return '<tours %r %d>' % (self.city, self.year)
