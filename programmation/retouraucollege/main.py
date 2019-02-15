import os
import sys
import math
import re
import irc.client

class RetourAuCollege(irc.client.SimpleIRCClient):

    def __init__(self, server, nick, bot, port=6667):
        irc.client.SimpleIRCClient.__init__(self)
        self.bot = bot
        self.tic = 0

        self.connect(server, port, nick)

    def on_welcome(self, connection, event):
        print("[+] Connection sucess")
        connection.privmsg(self.bot, "!ep1")

    def on_privmsg(self, connection, event):
        print ("[+] From %s a %s arguments: %s" % (
		event.source,
		event.target,
		event.arguments,
        ))

        message = event.arguments[0]
        print("[+] Message: %s" % message)

        if self.tic == 0:
            i, j = (float(i) for i in re.findall('[0-9]+', message))
            res = '!ep1 -rep %.2f' % (round(math.sqrt(i) * j, 2))
            connection.privmsg(self.bot, res)

            self.tic += 1
        else:
            sys.exit(0)

def main():
    server = 'irc.root-me.org'
    port = 6667
    nick = 'Koneko'
    bot = 'Candy'

    c = RetourAuCollege(server, nick, bot, port)
    c.start()

if __name__ == "__main__":
    main()
