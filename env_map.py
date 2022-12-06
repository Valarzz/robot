import cv2
import numpy as np
from sklearn.preprocessing import normalize


class grid:
    def __init__(self, w, h, l):
        self.w = w
        self.h = h
        self.r = 100
        self.grid_shape = l
        img = np.ones([w, h, 3])
        self.gr = self.draw_grid(img, l)
        self.robot_observe_color = np.array([0., 0., 0.5, 0.5])
        self.robot_obstacle_color = np.array([0., 0., 0., 0.])
        self.robot_pos_map = np.zeros([self.w, self.h, 4])
        self.discrete_map = np.zeros(l)  # -1:obstacle, 0:unknown, 1:known
        self.gen_true_map()

    def draw_grid(self, img, grid_shape, color=(1, 0, 0), thickness=1):  #
        h, w, _ = img.shape
        rows, cols = grid_shape
        dy, dx = h / rows, w / cols
        # draw vertical lines
        for x in np.linspace(start=dx, stop=w - dx, num=cols - 1):
            x = int(round(x))
            cv2.line(img, (x, 0), (x, h), color=color, thickness=thickness)
        # draw horizontal lines
        for y in np.linspace(start=dy, stop=h - dy, num=rows - 1):
            y = int(round(y))
            cv2.line(img, (0, y), (w, y), color=color, thickness=thickness)
        a = np.zeros([self.w, self.h, 1])
        img = np.concatenate((img, a), axis=2)
        return img

    def robot_move(self, pos, yaw):
        # self.robot_pos_map = np.zeros([self.w, self.h, 4])
        for x in range(-self.r, self.r+1):
            for y in range(-self.r, self.r+1):
                if x**2+y**2 < self.r**2:
                    loc = np.array([x, y])  # relative
                    lx = pos[0]+x           # global
                    ly = pos[1]+y
                    if self.w > lx > 0 and self.h > ly > 0:
                        # if np.dot(normalize(loc[:, np.newaxis], axis=0).ravel(), np.array([np.cos(yaw), np.sin(yaw)]))>0.5:
                        if np.dot(normalize(loc[:, np.newaxis], axis=0).ravel(), yaw)>0.8:
                            self.robot_pos_map[lx, ly] = self.robot_observe_color
                            self.discrete_map[int(lx//(self.w/self.grid_shape[0]))][int(ly//(self.h/self.grid_shape[1]))] = 1

    def gen_map(self):
        m = self.robot_pos_map[:, :, -1] - self.gr[:, :, -1]
        out = self.robot_pos_map[:, :, :-1] * m[:, :, np.newaxis] + self.gr[:, :, :-1] * (1-m[:, :, np.newaxis])
        f = self.print_frontier()
        for x in range(len(f)):
            for y in range(len(f[0])):
                if f[x][y] == 1:
                    out = self.print_grid([x, y], np.array([0.8, 0.8, 0.8]), out)
        self.robot_pos_map = np.zeros([self.w, self.h, 4])
        for i in range(len(self.true_map)):
            for j in range(len(self.true_map[0])):
                if self.true_map[i][j]:
                    self.print_grid([i, j], self.robot_obstacle_color, out)
        return out

    def print_grid(self, pos, color, mm):
        x0 = pos[0] * int(self.w/self.grid_shape[0])
        y0 = pos[1] * int(self.h/self.grid_shape[1])
        m = mm[x0:x0+int(self.w/self.grid_shape[0]), y0:y0+int(self.h/self.grid_shape[1])]
        mm[x0:x0+int(self.w/self.grid_shape[0]), y0:y0+int(self.h/self.grid_shape[1])] = color * 0.5 + m * 0.5
        return mm

    def print_frontier(self):
        frontier = self.discrete_map.copy()
        for x in range(len(frontier)):
            for y in range(len(frontier[0])):
                if frontier[x][y] == 1:
                    if not self.test_f([x, y]):  # truely frontier
                        frontier[x][y] = 0
        return frontier

    def test_f(self, pos):
        x, y = pos
        temp = []
        if x-1>-1:
            temp.append(self.discrete_map[x-1][y])
        if x+1<self.grid_shape[0]:
            temp.append(self.discrete_map[x+1][y])
        if y-1>-1:
            temp.append(self.discrete_map[x][y-1])
        if y+1<self.grid_shape[1]:
            temp.append(self.discrete_map[x][y+1])
        temp = np.array(temp)
        if (temp==np.zeros_like(temp)).any():
            return True
        else:
            return False

    def gen_true_map(self):
        self.true_map =[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        self.true_map = np.array(self.true_map)





