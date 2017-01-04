#!/usr/bin/env bash

here=$(pwd)

clean () {
  if [[ -d "build" ]]; then
    echo cleaning build
    rm -rf build
  fi

  if [[ -d "dist"  ]]; then
    echo cleaning dist
    rm -rf dist
  fi

  if [[ -d "mypwb/__pycache__"  ]]; then
    echo cleaning pycache
    rm -rf mypwb/__pycache__
  fi
}

clean

if [[ -d "dist" ]]; then
  rm -rf dist
fi

pyinstaller wayback.spec
pyinstaller wb-manager.spec
pyinstaller cdx-indexer.spec
pyinstaller cdx-server.spec


mkdir dist/pywb
cp -r dist/wayback/* dist/pywb
cp dist/cdxIndexer/cdx-indexer dist/pywb
cp dist/cdxServer/cdx-server dist/pywb
cp dist/wbMan/wb-manager dist/pywb

chmod a+rwx runPywb.sh
cp runPywb.sh dist/pywb
