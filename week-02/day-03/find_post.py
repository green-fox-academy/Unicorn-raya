import json
json_file_name = "C:\\Users\\Ray_Zhang\\greenfox\\Unicorn-raya\\week-02\\day-03\\post.json"
def find_most_popular_comments(json_file_name):
    file = open(json_file_name,encoding = 'utf-8')
    contents = json.load(file)
    max_number = -1
    content_base_on_maxnumber = ""
    for content in contents:
        if isinstance(content["comments"],list): #in case of null comment
            current_sum_of_like_count = 0
            for items in content["comments"]:
               current_sum_of_like_count += int(items["like_count"])
            if max_number < current_sum_of_like_count:
                max_number = current_sum_of_like_count
                content_base_on_maxnumber = content["content"]
    return content_base_on_maxnumber
        
print(find_most_popular_comments(json_file_name))



