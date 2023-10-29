def main():
    discord_name = [input() for _ in range(5)]
    name = []
    for i in range(len(discord_name)):
        remove_tag = discord_name[i].rsplit('#')
        name.append(remove_tag[0])
        print(name[i]) 
main()

def few():
    member = [input() for _ in range(5)]
    member = [x.split("#")[0] for x in member]
    print(*member, sep="\n")