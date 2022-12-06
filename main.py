import cv2
import numpy as np
import time
import imageio

from env_map import grid
from robot import robot


r = 10


# def robot(pos, yaw, grid):
#     for x in
#     norm1 = x / np.linalg.norm(x)


if __name__ == '__main__':
    g = grid(1024, 1024, [20, 20])
    print("start")
    imgs = []
    i = 100
    j = 0
    k = 0
    rob1 = robot(512, 512, 30)
    rob2 = robot(256, 512, 10)

    while True:
        # if i > 1024:
        #     i = 100
        # else:
        #     i += 30
        # g.robot_move([800, i], np.pi/8)

        rob1.move([1024, 1024])
        rob2.move([0, 0])
        g.robot_move([round(rob1.x), round(rob1.y)], np.pi / 8)
        g.robot_move([round(rob2.x), round(rob2.y)], np.pi / 8)

        m = g.gen_map()
        m = np.rot90(m, 1)

        frame = (m.copy()*255).astype(np.uint8)
        # cv2.imshow('image', frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        #     break
        imgs.append(frame)
        print(str(len(imgs))+"\t", end="")
        if len(imgs) > 5:
            break
    gif = imageio.mimsave('result.gif', imgs, 'GIF', duration=0.1)
    print("\ndone")


    # while True:
    #     cv2.imshow('image', imgs[j % len(imgs)])
    #     # print(str(j)+"\t", end="")
    #     print(str(j))
    #     j += 1
    #     time.sleep(0.1)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #       cv2.destroyAllWindows()
    #       break


