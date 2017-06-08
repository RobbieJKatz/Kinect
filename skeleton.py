from openni import *
import numpy as np
import cv2



#cv2.waitKey(0)
#cv2.destroyAllWindows()


ctx = Context()
ctx.init()

# Create the user generator
user = UserGenerator()
user.create(ctx)
pose_to_use = 'Psi'


# Obtain the skeleton & pose detection capabilities
skel_cap = user.skeleton_cap
pose_cap = user.pose_detection_cap

# Declare the callbacks
def new_user(src, id):
    print "1/4 User {} detected. Looking for pose..." .format(id)
    pose_cap.start_detection(pose_to_use, id)

def pose_detected(src, pose, id):
    print "2/4 Detected pose {} on user {}. Requesting calibration..." .format(pose,id)
    pose_cap.stop_detection(id)
    skel_cap.request_calibration(id, True)

def calibration_start(src, id):
    print "3/4 Calibration started for user {}." .format(id)

def calibration_complete(src, id, status):
    if status == CALIBRATION_STATUS_OK:
        print "4/4 User {} calibrated successfully! Starting to track." .format(id)
        skel_cap.start_tracking(id)
    else:
        print "ERR User {} failed to calibrate. Restarting process." .format(id)
        new_user(user, id)

def lost_user(src, id):
    print "--- User {} lost." .format(id)

# Register them
user.register_user_cb(new_user, lost_user)
pose_cap.register_pose_detected_cb(pose_detected)
skel_cap.register_c_start_cb(calibration_start)
skel_cap.register_c_complete_cb(calibration_complete)

# Set the profile
skel_cap.set_profile(SKEL_PROFILE_ALL)

# Start generating
ctx.start_generating_all()
print "0/4 Starting to detect users. Press Ctrl-C to exit."
if cv2.waitKey(1) & 0xFF == ord('q'):
	print 'a'
