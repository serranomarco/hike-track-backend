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
    user2 = User(username='steveholden', email='steveholden@gmail.com', first_name='Steve',
                 last_name='Holden', profile_pic_url='https://i.imgur.com/B2doARA.jpeg')
    user2.set_password = 'steveholden'
    user3 = User(username='lance234weaver', email='lanceweaver@gmail.com', first_name='Lance', last_name='Weaver',
                 profile_pic_url='https://i.imgur.com/GbkIAW4.jpeg')
    user3.set_password = 'lanceweaver'
    user4 = User(username='jeremywallace', email='jeremywallace@gmail.com', first_name='Jeremy', last_name='Wallace',
                 profile_pic_url='https://i.imgur.com/8A8t4kB.jpg')
    user4.set_password = 'jeremywallace'
    user5 = User(username='emma908schmidt', email='emmaschmidt@gmail.com', first_name='Emma', last_name='Schmidt',
                 profile_pic_url='https://i.imgur.com/AKlIleQ.jpeg')
    user5.set_password = 'emmaschmidt'
    user6 = User(username='laceymeyers89', email='laceymeyers@gmail.com', first_name='Lacey', last_name='Meyers',
                 profile_pic_url='https://i.imgur.com/2SGKeRO.jpeg')
    user6.set_password = 'laceymeyers'
    user7 = User(username='veronicaalverez', email='veronicaalveres@gmail.com', first_name='Veronica', last_name='Alverez',
                 profile_pic_url='https://i.imgur.com/Hov9R1b.jpeg')
    user7.set_password = 'veronicaalverez'
    user8 = User(username='trentgwan34', email='trentgwan@gmail.com', first_name='Trent', last_name='Gwan',
                 profile_pic_url='https://i.imgur.com/tS8G2zH.jpg')
    user8.set_password = 'trentgwan34'
    user9 = User(username='ellawatanbe', email='ellawatanbe@gmail.com', first_name='Ella', last_name='Watanbe',
                 profile_pic_url='https://i.imgur.com/SJARRsf.jpg')
    user9.set_password = 'ellawatanbe'
    user10 = User(username='maia-lennon', email='maialennon@gmail.com', first_name='Maia', last_name='Lennon',
                  profile_pic_url='https://i.imgur.com/jKFkUyH.jpeg')
    user10.set_password = 'maialennon'
    user11 = User(username='abramahluwalia', email='abram@gmail.com', first_name='Abram', last_name='Ahluwalia',
                  profile_pic_url='https://i.imgur.com/OTYropp.jpeg')
    user11.set_password = 'abramahluwalia'
    db.session.add(user)
    db.session.add(user2)
    db.session.add(user3)
    db.session.add(user4)
    db.session.add(user5)
    db.session.add(user6)
    db.session.add(user7)
    db.session.add(user8)
    db.session.add(user9)
    db.session.add(user10)
    db.session.add(user11)
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
    location8 = Location(name='Glacier National Park', city='Columbia Falls', state='Montana', country='USA',
                         description='Glacier National Park is a 1,583-sq.-mi. wilderness area in Montana\'s Rocky Mountains, with glacier-carved peaks and valleys running to the Canadian border. It\'s crossed by the mountainous Going-to-the-Sun Road. Among more than 700 miles of hiking trails, it has a route to photogenic Hidden Lake. Other activities include backpacking, cycling and camping. Diverse wildlife ranges from mountain goats to grizzly bears.',
                         latitude=48.6960847, longitude=-113.8070624)
    location9 = Location(name='Banff National Park', city='Alberta\'s Rockies', state='Alberta', country='Canada',
                         description='Rocky Mountain park offering year-round activities & glacial lakes such as Lake Louise, also a town.', latitude=51.496845, longitude=-115.928055)
    location10 = Location(name='Frazier Discovery Trail', city='Crozet', state='Virginia', country='USA',
                          description='Frazier Discovery Trail is a 1.2 mi/1.9 km loop with a view of the South District of Shenandoah National Park. From the north end of the Loft Mountain Wayside parking area at mile 79.5, cross Skyline Drive and follow the blue-blazed Frazier Discovery Trail.',
                          latitude=38.051971, longitude=-78.699120)
    location11 = Location(name='Appalachian Trail', city='Harpers Ferry', state='West Virginia', country='USA',
                          description='Headquarters for famed trail\'s conservancy group, also a visitor center with exhibits & information.', latitude=41.5929, longitude=-73.588)

    db.session.add(location)
    db.session.add(location2)
    db.session.add(location3)
    db.session.add(location4)
    db.session.add(location5)
    db.session.add(location6)
    db.session.add(location7)
    db.session.add(location8)
    db.session.add(location9)
    db.session.add(location10)
    db.session.add(location11)

    post = Post(user_id=4, location_id=8, title='National Park Adventures',
                text='Fifty miles of superlative scenery on Going-to-the-Sun Road. Sixty-two species of mammals, from pygmy shrews to majestic mountain goats and grizzly bears. More than 260 species of birds, 780 miles of trails and 10,000 years of natural history. And some spectacular national park lodges. You\'ve got six days. It all adds up to one incredible story to tell.', photo_url='https://www.backroads.com/sites/default/files/trips/2018/slideshow/WGLQ-glacier-waterton-lakes-walking-hiking-tour-1.jpg')
    post6 = Post(user_id=1, location_id=2, title='Angel\' Rest',
                 text='Angels Rest  is a 4.5 mile heavily trafficked out and back trail located near Corbett, Oregon that features a river and is rated as moderate. The trail is primarily used for hiking, walking, nature trips, and bird watching and is best used from April until September. Dogs are also able to use this trail but must be kept on leash.')
    post2 = Post(user_id=5, location_id=9, title='What are your spots?',
                 text='I spent the entire month of June camping and exploring Alberta, Canada’s Banff National Park, as well as Yoho and Jasper National Parks. Banff has a reputation for being a favorite spot among outdoor adventure travelers in large part because of the all the outdoor activities you can do in and around the Canadian Rockies. The turquoise glacial lakes, winding roads, and fun mountain town vibe ranks it high on the list for anyone who wants to base their trip around the outdoors and still experience the culture.', photo_url='https://s34003.pcdn.co/wp-content/uploads/2019/05/Banff_Morraine-Lake.jpg.optimal.jpg')
    post5 = Post(user_id=1, location_id=1, title='Larch Mountain',
                 text='The Larch Mountain trail was constructed in 1915 by members of the Eastside Progressive Businessmen\'s Club. Many of those involved became founding members of the Trails Club of Oregon. Portland residents might recognize the names of a few early members such as store owners Julius Meier and Aaron Frank, newspaperman Henry Pittock, and Columbia River Highway Builders Sam Lancaster and Simon Benson, the latter contributing $3,000. The trail route was flagged out by the "mountain man" Ralph Shelly. Today the Trails Club still maintains Nesika Lodge on a spur trail off of the Larch Mountain Trail. While the stone lodge itself survived the 2017 fire, the dormitory buildings and most other structures did not')
    post3 = Post(user_id=3, location_id=10, title='Frazier Discovery Trail',
                 text='One of the most fun short day hikes in Shenandoah National Park, the Frazier Discovery Trail loops its way past a scenic rocky outcrop. Easily accessible from the Loft Mountain Campground and Loft Mountain Wayside, the trail is short and involves a moderate climb.', photo_url='https://cdn.shortpixel.ai/client/q_lossy,ret_img,w_1280/https://www.travel-experience-live.com/wp-content/uploads/2017/11/Turk-Mountain-Best-Day-Hikes-in-Shenandoah-National-Park.jpg')
    post4 = Post(user_id=2, location_id=11, title='The Appalachian Trail',
                 text='A day hike on the Appalachian Trail can be a vigorous hike to an amazing destination or a wonder-filled nature walk. It can be easy or challenging.', photo_url='https://bloximages.chicago2.vip.townnews.com/cumberlink.com/content/tncms/assets/v3/editorial/3/32/332eb731-ad93-5b57-bf05-a866ee3ea06a/5a860c0c8804c.image.jpg')
    db.session.add(post)
    db.session.add(post2)
    db.session.add(post3)
    db.session.add(post4)
    db.session.add(post5)
    db.session.add(post6)
    db.session.commit()
