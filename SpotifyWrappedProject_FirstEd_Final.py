#SpotifyWrappedProject_FirstEd_Final

#Project Name: SpotifyWrappedProject_FirstEd_Final
#Programmed by: Julian Simeonov
#Project Date: December 15, 2022.
#Description: This is the final version of the First Edition of my SpotifyWrapped project, scrubbing a user's downloaded Spotify data and providing accurate ranking of a users most streamed songs and artists.

#importing os module to gather data from my os (file list from my current (listdir) directory)
import os 

#importing json library
import json 
#Importing statistics library and mode method for gathering most common item in list.
import statistics
from statistics import mode
#Importing itemgetter function from operator module for sorting list of most streamed song/artist by time streamed
from operator import itemgetter

#Importing csv
import csv

#~~~
#Next 3 lines initialize string variables for the user input. 
userIn01 = ""
userIn02 = ""
#Could be made more efficient using 1 variable, but efficiency is a later task.
#~~~

#+++Defining variables (empty lists) needed 
fileList = os.listdir('.') #retrieves a list of files in the current directory
testList = [] #Can be removed
sptfyData = []
largeSpotifyData = []
timeStreamedWorkingList = []
#+++

#===Defining variables (empty lists), working lists used for sorting most played artists and songs (by streams and time).
mpArtistWorkingList = []  #Working list for most played artist.
mpSongWorkingList01 = []  #Working list for most played song
mpSongWorkingList02 = []  #Second Working list for most played song
timeStreamedWorkingList = [] #Working list, idea is that this creates a list with all relevant data needed to sort by most time streamed.
tsSongsWorkingList01 = [] #Working list for time streamed of each song (labeled 01 in case I need multiple later)
tsSongsWorkingList02 = [] #second working list for time streamed song.
tsArtistWorkingList01 = [] #Working list for time streamed of each artist (labeled 01 in case I need multiple later)
tsArtistWorkingList02 = [] #second working list for time streamed artist.

#Adding lists of the headers for the .csv files.
headerArtist = ["Rank", "Artist", "# of Times Played"]
headerSong = ["Rank", "Song", "Artist", "# of Times Played"]
headerTsArtist = ["Rank", "Artist", "Time Streamed"]
headerTsSong = ["Rank", "Song", "Artist","Time Streamed"]

#Also adding variables of the actual fully sorted lists:
mpArtist = []
mpSong = []
mtsSong = [] #List sorting by most played songs by time streamed.
mtsArtist = [] #List sorting by most played artist by time streamed.
#===


#~~~ Can I make these definitions more efficient?
#Defining user input function #1, asking user if they've downloaded their Spotify data.
def gatherUserInput01(userIn01):
    userIn01 = input("\nHave you downloaded your Spotify data? (type Y for yes, or N for no) ")
    #print(i)
    print(userIn01)
    if userIn01 == "Y" or userIn01 == "y" or userIn01 =="yes" or userIn01 == "YES" or userIn01 =="Yes" or userIn01 == "yES":
    #~~Put this range into its own function~~~
        gatherUserInput02(userIn02)
    #~~~~~~~
    elif userIn01 == "N" or userIn01 == "n" or userIn01 == "no" or userIn01 == "NO" or userIn01 == "No" or userIn01 == "nO":
        print("Download your Spotify data and come back here when you have.")
        gatherUserInput01(userIn01)
    else:
        print("Invalid input, let's try again. (Please only use Y for yes, or N for no)")
        gatherUserInput01(userIn01)

#Defining user input function #2, asking user if they've moved their Spotify data to the same folder as this python program/file?
def gatherUserInput02(userIn02):
    userIn02 = input("\nHave you put your Spotify data in the same folder as this program? (type Y for yes, or N for no)")
    print(userIn02)
    if userIn02 == "Y" or userIn02 == "y" or userIn02 == "yes" or userIn02 == "YES" or userIn02 == "Yes" or userIn02 == "yES":
        print("Let's get started... \n")
    elif userIn02 == "N" or userIn02 == "n" or userIn02 == "no" or userIn02 == "NO" or userIn02 == "No" or userIn02 == "nO":
        print("Move your Spotify data to the same folder as this program and come back here when you have.")
        gatherUserInput02(userIn02) 
    else:
        print("Invalid input, let's try again. (Please only use Y for yes, or N for no)")
        gatherUserInput02(userIn02)
#~~~


#Move this? (below input functions??)
#+++Defining function to pull Spotify data from the .json files in the directory.
def pullData(spotifyFiles):        
    for j in fileList:
        if j[:16] == "StreamingHistory" and j[-5:] == ".json":
            dictionary = open(j, encoding="utf8")
            dictReturned = json.load(dictionary)
            #print(dictReturned, "\n")
            sptfyData.extend(dictReturned)
            dictionary.close()
