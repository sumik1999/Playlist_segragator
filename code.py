def play_list(req_Id):
    nextpageToken=None
    plitems_details={}
    while True:
        plitems_request=youtube.playlistItems().list(part='contentDetails,snippet',maxResults=50,playlistId=req_Id,pageToken=nextpageToken)
        plitems_response=plitems_request.execute()
        for item in plitems_response['items']:
            plitems_details[item['snippet']['resourceId']['videoId']]=item['snippet']['title']
        nextpageToken=plitems_response.get('nextpageToken')
        if not nextpageToken:
            break
    return set(plitems_details.keys()),plitems_details

if __name__=="__main__":
    print("enter the two playlist urls:")
    pl1=input()
    pl2=input()
    playlist=[pl1,pl2]
    new_playlist=[]
    for item in playlist:
        index=item.rfind("=")
        new_playlist.append(item[index+1:])
         
    
    set_A,details_A=play_list(new_playlist[0])
    set_B,details_B=play_list(new_playlist[1])
    only_a=(set_A-set_B)
    only_b=(set_B-set_A)
    in_both=(set_A & set_B)

    print('Playlist A:---------------------')
    for count,x in enumerate(only_a,1):
        print(f"{count}#{details_A[x]}")
        print("")
    print('Playlist B:---------------------')
    for count,x in enumerate(only_b,1):
        print(f"{count}#{details_B[x]}")
        print()

    print('Common to both Playlist:---------')
    for count,x in enumerate(in_both,1):
        print(f"{count}#{details_A[x]}")
        print()
        

    
