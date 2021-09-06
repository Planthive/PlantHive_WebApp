from pymongo import MongoClient

if __name__ == '__main__':
client= MongoClient('localhost',27017)
db=client['game']
collection=db['test']


# Sample code for JSON input
def output(request):
    # this finds our json files
    path_to_json = 'C:\\JSON'
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

    client= MongoClient('localhost',27017)
    db=client["game"]
    collection=db["test"]

    # we need both the json and an index number so use enumerate()
    for index, js in enumerate(json_files):
        with open(os.path.join(path_to_json, js)) as json_file:
            json_data = json.load(json_file)

            collection.insert_one(json_data)

            client.close()

    for filename in os.listdir(path_to_json):
        file_path = os.path.join(path_to_json, filename)
        os.remove(file_path)
    return render(request, 'local_home/home.html',{'json_files': json_files} )
