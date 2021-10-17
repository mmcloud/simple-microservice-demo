FROM tomcat:alpine

RUN ["rm", "-fr", "/usr/local/tomcat/webapps/ROOT"]
COPY ./build/libs/docker-tomcat-java-example.war /usr/local/tomcat/webapps/ROOT.war