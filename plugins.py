#
#              AdvancedPresence
#                 by @fxcvd
#
#   main.py
#   created at 06.06.21
#   modifed at 07.06.21
#

#Connect you plugin in config file
#U can make ur plugin
#Check example

def example(title, url):
    #Advenced Presecnce call u plugin with title and url params
    #If u plugin works with github.com and url not equal github.com ur must be return None
    
    #Plugin code here...

    return {
            #all this params not requirement
            #You can return only state or state and details
            "button": {
                "label": "Open this video",
                "url": url
            },

            "state": title,
            "icon": "youtube",
            "details": "Watching YouTube"
        }

def youtube(title, url):
    if " - YouTube" in title:
        state = title.replace(" - YouTube", "")

        return {
            "button": {
                "label": "Open this video",
                "url": url
            },

            "state": state,
            "icon": "youtube",
            "details": "Watching YouTube"
        }