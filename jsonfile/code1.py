import json

def load_data(fillename):
    with open(fillename, "r") as file:
        data = json.load(file)
    return data 

def clean_data(data):
    text_to_num = {
            "one" : 1,
            "two" : 2,
            "three" : 3,
            "four" : 4,
            "five" : 5
    }
    cleaned_data = []
    unique_users = set()
    for user in data:
        ## Cleaning rating data
        raw_rating = user["rating"].strip().lower()
        if raw_rating in text_to_num:
            raw_rating = text_to_num[raw_rating]
        user["rating"] = str(raw_rating)

        ## Handling Missing Value
        raw_age = user.get("age")
        if raw_age == None:
            user["age"] = None

        ## Deduplication
        if user["name"].strip() in unique_users:
            continue
        unique_users.add(user["name"])
        cleaned_data.append(user)

    return (cleaned_data)

def avg_rating(data):
    total_rating = 0
    for user in data:
        total_rating = total_rating + float(user["rating"])
    return f"Average Rating is {total_rating/len(data)}"

def percentage_poor_rating(data):
    poor_rating = 0
    for user in data:
        if float(user["rating"]) < 3.0:
            poor_rating += 1
    return f"Percentage of poor rating is: {(poor_rating * 100)/len(data)}%"

def recommendation(data):
    recomm = []
    for user in data:
        curr_recomm = {}
        curr_recomm["name"] = user['name']
        if float(user['rating']) >= 4.0:
            curr_recomm["brand"] = "Apple"
        else:
            curr_recomm["brand"] = "Samsung"
        recomm.append(curr_recomm)
    return recomm

data = load_data("D:\desktop\Data Science Learning\Data-Science-learning\jsonfile\store_data.json")
data = clean_data(data)
print(data)
print(avg_rating(data))
print(percentage_poor_rating(data))
print(recommendation(data))