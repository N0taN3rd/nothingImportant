from wb_cdx_shared import *


def cdx_server(args=None):  # pragma: no cover
    CdxCli(args=args,
           default_port=8080,
           desc='pywb CDX Index Server').run()


if __name__ == "__main__":
    cdx_server()