#+++


#===Defining function to gather 3 lists out of the list of dictionaries gathered from the Spotify json data.
def gatherListData(listGathered):
    for i in listGathered:
        mpArtistWorkingList.append(i["artistName"])
        mpSongWorkingList01.append([i["trackName"], i["artistName"]])#Maybe adjust to include artist name as well?
#        tsSongsWorkingList01.append([i["artistName"],i["trackName"],i["msPlayed"]])#May not nead this...
#        tsArtistWorkingList01.append([i["artistName"],i["trackName"],i["msPlayed"]]) #...and can remove this, and just use 1 working list for both
        timeStreamedWorkingList.append([i["artistName"],i["trackName"],i["msPlayed"]]) #Remove this, it's not needed... actually no, see 2 comments up
#===

#---Defining function that sorts the artists from most to least listened to.
def sortArtistData(mpArtistWorkingList): 
    counter = 0 
    mpArtist = []
    while len(mpArtistWorkingList) != 0: #While loop runs while working list is not empty.
        counter = counter + 1 #Adds 1 to the counter. This counter will be the 'rank' of each artist (in order of listened to)
        #print(count)
        mostCommon=mode(mpArtistWorkingList) #Local variable, which is equal to the most common item in the list at the time the while loop runs.
        mpArtist.append((counter, mostCommon, mpArtistWorkingList.count(mostCommon))) #Adds the most common item in the list along with its rank of most common artists (as a list in a list)
        mpArtistWorkingList = list(filter((mostCommon).__ne__, mpArtistWorkingList)) #Changes the mpArtistWorkingList, filtering out all the most common artists.
    else: #When the working list is empty resets the counter and prints the list of most played artists.
        counter=0
        print(mpArtist)
        with open("mpArtist.csv", "w", encoding="UTF8") as f:
            writer = csv.writer(f)
            writer.writerow(headerArtist)
            writer.writerows(mpArtist)
#---

