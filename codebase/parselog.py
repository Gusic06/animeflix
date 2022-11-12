def parse_log(logFile):

    '''
    function to parse log file
    '''
    
    anime = {}
    anime_last = {}
    names = []


    with open(logFile, "r") as file:
        for line in file.readlines():
            p = line.strip("\n") #Please for the love of god never name your variables "s" or "p" because I have no fucking clue what the hell they are for

            if len(p)>1:
                s = p.split(" ")
                name = s[2]
                name = name.replace(":","")
                names.append(name)
                episode_watched = s[-1].split("-")[-1].split(":")[0]
                last_episode = s[-1].split("-")[-1].split(":")[1]

                if episode_watched != last_episode:
                    anime[name] = episode_watched
                    anime_last[name] = last_episode
                else:
                    anime[name] = "finished"
    file.close()

    #delete duplicates if any
    duplicates = set(names)
    names = list(duplicates)

    #delete already finished anime
    for finishedAnime in names:
        if anime[finishedAnime] == "finished":
            names.remove(finishedAnime)

    return anime,anime_last,names

if __name__ == "__main__":
    parse_log()
