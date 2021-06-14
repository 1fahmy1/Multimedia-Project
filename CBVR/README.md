# CBVR

cd ${PROJECT_FOLDER}

# On root folder run file server to fetch video files
python -m SimpleHTTPServer 3333
/ python -m http.server 3333

# Run pyhon api server
python api.py

# Run Webapp
cd webapp
source ng.sh
ng serve --proxy-config proxyconf.json
/ npm run ng <command>
/ npm run ng serve --proxy-config proxyconf.json
