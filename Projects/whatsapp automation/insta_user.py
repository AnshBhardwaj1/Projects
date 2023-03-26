from instagramy import InstagramUser
alpha=['aa', 'ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ah', 'ai']
for i in alpha:
    name = i
    try:
        user = InstagramUser(name)
        #followers = user.number_of_followers
        #print('Total followers:', followers)
        #following = user.number_of_followings
        #print('Total followings:',following)
        #posts = user.number_of_posts
        #print('Total posts:',posts)
    except:
        print(f"{name} is available")
