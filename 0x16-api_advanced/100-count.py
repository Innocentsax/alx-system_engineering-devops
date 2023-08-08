import requests

def count_words(subreddit, word_list, after=None, word_counts=None):
    if word_counts is None:
        word_counts = {}

    if after is None:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'

    headers = {'User-Agent': 'Reddit API Example'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("Invalid subreddit or other error occurred.")
        return

    data = response.json()['data']
    posts = data['children']

    for post in posts:
        title = post['data']['title']
        for word in word_list:
            word_lower = word.lower()
            title_lower = title.lower()
            if title_lower.count(word_lower):
                if word_lower in word_counts:
                    word_counts[word_lower] += title_lower.count(word_lower)
                else:
                    word_counts[word_lower] = title_lower.count(word_lower)

    after = data['after']
    if after is not None:
        count_words(subreddit, word_list, after, word_counts)
    else:
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_counts:
            print(f"{word}: {count}")

# Call the function with the subreddit and a list of keywords
#count_words('python', ['python', 'java', 'javascript'])
