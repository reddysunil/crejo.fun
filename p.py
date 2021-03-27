# -*- coding: utf-8 -*-
import operator
from datetime import date
td=date.today()
ye=date.today().year



movies={"don":2006,"Tiger":2008,"padmavat":2006,"lunchbox":2022,"Guru":2006,"Metro":2006}
users=['SRK','Salman','Deepika']
generes={"don":("Action","Drama"),"Tiger":"Drama","padmavat":"Comedy","Lunchbox":"Drama","Guru":"Drama","Metro":"Romance"}

reviews=[]

critics=[]

def base():
    print('\n')
    print("1.ADD NEW MOVIE DETAILS")
    print("2.SHOW ALL REVIEWS")
    print("3.ADD REVIEW ")
    print("4.Average review score of the movie")
    print("5.ADD NEW USER")
    print("6.top movies in the particular genre")
    print("7.For average review score in a particular year of release ")
    print("8.To exit ")
    
    print('\n')
    print('please enter the choice')
    print('\n')
    x=int(input())
    if x==3:
        print("Enter the user")
        p=str(input())
        if p in users:
            print("Enter the movie name")
            mov=str(input())
            if mov in movies:
                if movies[mov] < ye:
                    print("Enter the review score ranging from 1 to 10")
                    s=int(input())
                    reviews.append([p,mov,s])
                    for j in users:
                        c=0
                        for i in  range (0,len(reviews)):
                            if reviews[i][0] == j:
                                c=c+1
                        if(c>=3):
                            critics.append(j)
                else:
                    print('\n')
                    print("Exception movie yet be released ")
                    print('\n')
            else:
                print("movie not found")
                print('\n')
            if p in critics:
                print("since"+p+"has published 3 reviews he is promoted to critic now")
                print('\n')
                
        else:
            print("please add the user :")
    if x==2:
        print(reviews)
    if x==1:
        print("please enter the movie name  ")
        k=str(input())
        print("please enter the year ")
        y=int(input())
        movies[k]=y
        print("Movies list updated !! Thank You ")
        print("Enter genre of the movie ")
        g=str(input())
        generes[k]=g
        
    if x==4:
        print("please enter the movie name")
        k=str(input())
        s=0
        c=0
        for i in  range (0,len(reviews)):
            if k==reviews[i][1]:
                c=c+1
                if reviews[i][0] in critics:
                    s=s+2*(reviews[i][2])
                else:
                    s=s+reviews[i][2]
        print(str(float(s/c))+' is the average review score for the '+k+' movie')
    if x==5:
        print("ENTER NEW USER NAME")
        c=str(input())
        users.append(c)
    
    print('\n')
    print('\n')
    if x==6:
        print("Enter the genre")
        print('\n')
        k=str(input())
        s=[]
        for item in generes:
            if k==generes[item] or k in generes[item]:
                s.append(item)

        tp={}
        for m in s:
            score=0
            for cr in critics:
                for i in range (0,len(reviews)):
                    if reviews[i][0]==cr and reviews[i][1]==m:
                        score=score+(2*(reviews[i][2]))
            tp[m]=score
        sorted_d = dict( sorted(tp.items(), key=operator.itemgetter(1),reverse=True))
        for k in sorted_d.keys():
            print('\n')
            print(k)
        print("NOTE:NO REVIWED MOVIES SCORE CONSIDERED AS 0 AND GIVEN LIST")
        print('\n')
        print('\n')

    if x==7:
        print('\n')
        print('input the year')
        print('\n')
        y=int(input())
        print('\n')
        p=[]
        for item in movies:
            if movies[item]==y:
                p.append(item)
        co=len(p)
        sc=0
        for x in p:
            for i in range(0,len(reviews)):
                if reviews[i][1]==x:
                    if reviews[i][0] in critics:
                        sc=sc+(2*(reviews[i][2]))
                    else:
                        sc=sc+reviews[i][2]
        
        print("average review score in a particular year of release is "+str(float(sc/co))+".")
        print('\n')
    if x==8:
        quit()
                        
                        
                
            
               
    base()
    print('\n')
base()
print('\n')


        

