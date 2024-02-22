import time
import rotatescreen as rs

def rotate_primary_display():
    pd = rs.get_primary_display()
    angles = [90, 180, 270, 0]

    for i in range(5):
        while True:
            for x in angles:
                pd.rotate_to(x)
                time.sleep(0.1) # Adjust the sleep duration as needed


if __name__ == "__main__":
    rotate_primary_display()

#The code is for educational purposes of course.
