import random
import requests

finish_api = "https://cat-match.easygame2021.com/sheep/v1/game/game_over?rank_score=1&rank_state={}&rank_time={}&rank_role=1&skin=1"

t = "---Your cookies---"
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.27(0x18001b36) NetType/WIFI Language/zh_HK"
done_time = random.randint(360, 4000)
done_count = 1

request_header = {
    "Host": "cat-match.easygame2021.com",
    "User-Agent": user_agent,
    "t": t
}

def done(rank_state, rank_time):
    res = requests.get(finish_api.format(rank_state, rank_time), headers=request_header)
    if res.json()["err_code"] == 0:
        pass
    else:
        print(res.json())

for i in range(done_count):
    print("The first {} Rank".format(i+1))
    done(1, done_time)
    print("The first {} time done".format(i+1))
print("All done!!!")