while True:
    frame = np.zeros((800,1400,3),np.uint8)
    # Update to next frame
    ctx.wait_and_update_all()


	
    # Extract head position of each tracked user
    for id in user.users:
        if skel_cap.is_tracking(id):
            head = skel_cap.get_joint_position(id, SKEL_HEAD)
            rhand = skel_cap.get_joint_position(id, SKEL_RIGHT_HAND)
	    lhand = skel_cap.get_joint_position(id, SKEL_LEFT_HAND)
	    rfoot = skel_cap.get_joint_position(id, SKEL_RIGHT_FOOT)
            lfoot = skel_cap.get_joint_position(id, SKEL_LEFT_FOOT)
  	    torso = skel_cap.get_joint_position(id, SKEL_TORSO)
  	    relbow = skel_cap.get_joint_position(id, SKEL_RIGHT_ELBOW)
  	    lelbow = skel_cap.get_joint_position(id, SKEL_LEFT_ELBOW)
            rknee= skel_cap.get_joint_position(id, SKEL_RIGHT_KNEE)
            lknee= skel_cap.get_joint_position(id, SKEL_LEFT_KNEE)
            lshoulder= skel_cap.get_joint_position(id, SKEL_LEFT_SHOULDER)
            rshoulder= skel_cap.get_joint_position(id, SKEL_RIGHT_SHOULDER)
            neck= skel_cap.get_joint_position(id, SKEL_NECK)
            rhip= skel_cap.get_joint_position(id, SKEL_RIGHT_HIP)
	    lhip= skel_cap.get_joint_position(id, SKEL_LEFT_HIP)
            
            headX = 600-int(head.point[0]/4)
            headY = 400-int(head.point[1]/4)
	    headZ = int(64-head.point[2]/60)
            if(headZ < 0):
            	headZ =0

            torsoX = 600-int(torso.point[0]/4)
            torsoY = 400-int(torso.point[1]/4)
	    torsoZ = int(64-torso.point[2]/60)
            if(torsoZ < 0):
            	torsoZ =0

            rhipX = 600-int(rhip.point[0]/4)
            rhipY = 400-int(rhip.point[1]/4)
	    rhipZ = int(64-rhip.point[2]/60)
            if(rhipZ < 0):
            	rhipZ =0
            lhipX = 600-int(lhip.point[0]/4)
            lhipY = 400-int(lhip.point[1]/4)
	    lhipZ = int(64-lhip.point[2]/60)
            if(lhipZ < 0):
            	lhipZ =0

            lkneeX= 600-int(lknee.point[0]/4)
            lkneeY = 400-int(lknee.point[1]/4)
	    lkneeZ = int(64-lknee.point[2]/60)
            if(lkneeZ < 0):
            	lkneeZ =0
            rkneeX= 600-int(rknee.point[0]/4)
            rkneeY = 400-int(rknee.point[1]/4)
	    rkneeZ = int(64-rknee.point[2]/60)
            if(rkneeZ < 0):
            	rkneeZ =0
            neckX= 600-int(neck.point[0]/4)
            neckY = 400-int(neck.point[1]/4)
	    neckZ = int(64-neck.point[2]/60)
            if(neckZ < 0):
            	neckZ =0
            rshoulderX= 600-int(rshoulder.point[0]/4)
            rshoulderY = 400-int(rshoulder.point[1]/4)
	    rshoulderZ = int(64-rshoulder.point[2]/60)
            if(rshoulderZ < 0):
            	rshoulderZ =0
            lshoulderX= 600-int(lshoulder.point[0]/4)
            lshoulderY = 400-int(lshoulder.point[1]/4)
	    lshoulderZ = int(64-lshoulder.point[2]/60)
            if(lshoulderZ < 0):
            	lshoulderZ =0

            rhandX = 600-int(rhand.point[0]/4)
            rhandY = 400-int(rhand.point[1]/4)
	    rhandZ = int(64-rhand.point[2]/60)
            if(rhandZ < 0):
            	rhandZ =0
            lhandX = 600-int(lhand.point[0]/4)
            lhandY = 400-int(lhand.point[1]/4)
	    lhandZ = int(64-lhand.point[2]/60)
            if(lhandZ < 0):
            	lhandZ =0

	    lelbowX = 600-int(lelbow.point[0]/4)
            lelbowY = 400-int(lelbow.point[1]/4)
	    lelbowZ = int(64-lelbow.point[2]/60)
            if(lelbowZ < 0):
            	lelbowZ =0	   	    
	    relbowX = 600-int(relbow.point[0]/4)
            relbowY = 400-int(relbow.point[1]/4)
	    relbowZ = int(64-relbow.point[2]/60)
            if(relbowZ < 0):
            	relbowZ =0

            rfootX = 600-int(rfoot.point[0]/4)
            rfootY = 400-int(rfoot.point[1]/4)
	    rfootZ = int(64-rfoot.point[2]/60)
            if(rfootZ < 0):
            	rfootZ =0
            lfootX = 600-int(lfoot.point[0]/4)
            lfootY = 400-int(lfoot.point[1]/4)
	    lfootZ = int(64-lfoot.point[2]/60)	   
            if(lfootZ < 0):
            	lfootZ =0
            cv2.line(frame,(headX,headY),(headX,headY),(120,120,40),headZ*3)
	    cv2.line(frame,(headX,headY),(neckX,neckY),(120,120,40),neckZ)
	    cv2.line(frame,(lelbowX,lelbowY),(lshoulderX,lshoulderY),(120,120,40),lelbowZ)
	    cv2.line(frame,(relbowX,relbowY),(rshoulderX,rshoulderY),(120,120,40),relbowZ)
	    cv2.line(frame,(neckX,neckY),(lshoulderX,lshoulderY),(120,120,40),lshoulderZ)
	    cv2.line(frame,(neckX,neckY),(rshoulderX,rshoulderY),(120,120,40),rshoulderZ)
            cv2.line(frame,(neckX,neckY),(torsoX,torsoY),(120,120,40),torsoZ)
	    cv2.line(frame,(lelbowX,lelbowY),(lhandX,lhandY),(120,120,40),lhandZ)
	    cv2.line(frame,(relbowX,relbowY),(rhandX,rhandY),(120,120,40),rhandZ)
	    cv2.line(frame,(lfootX,lfootY),(lkneeX,lkneeY),(120,120,40),lfootZ)
	    cv2.line(frame,(rfootX,rfootY),(rkneeX,rkneeY),(120,120,40),rfootZ)
	    cv2.line(frame,(lkneeX,lkneeY),(lhipX,lhipY),(120,120,40),lkneeZ)
	    cv2.line(frame,(rkneeX,rkneeY),(rhipX,rhipY),(120,120,40),rkneeZ)
	    cv2.line(frame,(torsoX,torsoY),(rhipX,rhipY),(120,120,40),torsoZ)
	    cv2.line(frame,(torsoX,torsoY),(lhipX,lhipY),(120,120,40),torsoZ)

        #    print "  {}: head at ({loc[0]}, {loc[1]}, {loc[2]}) [{conf}]" .format(id, loc=rARM.point, conf=rARM.confidence)	

    cv2.imshow("image", frame)	
    if cv2.waitKey(1) & 0xFF == ord('q'):
        	break
