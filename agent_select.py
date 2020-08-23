import configparser
config1 = configparser.ConfigParser()

character = {}


def read_config():
    configfilepath = 'config.ini'
    config1.read(configfilepath)
    for i in range(12):
        character[str(i)] = config1.get('main', str(i + 1))
        #print(character)

    for i in character:
        if character[str(i)] == "1":
            character[str(i)] = "Brimstone"
        if character[str(i)] == "2":
            character[str(i)] = "Cypher"
        if character[str(i)] == "3":
            character[str(i)] = "Jett"
        if character[str(i)] == "4":
            character[str(i)] = "Omen"
        if character[str(i)] == "5":
            character[str(i)] = "Pheonix"
        if character[str(i)] == "6":
            character[str(i)] = "Sage"
        if character[str(i)] == "7":
            character[str(i)] = "Sova"
        if character[str(i)] == "8":
            character[str(i)] = "Breach"
        if character[str(i)] == "9":
            character[str(i)] = "Killjoy"
        if character[str(i)] == "10":
            character[str(i)] = "Raze"
        if character[str(i)] == "11":
            character[str(i)] = "Reyna"
        if character[str(i)] == "12":
            character[str(i)] = "Viper"
    print("Converting done!")

    return character


read_config()


# print(character)


print("Welcome to the Agent Select!")
print("\n")
print("Choose YOUR Agent")
print("\n")
print("These are the numbers. Every number stands for an agent!")

for i in character:
    a = int(i) + 1
    print(str(a) + " = " + character[i])

agent = input("Which agent do you want to play? [enter a number]")


config2 = configparser.ConfigParser()


config2['agent'] = {'selected': agent}


configfile2 = open('agent_config.ini', 'w')
config2.write(configfile2)
