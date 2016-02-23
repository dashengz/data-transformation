# read from file
# handle error cases
# strip \n
review_list_raw = [line.strip() for line in open('wine.txt', errors="replace")]

# split review from stars
# review_list contains lists
review_list = []
for review in review_list_raw:
    review_list.append(review.split("\t"))

# print 4-star reviews
for review_item in review_list:
    if len(review_item[1]) == 4:
        print(review_item[0])

# print stars of reviews containing "good"
for review_item in review_list:
    if review_item[0].lower().find('good') != -1:
        print(review_item[1])
