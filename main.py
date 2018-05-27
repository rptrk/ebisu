#!/usr/bin/env python
# coding: UTF-8

import argparse
import signal

from src.factory import BotFactory

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This is trading script on bitmex")
    parser.add_argument("--test",     default=False,   action="store_true")
    parser.add_argument("--stub",     default=False,   action="store_true")
    parser.add_argument("--demo",     default=False,   action="store_true")
    parser.add_argument("--strategy", default="doten")
    args = parser.parse_args()

    bot = BotFactory.create(args.strategy, demo=args.demo, stub=args.stub, test=args.test)
    bot.run()

    if not args.test:
        signal.signal(signal.SIGINT, lambda x, y: bot.close())
        while True:
            pass
