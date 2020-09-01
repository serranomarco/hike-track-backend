from app import app
from dotenv import load_dotenv
from app.models import db, User, Post, Location, Comment, Like
load_dotenv()


with app.app_context():
    db.drop_all()
    db.create_all()

    user = User(username='demouser', email='demo@gmail.com', first_name='Demo', last_name='User', profile_pic_url='https://hike-track-app.s3-us-west-2.amazonaws.com/hiking-profile-pic.jpeg',
                bio='I am a Demo User. Welcome to the Hike Track app, a blog site where hikers all around the coutry can share and experience new hikes, created by Marco Serrano! You can find his GitHub and LinkedIn links in the bottom right :)')
    user.set_password = 'password'
    db.session.add(user)
    location = Location(name='Larch Mountain', city='Bridal Veil', state='Oregon', country='USA',
                        description='Beyond its creek & old growth forest, this soaring mountain peak offers views of Mount St. Helens.', latitude=45.5263145614, longitude=-122.086016323)
    location2 = Location(name='Angel\'s Rest', city='Bridal Veil', state='Oregon', country='USA',
                         description='Rugged gorge cliff at around 1,500 feet with a hiking trail, waterfalls & river & mountain views.', latitude=45.5645631, longitude=-122.1545319)
    location3 = Location(name='Punch Bowl Falls', city='Eagle Creek', state='Oregon', country='USA',
                         description='35-ft-high punchbowl-style waterfall in the Columbia River Gorge National Scenic Area.', latitude=45.62333, longitude=-121.89528)
    location4 = Location(name='Multnomah Falls', city='Bridal Veil', state='Oregon', country='USA',
                         description='Well-known, dramatic cascade with a visitor\'s center, observation platform & hiking trails.', latitude=45.5759516, longitude=-122.1153641)
    location5 = Location(name='Oneonta Gorge', city='Bridal Veil', state='Oregon', country='USA',
                         description='Panoramic river gorge formed of moss-covered basalt rock with 4 waterfalls & a trailhead.', latitude=45.5895623, longitude=-122.0753629)
    location6 = Location(name='Painted Hills', city='Mitchell', state='Oregon', country='USA',
                         description='Nature area featuring walks & fossil beds amid scenic hills striped with red, tan, orange & black.', latitude=44.6615223, longitude=-120.2730726)
    location7 = Location(name='Silver Falls', city='Sublimity', state='Oregon', country='USA',
                         description='Serene park featuring 10 waterfalls on a dog-friendly 9-mile loop trail, plus campsites & cabins.', latitude=44.8512332, longitude=-122.6461975)
    db.session.add(location)
    db.session.add(location2)
    db.session.add(location3)
    db.session.add(location4)
    db.session.add(location5)
    db.session.add(location6)
    db.session.add(location7)
    db.session.commit()
