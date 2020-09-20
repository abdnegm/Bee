import json
import os.path
import pickle
import time
import urllib.request

def url_open(url):
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    return data

def picklee(obj, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(obj, f)
    return

def unpickle(file_name):
    with open(file_name, 'rb') as f:
        unpickled = pickle.load(f)
    return unpickled

def download_dict(words, save_folder):
    API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

    num_words_skipped = 0
    num_words_errored = 0
    num_words_downloaded = 0
    for word in words:
        file_name = "{}/{}.pickle".format(save_folder, word)
        if os.path.exists(file_name):
            num_words_skipped += 1
            print(word + " already exists. skipping")
        else:
            time.sleep(2) # don't spam the server as fast as possible
            url = API_URL + word
            try:
                api_result = url_open(url)
            except urllib.error.HTTPError:
                num_words_errored += 1
                print("no definitions found for the word " + word)
            except UnicodeEncodeError:
                num_words_errored += 1
                print("unicode error for the word " + word)
            else:
                num_words_downloaded += 1
                picklee(api_result, file_name)
    print("skipped " + str(num_words_skipped) + " words")
    print("errored " + str(num_words_errored) + " words")
    print("downloaded " + str(num_words_downloaded) + " words")

##########

# easy
words = unpickle("level_one_words.pickle")
save_folder = "easy"
download_dict(words, save_folder)

# medium
words = unpickle("level_two_words.pickle")
save_folder = "medium"
download_dict(words, save_folder)

# hard
words = unpickle("level_three_words.pickle")
save_folder = "hard"
download_dict(words, save_folder)
