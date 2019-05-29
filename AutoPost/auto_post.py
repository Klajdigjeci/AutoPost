import facebook

#try 1
from datetime import datetime, timedelta
from threading import Timer

#try 2
import schedule
import time

#facebook token
token= 'EAALsD82ZALdwBAOwco9BhGCL63FyrheZBf3g9FFdz7mBA3GLrVZCwrEQXqbs8luAoc6ZASpcMH5rpLaZAxE1K2ZCYeQxjmNFLruVl6Y19Cv19BQ0pnCgd7MzXwFpsV9HHWXUzmWItd1vLESyPRyB3QYA96ktVCUNlnpCDAHZBbTwFl5aTQRuUehcw6EmtcqXdoZD'

def something(t):
    print("auto",t)
    return

def try_1():
# x= time today
    x = datetime.today()
    print(x)
#y= tomorrow at 1 am
    y = x.replace(day=x.day, hour=19, minute=20, second=0, microsecond=0) + timedelta(days=1)
    print(y)

#delta t is how much time it is until tmr at 1 am
    delta_t=y-x
    print(delta_t)


#secs= turns the total difference into seconds
    secs=delta_t.total_seconds()
    t= Timer(secs,something)
    t.start()



def try_2():
    schedule.every().day.at("19:29:30").do(something,'It is 7:30')
    while True:
        schedule.run_pending()
        time.sleep(60)


#---------------------facebook object
fb = facebook.GraphAPI(access_token=token)
#--------------------facebook post
#fb.put_object(parent_object='me',connection_name='feed',message='8:30?',published=False,scheduled_publish_time=1557307800)
#fb.put_wall_post("Try 2")


with open("C:\\Users\\klajd\\Desktop\\Games\\garen runes.png",'rb') as imagefile:
    imagedata = imagefile.read()
fb.put_photo(image=imagedata, message="try")
#if __name__ == '__main__':
#    try_2()
#https://graph.facebook.com/v2.10/oauth/access_token?grant_type=fb_exchange_token&client_id={822502571453916}&client_secret={4343c3c985786ae7ce9c7ee57194cedb}&fb_exchange_token={EAALsD82ZALdwBAKRgqqTYQnzNWL83GRbTZCu1e7aqB2afCleVapxMHTNZBi3GkoZCwDHB4rAwcxqvyjkX9SxK0XGZAvZC25FVD4Iyi96Nd5N8UO941mtxWqmaU36EKwwjYeV6ONc4wZC5LP3UwfuAX0802rNoyuZA4lZBeZC7o9FXYGUJljdoqqBliehpF7pW2ZBZAQDda6ZCeclWuAZDZD}
