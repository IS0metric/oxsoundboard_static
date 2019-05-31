import sys
sys.path.insert(0, '../../')

from app import app, db, Sound

data = [
    # ["filename", "name", "person", "description", "video_url"],
    ["jane_likesubdie", "Like, Subscribe and Die", "Jane", "Like, subscribe and die!", "https://www.youtube.com/watch?v=Ou3xExhXe3o"],
    ["jane_nottoday", "Not Today, Satan", "Jane", "Not Today, Satan!", "https://www.youtube.com/watch?v=-Lj4jThCuNo"],
    ["mike_sleepisoptional", "Sleep is Optional", "Mike", "Sleep is optional", "https://www.youtube.com/watch?v=Pko7aPpOEm8"],
    ["jane_sleepweak", "Sleep is for the Weak", "Jane", "Sleep is for the weak", "https://www.youtube.com/watch?v=Pko7aPpOEm8"],
    ["andy_beaningbean", "Throwing Muffins at Sean Bean", "Andy", "Why are you throwing muffins at Sean Bean?", "https://www.youtube.com/watch?v=ODYSz_Kx-d0"],
    ["jane_youare", "You Are", "Jane", "Shh, you are...", "https://www.youtube.com/watch?v=ODYSz_Kx-d0"],
    ["jane_worstthing", "Worst Thing I've Ever Seen", "Jane", "That's the worst thing I've ever seen...", "https://www.youtube.com/watch?v=RVbKyh1Mm3c"],
    ["jane_throwcat", "Throw That Cat", "Jane", "Decisive action: throw that cat.", "https://www.youtube.com/watch?v=udRYaf8oBwo"],
    ["jane_ishedead", "Is He Dead", "Jane", "Is he dead?", "https://www.youtube.com/watch?v=tvprtaZC7nY"],
    ["ian_swears", "We're Not OutsideXbox", "Ian", "We're not OutsideXbox, we can play it with the swears.", "https://www.youtube.com/watch?v=v1rV6_dqFcI"],
    ["andy_everythingrude", "Everything was Rude", "Andy", "I realise now: everything was rude.", "https://www.youtube.com/watch?v=8fLGdaUNBqc"],
    ["jane_well", "Well...", "Jane", "Well... well... well...", "https://www.youtube.com/watch?v=9oIiJ0bRt4Y"],
    ["andy_billy", "Come at me, Billy", "Andy", "Yeah, come at me, Billy the Kid!", "https://www.youtube.com/watch?v=ppSbm_EHc4I"],
    ["jane_grenadeout", "Grenade Out", "Jane", "Grenade out! Aaaand I'm out of grenades. Fine.", "https://www.youtube.com/watch?v=5ZvwDRLbEjM"],
    ["jane_headshot", "Have a Headshot", "Jane", "Have a headshot!", "https://www.youtube.com/watch?v=qNWPXdxjwoo&feature=youtu.be"],
    ["jane_mercyspree", "Mercy Spree", "Jane", "I'm on a spree. Of mercy. A mercy spree.", "https://www.youtube.com/watch?v=dg0wxybDCag"],
    ["mike_whatwasthat", "What the Hell was that", "Mike", "What the hell was that?!", "https://www.youtube.com/watch?v=hc5f30UqgdE"],
    ["mike_responsibility", "OX Accepts No Responsibility", "Mike", "OutsideXbox accepts no responsibility for laptops broken while high-fiving virtual us-es.", "https://www.youtube.com/watch?v=FMaeoWQzbNA"],
    ["jane_numbers", "How Numbers Work", "Jane", "Because that's how numbers work", "https://www.youtube.com/watch?v=FMaeoWQzbNA"],
    ["mike_dangerousalone", "It's Dangerous to go Alone", "Mike", "It's dangerous to go alone - take this!", "https://www.youtube.com/watch?v=SlplJ4IY2rw"],
    ["luke_change", "Somebody's Gonna Have To Change", "Luke", "Well, somebody's gonna have to go change... and it ain't gonna be me...", "https://www.youtube.com/watch?v=78_qjgmzCfA"],
    ["luke_shameunit", "Shame On The Unit", "Luke", "Shame on the unit!", "https://www.youtube.com/watch?v=_pdQ-HhtSRI"],
    ["jane_whocult", "Who Wants To Join My Cult", "Jane", "Who wants to join MY cult?", "https://www.youtube.com/watch?v=KGEsbXpyq6o"],
    ["jane_airhorn", "Airhorn Airhorn", "Jane", "Airhorn airhorn", "https://www.youtube.com/watch?v=KGEsbXpyq6o"],
    ["jane_joincult", "Join My Cult", "Jane", "Alright, I propose everyone joins MY cult...", "https://www.youtube.com/watch?v=KGEsbXpyq6o"],
]

print("Dataset Size: %s" % len(data))
print("--------------------\n")

for line in data:
    print("Found: %s" % line[0])
    if db.session.query(Sound).filter_by(filename=line[0]).scalar() is None:
        print("\tAdding...", end=" ")
        sound = Sound(filename=line[0], name=line[1], person=line[2], description=line[3], video_url=line[4], num_plays=0, rank=1)
        db.session.add(sound)
        print("Done")
    else:
        print("\t\tAlready in DB - Skipping")

print("Commiting...")
db.session.commit()
print("Done.")
