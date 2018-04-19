FROM ibmcom/websphere-traditional:9.0.0.7-install

COPY /profile/profile.car /home/was

COPY /scripts /work