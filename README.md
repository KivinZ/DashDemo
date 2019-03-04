# DashDemo
LSTM Model Accuracy app: http://dashmoneyball.us-east-2.elasticbeanstalk.com/

Static Dash Demo ```static-demo.py```
Year Slider demo ```callback.Demo.py```

Callback Demo app http://callback.us-east-2.elasticbeanstalk.com/

User starter code to develop your own app,
if your requirement.txt does not run on aws, try delete all windows related py (or use mine ;p)

## Install dash
pip install dash

pip install dash-renderer

pip install dash-html-components

pip install dash-core-components


## To create an docker environment and deploy on AWS
https://www.phillipsj.net/posts/deploying-dash-to-elastic-beanstalk

## Freeze your library
pip freeze > requirements.txt
**remove any library with 'win' in it!** if you are using windows

## Upload to AWS Elastik Beanstalk
Rename your python code to application.py
zip with requirements.txt
