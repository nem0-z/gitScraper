import requests
from bs4 import BeautifulSoup

f = open("commit.sh","w")
f.write("#!/bin/bash\n\n")

# testURL = 'https://github.com/nem0-z/android_kernel_oneplus_sm8150/commits/labs'
# page = requests.get(testURL)
URL = input('Url of the commit history page on GitHub: ')
try:
    page = requests.get(URL)
    print('Connection established.')
except:
    print('Invalid URL.')
    exit()

choice = input('Do you want to pick or revert commits? ').lower()
if choice not in ['pick','revert']:
    raise ValueError('You can only pick or revert a commit.')
elif choice == 'pick':
    choice = 'cherry-pick'

limit = input(f'If you want to {choice} until a specific commit, paste in the commit SHA, otherwise press enter: ')

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('li', class_='Box-row Box-row--focus-gray mt-0 d-flex js-commits-list-item js-navigation-item js-details-container Details js-socket-channel js-updatable-content')

commits = []

for result in results:
    entry = result.get('data-url')
    commitSHA = entry.split('/')[4]
    commitMessage = result.find('a').get('aria-label').splitlines()
    if commitSHA == limit or len(limit) == 7 and commitSHA[:7] == limit:
        break
    commit = f'#{commitMessage[0]}\ngit {choice} {commitSHA} --signoff\n'
    commits.append(commit)

for commit in reversed(commits):
    f.write(commit)

print('Success!')
f.close()