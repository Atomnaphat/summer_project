import cv2

# เลือกวิธีการเชื่อมต่อกับกล้อง
# ถ้าใช้กล้องในเครือข่าย (IP Camera) ใช้ rtsp หรือ http
# ถ้าใช้กล้องในเครื่อง (Webcam) ใช้ตัวเลข 0
# หากมีกล้องหลายตัวสามารถใส่ตัวเลขตามลำดับ เช่น 1, 2, 3, ...
camera_source = "rtsp://your_ip_address/your_stream_path"  # หรือ "http://your_ip_address/video"
# ถ้าใช้กล้องในเครื่อง (Webcam)
# camera_source = 0

# เชื่อมต่อกับกล้อง
cap = cv2.VideoCapture(camera_source)

# ตรวจสอบว่าเชื่อมต่อกับกล้องได้หรือไม่
if not cap.isOpened():
    print("ไม่สามารถเชื่อมต่อกับกล้องได้")
    exit()

# วนลูปอ่านภาพจากกล้องและแสดงผล
while True:
    ret, frame = cap.read()

    # ถ้าอ่านภาพไม่ได้ (เช่นกล้องถูกปิด) ให้ออกจากโปรแกรม
    if not ret:
        print("ไม่สามารถอ่านภาพได้")
        break

    # แสดงภาพ
    cv2.imshow('Camera', frame)

    # หากกดปุ่ม 'q' ให้ออกจากโปรแกรม
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# คืนทรัพยากร
cap.release()
cv2.destroyAllWindows()
