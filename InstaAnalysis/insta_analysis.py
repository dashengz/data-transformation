import json
from urllib.request import urlopen

# Parse json data
# Recent media posted by myself
# Replace ACCESS_TOKEN with your own access_token
url = "https://api.instagram.com/v1/users/self/media/recent/?access_token=ACCESS_TOKEN"
response = urlopen(url).read().decode('utf8')
obj = json.loads(response)

# Like counts of media that have certain tag (#photograph in this case) over time
# Most recent one first
target_tag = "photography"
like_count_if_tagged = []
for post in obj['data']:
    if post['tags'] is not None and target_tag in post['tags'] and post['likes'] is not None:
        like_count_if_tagged.append(post['likes']['count'])
print(like_count_if_tagged)

# Data visualization
for i in like_count_if_tagged:
    pattern = '{:->' + str(i + 1) + '}'
    print("^" + pattern.format('>'))
# ^--------------------------------->
# ^---------------------->
# ^------------------------>
# ^---------------->
# ^------------------->


# See if the number of tags added to a post
# is related to the number of likes a post received
tag_like_list = []
for post in obj['data']:
    if post['tags'] is not None and post['likes'] is not None:
        tag_like_list.append([len(post['tags']), post['likes']['count']])

tag_like_list = sorted(tag_like_list, reverse=True)
print(tag_like_list)

# Use this to add extra spaces (if needed)
max_tag_count = tag_like_list[0][0]

# Data visualization
for pair in tag_like_list:
    tag_pattern = '{:-<' + str(pair[0] + 1) + '}'
    like_pattern = '{:->' + str(pair[1] + 1) + '}'
    print(" " * (max_tag_count - pair[0]) + tag_pattern.format('<'), "| ", end="")
    print(like_pattern.format('>'), "", end="")
    print()
    # <---------------- | --------------------------------->
    #  <--------------- | ------------------------>
    #    <------------- | ------------------->
    #     <------------ | ---------------------->
    #     <------------ | --------------------->
    #      <----------- | ---------------->
    #       <---------- | ------------------------>
    #       <---------- | --------------------->
    #       <---------- | -------------------->
    #        <--------- | ------------------------->
    #         <-------- | -------------------------->
    #           <------ | ------------->
    #             <---- | ------------>
    #             <---- | -------->
    #              <--- | ----------------->
    #              <--- | --------------->
    #              <--- | ------------>
    #               <-- | ---------------->
    #                <- | ----->
    #                 < | ------------>
