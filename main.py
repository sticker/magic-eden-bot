import os
import json
#import helper functions for magiceden
import magiceden
#import helper functions for monkeylabs



if __name__ == "__main__":
    def getConfig():
            configFile = open("config.json", 'r')
            return list(json.load(configFile).values())

    #gets config
    config = getConfig()

    #if windows True, else False (mac, linux)
    isWindows = True if os.name == 'nt' else False

    #if mint on magiceden.io
    if "magiceden.io" in config[0]:
        print("Found magiceden.io link")
        magiceden.mint(config, isWindows)

    #if platform not supported
    else:
        print("Could not recognize link")

