from market import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(60), nullable=False)
    budget = db.Column(db.Integer, nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    @property
    def prettier_budget(self):
        return f'R$ {self.budget / 100:,.2f}'

    def __repr__(self):
        return f'<User {self.username}>'

class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String(12), nullable=False, unique=True)
    description = db.Column(db.String(1024), nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Item {self.name}>'

