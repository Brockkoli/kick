FROM jenkins/jenkins:lts

USER root

# Update and install Python, pip, and python3-venv
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    ln -s /usr/bin/python3 /usr/bin/python

# Install sudo
RUN apt-get update && \
    apt-get install -y sudo

# Give the jenkins user passwordless sudo privileges
RUN echo "jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

USER jenkins
