from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

search_queue = deque()
search_queue += graph['you']
searched = []


def search(search_queue):
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if presonal_quite(person):
                print(person + ' is quite!')
            else:
                search_queue += graph[person]

            searched.append(person)

    return False


def presonal_quite(name):
    return name[-1] == 'm'


if __name__ == '__main__':
    search(search_queue)
