from random import choice as rc
import random
from faker import Faker
from datetime import date
from app import app
from models import db, Defect

fake = Faker('en_US')

with app.app_context():
    print('Deleting existing Defect table ...\n')
    Defect.query.delete()

    defects = []
    osystem = ["Linux Mint", "unix", "windows", "OS", "OS/370"]
    versions = ["21.2","V7","11", "18.0", "370", "360"]
    application = ["Tunnel", "Tailwind", "SASShare", "Base", "Viya"]
    appversion = ["1.2", "R.24", "2.12", "18", "v21","v1232.4"]
    browsers = ["Chrome", "Firefox","Safari","Edge"]
    browser_ver = ["3.4", "11.0", "17,8", "13","22.3"]
    hosts = ["R64", "Win", "WX6", "MVS", "Mac", "Redhat"]
    titles = ["Unable to show file name", "printing the wrong name", "Not able to change name","Printing Message twice"]
    for _ in range (30):
        defect = Defect (
            defectId = 'P' + str(random.randint(100,1000)),
            title = rc(titles),
            open_date = fake.date_this_month(after_today=True),
            close_date = fake.date_this_month(after_today=True),
            username = fake.free_email(),
            os = rc(osystem),
            os_version = rc(versions),
            application = rc(application), 
            app_version = rc(appversion),
            browser = rc(browsers),
            browser_version = rc(browser_ver),
            host = rc(hosts),
            desc = fake.paragraph(nb_sentences=5),
            comments = fake.paragraph(nb_sentences=5),
            status = "Open",
            isalert = fake.boolean(chance_of_getting_true=10),
            interested_party = fake.free_email(),
            num_days =  random.randint(1,300),
        )
        defects.append(defect)

    for defect in defects:
        defect.email = defect.username

    db.session.add_all(defects)    
    db.session.commit()
    print('Seeding Complete')  