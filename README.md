# Social Distancing AI
Tool to moniter social distancing from CCTV, videos using Python, Deep learning, Computer Vision.

## Demo
![Demo](./demo/social_distancing.gif)

## Problem Statement:
    To moniter distance between persons from CCTV feeds or videos.
     
## Requirements:

    You will need the following to run the above:
    Python 3.5.2
    Opencv(CV2) 4.2.0
    numpy 1.14.5
    argparse
    
    For running: Good GPU, for faster results. CPU is also fine
    
## File Structure:

    main.py     : Detects and calculates distance between persons
    utills.py   : Contain functions to calculate distance, scale, transformed points
    plot.py     : Contain functions to draw bird eye view and frame
    models      : Contain yolo weights and cfg.(IMPT NOTE: weights file in not present because of size issue. 
                  It can be downloaded from here : https://pjreddie.com/media/files/yolov3.weights)
    data        : Contain video sample
    output      : Contain output frames
    output_vid  : Contain output videos(Empty for now)
      
## Usage:
        
     * If following same directory structure   
         python main.py
     * If paths for models, input video is different then given directory structure
         python main.py --model='model path' --video_path='path to video file' --output_dir='output directory' --output_vid='output vid directory'
               
## Output:

Bird Eye View       
![Bird Eye View](./demo/bird_eye_view.gif) 

Output
![Output 2](./demo/social_distancing.gif)
    
More result frames are in output folder
