import requests

def bot(msg):
        url = "https://api.telegram.org/bot1171824656:AAHC7VsK9iJOLmnkbR5vQA0aGAkmLJNUHlI/sendMessage?chat_id=438462561&text="+msg
            
        payload = {
                "UrlBox":url,
                "AgentList":"Mozilla Firefox",
                "VersionsList":"HTTP/1.1",
                "MethodList":"POST"

        }

        r = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",payload)
        return r.text


bot("")