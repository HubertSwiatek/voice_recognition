#!/usr/bin/env python
import requests
import json
import rospy
from std_msgs.msg import String

from Recorder import record_audio, read_audio

# Wit speech API endpoint
API_ENDPOINT = 'https://api.wit.ai/speech'

# Wit.ai api access token
wit_access_token = 'T2PC3EQVUUHIOQ27R7OLOXKVTGKYPYKO'
global text
def RecognizeSpeech(AUDIO_FILENAME, num_seconds = 5):
    
    # record audio of specified length in specified audio file
    record_audio(num_seconds, AUDIO_FILENAME)
    
    # reading audio
    audio = read_audio(AUDIO_FILENAME)
    
    # defining headers for HTTP request
    headers = {'authorization': 'Bearer ' + wit_access_token,
               'Content-Type': 'audio/wav'}

    # making an HTTP post request
    resp = requests.post(API_ENDPOINT, headers = headers,
                         data = audio)
    
    # converting response content to JSON format
    data = json.loads(resp.content)
    
    # get text from data
    text = data['_text']
    
    # return the text
    return text

def speech_to_text():  
    rospy.init_node('voice_recognition', anonymous=True)
    pub = rospy.Publisher('voice_reco', String, queue_size=10)
    rate = rospy.Rate(0.2) #0.2Hz -> 5 sekund
    while not rospy.is_shutdown():
	text =  RecognizeSpeech('myspeech.wav', 3)
	print("\nYou said: {}".format(text))    	
	pub.publish(text)
    	rate.sleep()

if __name__ == '__main__':
    try:
        
    	
	speech_to_text()
    except rospy.ROSInterruptException:
        pass
