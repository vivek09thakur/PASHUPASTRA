from instagrapi import Client

creds = [
    "marshal_jon333",
    "Dollar$1357"
]

cl = Client()
# cl.login(creds[0], creds[1])
#  dump session into avoid relogin
# cl.dump_settings("session.json")
cl.load_settings("session.json")
cl.login_by_sessionid(cl.sessionid)

hashtag = "hindulivesmatter"
media = cl.hashtag_medias_top(hashtag, amount=15)


for m in media:
    try:
        # print(m)
        print(f"Media ID, Likes: {m.like_count}, Comments: {m.comment_count}")
        cl.media_like(m.id)
        print(f"Liked media ID: {m.id}")
        cl.media_save(m.id)
    except Exception as e:
        print(f"Error processing media: {e}")
        continue