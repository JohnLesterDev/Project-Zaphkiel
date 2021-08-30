import Network

animList = [
    'Aaaaaaaaaa',
    'aAaaaaaaaa',
    'aaAaaaaaaa',
    'aaaAaaaaaa',
    'aaaaAaaaaa',
    'aaaaaAaaaa',
    'aaaaaaAaaa',
    'aaaaaaaAaa',
    'aaaaaaaaAa',
    'aaaaaaaaaA',
    'aaaaaaaaaa']

finished = False

thread = Network.threading.Thread(target=Network.animate, args=(animList, finished))
thread.start()


finished = True
