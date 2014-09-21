config = {
    "webhook_token": 'zRvQarFn8rtOYY8mcYef0uR6',
    "sqs_token": '<amazon sqs integration token>',
    "aws_access_key": '<with sqs permissions>',
    "aws_secret_key": '<with sqs permissions>',
    "username": 'pybot',
    "icon_url": 'https://slack-assets2.s3-us-west-2.amazonaws.com/10068/img/slackbot_192.png',
    "domain": 'https://shfriends.slack.com/messages/testing/',
    "queue": '<sqs queue name>',

    # stackdriver plugin
    "stackdriver_username": 'stackdriver',
    "stackdriver_channel": '#monitoring',
    "stackdriver_icon": 'https://fbcdn-profile-a.akamaihd.net/hprofile-ak-xaf1/t1.0-1/p160x160/417293_271031206332030_738543521_n.jpg',
    "stackdriver_sns_topic": 'arn:aws:sns:us-east-1:<aws account id>:<sns topic name>',

    # jira plugin
    "jira_username": '<jira username>',
    "jira_password": '<jira password>',
}
