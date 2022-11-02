
import requests
from dict_json import open_file
def get_course_info(course_id):
    url=f"https://siigosas.udemy.com/api-2.0/courses/{course_id}/subscriber-curriculum-items/?page_size=1400&fields[lecture]=title,object_index,is_published,sort_order,created,asset,supplementary_assets,is_free&fields[quiz]=title,object_index,is_published,sort_order,type&fields[practice]=title,object_index,is_published,sort_order&fields[chapter]=title,object_index,is_published,sort_order&fields[asset]=title,filename,asset_type,status,time_estimation,is_external&caching_intent=True"

    headers = open_file("./headers.json")
   
    response = requests.get(url,headers=headers)
    if 299>= response.status_code >= 200:
        try:
            return response.json()
        except:
            return response.text
    return response.text
