from wb_cdx_shared import *


def wayback(args=None):
    WaybackCli(args=args,
               default_port=8080,
               desc='pywb Wayback Web Archive Replay').run()


if __name__ == '__main__':
    wayback()
