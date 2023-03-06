# print(dir(str))

input_dict = {'image_id': 4223, 'image_title': 'my_cat'}


def image_info(dict):

    if ('image_title' not in dict):
        raise KeyError("not key 'image_title' in dict")

    if ('image_id' not in dict):
        raise KeyError("not key 'image_id' in dict")
    return (f"Image {input_dict['image_title']} has {input_dict['image_id']} ID")


try:
    print(image_info(input_dict))
except Exception as e:
    print(e)
