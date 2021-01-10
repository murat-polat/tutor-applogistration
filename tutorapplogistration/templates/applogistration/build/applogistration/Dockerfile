FROM debian

LABEL MAINTAINER=MP
RUN apt-get update && apt-get -y upgrade

# Installing python packages with nano, vim and telnet
RUN apt-get -y install python3-dev default-libmysqlclient-dev build-essential nano vim telnet

RUN apt-get -y install python3-pip  git curl 
RUN pip3 install mysqlclient

# Installing node and React dependencies
RUN apt-get -y install node-gyp nodejs npm && npm install npm@latest -g

# Making directory
RUN  mkdir /openedx /openedx/data

####### Here must be your fork ad your custom branch(Don't forget to edit ".ENV.development" and "package.json" in your branch :) #########
RUN git clone -b solo https://github.com/murat-polat/frontend-app-logistration/ /openedx/applogistration

WORKDIR /openedx/applogistration/

RUN cd /openedx/applogistration

## Installing and building app
RUN npm install && npm run build 

EXPOSE 1999 


CMD ["npm", "start" ]