import pickle

d = {
    "name":"zkp",
    "role":"police",
    "blood":76,
    "weapon":"AK47"
}

alive_players = ["alex", "jack", "rain"]

d_dump = pickle.dumps(d) # 序列化
print(pickle.loads(d_dump)) # 反序列化

f = open("game.pkl","wb")
# f.write(d_dump)
# pickle.dump(d,f)
# pickle.dump(alive_players,f)

print(pickle.load(f))