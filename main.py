from critics import *
import recommendations

choice=raw_input('enter your search type\n1.By user\n2.By Book\nChoice:\t')

if choice=='1':
    user = raw_input('enter the user ID:\t')
    print '\n'
    print 'Books till now read by the user are:\n'
    print critics[user],'\n'

    dischoice=raw_input('enter your choice\n1.euclidian distance\n2.pearson corelation\nchoice:\t')
    if dischoice=='1':
        print 'top matched user according to the euclidian distance\n'
        print recommendations.topMatches(critics,user,3,recommendations.sim_distance),'\n'
        print 'Recommended books according to the euclidian distance\n'
        print recommendations.getRecommendations(critics,user,similarity=recommendations.sim_distance)[0:3],'\n'
    else:
        if dischoice=='2':
            print 'top matched user according to the pearson corelation\n'
            print recommendations.topMatches(critics,user, 3),'\n'
            print 'Recommended books according to the pearson corelaton\n'
            print recommendations.getRecommendations(critics,user)[0:3],'\n'
        else:
            print 'invalid choice... try again'
else:
    if choice =='2':
        critic = recommendations.transformPrefs(critics)
        book=raw_input('enter the book name:\t')
        print '\n'
        print 'Users who have read the book till now are:\n'
        print critic[book],'\n'
        disch=raw_input('enter your choice\n1.euclidian distance\n2.pearson corelation\nchoice:\t')
        if disch=='1':
            print 'top matched book according to the euclidian distance\n'
            print recommendations.topMatches(critic,book,3,recommendations.sim_distance),'\n'
            print 'Recommended user according to the euclidian distance\n'
            print recommendations.getRecommendations(critic,book,similarity=recommendations.sim_distance)[0:3],'\n'
        else:
            if disch=='2':
                print 'top matched book according to the pearson corelation\n'
                print recommendations.topMatches(critic,book, 3),'\n'
                print 'Recommended users according to the pearson corelaton\n'
                print recommendations.getRecommendations(critic,book)[0:3],'\n'
            else:
                print 'invalid choice... try again'
    else:
        print 'invalid choice... try again'
