XIAOMAGE_LABEL_LIST = [
    "Xiaomage",
]
COOK_LABEL_LIST = [
    "Cook",
]
MOVIE_LABEL_LIST = [
    "Movie",
]
READ_LABEL_LIST = [
    "Read",
]
DRAMA_LABEL_LIST = [
    "Drama",
]
PUSHUP_LABEL_LIST = [
    "PushUps",
]
BANGUMI_LABEL_LIST = [
    "Bangumi",
]
GAME_LABEL_LIST = [
    "Game",
]
MONEY_LABEL_LIST = [
    "Money",
]
MEDITATION_LABEL_LIST = [
    "Meditation",
]
MORNING_LABEL_LIST = [
    "Morning",
]
GTD_LABEL_LIST = [
    "GTD",
]

WEEKLY_LABEL_LIST = [
    "Weekly",
]
SQUAT_LABEL_LIST = [
    "Squat",
]
STORY_LABEL_LIST = [
    "Story",
]

### 2023 NEW ###
TIMELINE_LABEL_LIST = [
    "Timeline",
]

MY_BLOG_REPO = "lesnolie/Marverick"
GITHUB_README_COMMENTS = (
    "(<!--START_SECTION:{name}-->\n)(.*)(<!--END_SECTION:{name}-->\n)"
)

# add new label here
LABEL_DICT = {
    "Cook": {"label_list": COOK_LABEL_LIST, "comment_name": "my_cook"},
    "Movie": {"label_list": MOVIE_LABEL_LIST, "comment_name": "my_movie"},
    "Read": {"label_list": READ_LABEL_LIST, "comment_name": "my_read"},
    "Drama": {"label_list": DRAMA_LABEL_LIST, "comment_name": "my_drama"},
    "Bangumi": {"label_list": BANGUMI_LABEL_LIST, "comment_name": "my_bangumi"},
    "Game": {"label_list": GAME_LABEL_LIST, "comment_name": "my_game"},
    "Story": {"label_list": STORY_LABEL_LIST, "comment_name": "my_story"},
}


##### SHANBAY ######
MY_SHANBAY_USER_NAME = "盼盼"
SHANBAY_CALENDAR_API = "https://apiv3.shanbay.com/uc/checkin/calendar/dates/?user_id={user_name}&start_date={start_date}&end_date={end_date}"
MY_SHANBAY_URL = f"https://web.shanbay.com/web/users/{MY_SHANBAY_USER_NAME}/zone"

##### DUO ######
MY_DUOLINGO_URL = "https://www.duolingo.com/profile/Leslieilxyz"

##### CICHANG ######
MY_CICHANG_URL = "https://twitter.com/yihong06181/status/1359040099107897344?s=20"

##### BASE COMMENT TABLE ######
BASE_ISSUE_STAT_HEAD = "| Name | Start | Update | \n | ---- | ---- | ---- | \n"
BASE_ISSUE_STAT_TEMPLATE = "| {name} | {start} | {update} | \n"

##### BLOG COMMENT ######
BLOG_ISSUE_STAT_HEAD = (
    "| Name | Start | Update | Comments | \n | ---- | ---- | ---- | ---- |\n"
)
BLOG_ISSUE_STAT_TEMPLATE = "| {name} | {start} | {update} | {comments} | \n"


##### FOOD COMMENT TABLE ######
FOOD_ISSUE_STAT_HEAD = (
    "| Name | First_date | Last_date | Times | \n | ---- | ---- | ---- | ---- |\n"
)
FOOD_ISSUE_STAT_TEMPLATE = "| {name} | {first_date} | {last_date} | {times} |\n"


##### Month Summary ######
MONTH_SUMMARY_HEAD = "| Month | Number | \n | ---- | ---- | \n"

MONTH_SUMMARY_STAT_TEMPLATE = "| {month} | {number} |\n"
##### Forest Summary ######
FOREST_SUMMARY_HEAD = "| Tag | Times | \n | ---- | ---- | \n"
FOREST_SUMMARY_STAT_TEMPLATE = "| {tag} | {times} |\n"
FOREST_ISSUE_NUMBER = 14
TIMEZONE = "Asia/Shanghai"
##### GPT PROMPT #####
PROMPT = f"跟你对话的是一个 {YEAR - 1992} 岁的男人，有个 {YEAR-1998} 岁的女朋友，喜欢编程，游戏。\
工作是在亚马逊日本站开店铺卖东西，成绩一般般。喜欢电影和读书，最喜欢的电视剧是请回答1988。但有时候会感到孤独，你能作为他的朋友或助手给他回复么？因为需要记录回复，你的回复内容在 50 字以内，\
，不要带换行符号，以下为他想聊的内容： "
