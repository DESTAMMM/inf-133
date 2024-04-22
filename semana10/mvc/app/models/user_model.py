from database import db

class User(db.Model):
    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.String(50), nullable=False)
    
    def __init__(self, first_name, last_name, email, password, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.birth_date = birth_date

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()
    
