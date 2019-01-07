
#################################################################
# LOGIN IG AND LIKE RANDOM POSTS    
#################################################################

# https://github.com/timgrossmann/InstaPy

from instapy import InstaPy
from instapy.util import smart_run



# login credentials
insta_username = <IG_username>
insta_password = <IG_password>

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_dont_like(["pizza", "#store"])

    # actions
    session.like_by_tags(["natgeo"], amount=10)