#___Defining function that sorts the songs from most to least listened to.
def sortSongData(workingList): 
    #Below am calling 2 empty lists. Will become working lists of lists for purpose of sorting songs by most # of times played.
    #Calling these variables locally as they are only used within the function, and no value in their use outside of the function.
    mpSongWorkingList03 = []
    mpSongWorkingList04 = []
    indexValue = 0
    playedSongRank = 0
    #counter=0
    mpSong = []
    for i in workingList: #For every song (every item in mpSongWorkingList02)
        #print(i)
        if i not in mpSongWorkingList03:
            #add the item to the mpSongWorkingList03
            mpSongWorkingList03.append(i)
            mpSongWorkingList04.append([i[0],i[1],1])
        else:
            indexValue=mpSongWorkingList03.index(i)
            #print(mpSongWorkingList04[indexValue])
            mpSongWorkingList04[indexValue] = [i[0], i[1], mpSongWorkingList04[indexValue][2] + 1]
            #Add 1 play (+ 1 to index 2) to the occurance of the song in the mpSongWorkingList04
    #print(mpSongWorkingList04)
    mpSongWorkingList02 = sorted(mpSongWorkingList04, key=lambda x:x[2], reverse=True) #Sets mpSongWorkingList02 to the mpSongWorkingList04 but sorted by the 3rd index of each list of lists (sorted by time streamed)
    #^idk why the line above needs me to use another variable to sort into. Why Can't I just sort mpSongWorkingList04 into itself
    #print(mpSongWorkingList02)
    for j in mpSongWorkingList02:
            playedSongRank = playedSongRank + 1 #Adds 1 to the playedSongRank variable, adding to the times played'rank' of each song.
            mpSong.append([playedSongRank, j[0], j[1], j[2]])
    print("\n Your most streamed songs by order of times streamed: \n", mpSong)
    with open("mpSong.csv", "w", encoding="UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(headerSong)
        writer.writerows(mpSong)

#___

#~~~Function to find most streamed artist by time streamed - START
#Meh, just see comments for the sortMostTimeStreamedSong function for the functionality of this function. I am too lazy to comment rn.
def sortMostTimeStreamedArtist(listGoesHere):
    count1 = 0
    count2 = 0
    index = 0 #setting index to 0 just so it is of integer type and a variable existing throughout the function.
    artistCharted = False
    for i in listGoesHere:
        count1 = 0
        for j in tsArtistWorkingList02: #switched to just mtsArtist, won't need a working list at this point. Can probably just use timeStramedWorkingList
            if i[0] == j[0]:
                artistCharted = True
                index = count1
                #index = count of position of item in working list
            count1 = count1 + 1  #Adding to counter at the end of every run of the 2nd "for loop".
        if artistCharted == False:
            tsArtistWorkingList02.append([i[0],i[2]]) 
        elif artistCharted == True:
            tsArtistWorkingList02[index][1] = tsArtistWorkingList02[index][1] + i[2]
            artistCharted = False
    tsArtistWorkingList01 = sorted(tsArtistWorkingList02, key=lambda x:x[1], reverse=True)
    for i in tsArtistWorkingList01:
        count2 = count2 + 1
        mtsArtist.append([count2, i[0], i[1]])
    #mtsArtist = sorted(tsArtistWorkingList02, key=lambda x:x[1], reverse=True)
    print(mtsArtist, "\n")
    with open("mtsArtist.csv", "w", encoding="UTF8") as f:
            writer = csv.writer(f)
            writer.writerow(headerTsArtist)
            writer.writerows(mtsArtist)
#~~~Function to find most streamed artist by time streamed - END

#+++Function to find most streamed song by time streamed - START
def sortMostTimeStreamedSong(sortedList): 
    counter = 0 #Variable 'counter', integer type, equal to 0
    index = 0 #Variable 'index', integer type, equal to 0
    rank = 0 #Variable 'rank', integer type, equal to 0
    songCharted = False #Variable 'songCharted', boolean type, equal to 'False'
    for i in sortedList: #For loop, for each item in 'timeStreamedWorkingList'
        counter = 0 #Runs as an index value for every itme in tsSongsWorkingList01
        for j in tsSongsWorkingList01: #For loop, runs through every song in tsSongsWorkingList01 (sometimes empty, sometimes with many)
            if i[0] == j[0] and i[1] == j[1]: #If a song/artist in the (initially empty) working list is equal to timeStreamedWorking list entry
                songCharted = True #Variable becomes True if songs are equal (suggests a song has already been listened to & accounted for (charted))
                index = counter #Sets var 'index' to the value of 'counter'. Should be the index value of the already charted song in the 'tsSongsWorkingList02' list
            counter = counter + 1 #Needed, counts the index of each item in the tsSongWorkingList01 (list of each song, only once, w. time streamed info)
        if songCharted == False: #If songCharted=False, runs if a song in the timeStreamedWorkingList hasn't been added to tsSongWorkingList01
            tsSongsWorkingList01.append([i[0],i[1],i[2]])   #Adds the new (not yet charted) song to the 'tsSongsWorkingList01' list
        elif songCharted == True: #If the song has already been charted (an entry is already in 'tsSongsWorkingList02')
            tsSongsWorkingList01[index][2] = tsSongsWorkingList01[index][2] + i[2]
            songCharted = False #Sets 'songCharted' to 'False', will turn 'True' next time a song in the 'timeStreamWorkingList' has already been charted in 'tsSongsWorkingList02' 
    tsSongsWorkingList02 = sorted(tsSongsWorkingList01, key=lambda x:x[2], reverse=True) #Sets tsSongsWorkingList02 to the tsSongsWorkingList01 but sorted by the 3rd index of each list of lists (sorted by time streamed)
    #^idk why the line above needs me to use another variable to sort into. Why Can't I just sort tsSongsWorkingList01 into itself
    for k in tsSongsWorkingList02: #For loop adding a rank to the songs based on time streamed
        rank = rank + 1 #Add a value to the rank variable (per the rank of thesongs in order of time streamed)
        mtsSong.append([rank, k[1], k[0], k[2]]) #Adds to the mtsSong in the order [rank, song, artist, time streamed]
    print("\n Your most streamed songs by order of time spent listening is: \n", mtsSong)
    with open("mtsSong.csv", "w", encoding="UTF8") as f:
            writer = csv.writer(f)
            writer.writerow(headerTsSong)
            writer.writerows(mtsSong)
#+++Function to find most streamed song by time streamed - END



#~~Calling prev. defined functions.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("Thanks for using the Spotify Wrapped program. \n Let's get started...") #Intro statement, welcoming user.

gatherUserInput01(userIn01)
#print("Test, hoping this prints after I've provided all my user inputs.")

pullData(fileList)
print("Data has been pulled...")
gatherListData(sptfyData)
print("\n...lists have been gathered...")
#print(mpArtistWorkingList)
#print(mpSongWorkingList) #Maybe adjust to include artist name as well??
#print(tsSongsWorkingList01)

#time for sorting...
print("\nSort time...\n")
print("Sorting by most played artist...")
sortArtistData(mpArtistWorkingList)
print("Sorting by most played song...")
sortSongData(mpSongWorkingList01)
print("Sorting time streamed artist...")
sortMostTimeStreamedArtist(timeStreamedWorkingList)
print("Sorting time streamed song...")
sortMostTimeStreamedSong(timeStreamedWorkingList)
print("\nAll done!\n\nThanks for using our program!")
print("\nFor best data viewing experience, exit this program and enjoy the .csv files with your sorted data found in the same folder as this script.")
#Print test (functions don't change global variables...hm):
#print(mpArtist)
