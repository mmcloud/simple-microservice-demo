FROM tomcat:alpine

RUN ["rm", "-fr", "/usr/local/tomcat/webapps/ROOT"]
COPY ./build/libs/frontend-bakery.war /usr/local/tomcat/webapps/ROOT.war
