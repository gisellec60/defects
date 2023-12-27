from sqlalchemy.ext.hybrid import hybrid_property
from config import db, bcrypt

class Defect(db.Model):
    __tablenanme__ = "defects"

    __table_args__ = (
        db.CheckConstraint('length(desc) >= 30'),
    )

    id = db.Column(db.Integer, primary_key=True)
    defectId = db.Column(db.Integer, nullable=False)
    open_date = db.Column(db.Date, nullable=False)
    close_date = db.Column(db.Date, nullable=False)
    username = db.Column(db.String)
    email = db.Column(db.String,nullable=False, unique=True)
    os = db.Column(db.String)
    os_version = db.Column(db.String)
    application = db.Column(db.String)
    app_version = db.Column(db.String)
    host = db.Column(db.String)
    browser = db.Column(db.String)
    browser_version = db.Column(db.String)
    desc = db.Column(db.String,nullable=False)
    comments = db.Column(db.String)
    status = db.Column(db.Boolean, nullable=False)
    interested_party = db.Column(db.String)
    num_days = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Id: {self.id} DefectId:{self.defectId},' + \
               f'Date Opened: {self.open_date} Date Closed:{self.close_date},' + \
               f'User Name:{self.username} Email: {self.email},' + \
               f'OS: {self.os} OS Version: {self.os_version},' + \
               f'App: {self.application} App Version: {self.app_version},' + \
               f'Host: {self.host} Desc: {self.desc},' + \
               f'Comments: {self.comments} Status: {self.status},' + \
               f'Interested Party: {self.interested_party} Days Open: {self.num_days}'