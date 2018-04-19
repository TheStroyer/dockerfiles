#####################################################################################
#                                                                                   #
#  Script to                                                        #
#                                                                                   #
#  Usage :                 # 
#                                                                                   #
#####################################################################################

def setProfile():

	AdminTask.importWasprofile('[-archive /home/was/profile.car]')
	AdminConfig.save()

setProfile()	