
import cx_Freeze 

executables = [
        #                   name of your game script
        cx_Freeze.Executable("FACE_EYES_SMILE_DETECTION.py") 
] 
cx_Freeze.setup( 
        name = "Face, Eyes & Smile Detection",
        version='0.1',
        options= {"build_exe": {"packages":["numpy", 'cv2'],
                                "include_files":["eye.xml", "smile.xml", "frontalface_default.xml"]}},
        description = "Must have a web-cam to see your face!!!", 
        executables = executables)

