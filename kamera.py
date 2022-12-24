# import librari opencv
import cv2


# menemukan objek videocapture
vid = cv2.VideoCapture(0)

while(True):
	
	# menangkap frame daari videocapture
	# per frame
	ret, frame = vid.read()

	# menampilkan hasil dari frame yang tertangkap
	cv2.imshow('frame', frame)
	
	# tombol'q' digunakan untuk
	# keluar (menutup) kamera
	# desired button of your choice
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
