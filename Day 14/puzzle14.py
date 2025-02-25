import tkinter as tk
    def robots_update(array,tall,wide):
        for i in array:
            i[0] = (i[0] + i[2])%tall
            i[1] = (i[1] + i[3])%wide

    def robots_update_back(array,tall,wide):
        for i in array:
            i[0] = (i[0] - i[2])%tall
            i[1] = (i[1] - i[3])%wide

    def safety(array,tall,wide):
        lt,rt,lb,rb = 0,0,0,0
        for i in array:
            if i[0] < (tall-1)/2 and i[1] < (wide-1)/2: lt += 1
            elif i[0] < (tall-1)/2 and i[1] > (wide-1)/2: rt += 1
            elif i[0] > (tall-1)/2 and i[1] > (wide-1)/2: rb += 1
            elif i[0] > (tall-1)/2 and i[1] < (wide-1)/2: lb += 1
        print(lt*rt*lb*rb)

    def part1(array,tall,wide):
        for i in range(100): robots_update(array, tall, wide)
        safety(array, tall, wide)

    def map_update(array, tall, wide):
        map = []
        for i in range(tall):
            line = ""
            for j in range(wide):
                field_status = 0
                for k in array:
                    if i == k[0] and j == k[1]: field_status = 1
                line += str(field_status) if field_status > 0 else " "
            map.append(line)
        return map

    class MapApp:
        def __init__(self, root, tall, wide, robots, cell_size=6):
            self.root = root
            self.tall = tall
            self.wide = wide
            self.robots = robots
            self.cell_size = cell_size
            self.update_count = 0
            self.auto_update = False

            # making canvas to paint map
            self.canvas = tk.Canvas(root, width=self.wide * self.cell_size, height=self.tall * self.cell_size,
                                    bg="white")
            self.canvas.grid(row=0, column=0, columnspan=6)

            # 1/100/1000/-1 buttons
            self.update_button = tk.Button(root, text="Plus 1 sec",font=("Arial", 8,) ,command=lambda: self.update_map(1))
            self.update_button.grid(row=1, column=0)

            self.update_button = tk.Button(root, text="Plus 100 sec", font=("Arial", 8,),command=lambda: self.update_map(2))
            self.update_button.grid(row=1, column=1)

            self.update_button = tk.Button(root, text="Plus 1000 sec", font=("Arial", 8,),command=lambda: self.update_map(3))
            self.update_button.grid(row=1, column=2)

            self.update_button = tk.Button(root, text="Minus 1 sec",font=("Arial", 8) ,command=lambda: self.update_map(4))
            self.update_button.grid(row=1, column=3)

            # auto
            self.auto_button = tk.Button(root, text="AUTO", command=self.toggle_auto_update)
            self.auto_button.grid(row=1, column=5)

            self.counter_label = tk.Label(root, text=f"Seconds: {self.update_count}", font=("Arial", 12))
            self.counter_label.grid(row=1, column=4)

        def update_map(self,id):
            # position of robots
            if id == 1: robots_update(self.robots, self.tall, self.wide)
            elif id == 2:
                for i in range(100): robots_update(self.robots, self.tall, self.wide)
            elif id == 3:
                for i in range(1000): robots_update(self.robots, self.tall, self.wide)
            else: robots_update_back(self.robots, self.tall, self.wide)

            grid = map_update(self.robots, self.tall, self.wide)

            self.canvas.delete("all")

            for i in range(self.tall):
                for j in range(self.wide):
                    x1 = j * self.cell_size
                    y1 = i * self.cell_size
                    x2 = x1 + self.cell_size
                    y2 = y1 + self.cell_size
                    if grid[i][j] != " ":
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="")
                    else:
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="")

            if id == 1: self.update_count += 1
            elif id == 2: self.update_count += 100
            elif id == 3: self.update_count += 1000
            else: self.update_count -= 1
            self.counter_label.config(text=f"Seconds: {self.update_count}")

        def toggle_auto_update(self):
            self.auto_update = not self.auto_update
            if self.auto_update:
                self.auto_button.config(text="AUTO")
                self.run_auto_update()
            else:
                self.auto_button.config(text="AUTO")

        def run_auto_update(self):
            if self.auto_update:
                self.update_map(1)
                self.root.after(20, self.run_auto_update)

    with open('text14.txt') as file:
        arr = [l.replace(",", " ").split() for l in file]

    robots = []
    robots_copy = []
    for i in range(len(arr)):
        robots.append([int(arr[i][1]),int(arr[i][0][2:]),int(arr[i][3]),int(arr[i][2][2:])])
        robots_copy.append([int(arr[i][1]),int(arr[i][0][2:]),int(arr[i][3]),int(arr[i][2][2:])])

    tall = 103
    wide = 101

    #PART1
    part1(robots,103,101)

    #PART2 #8280
    root = tk.Tk()
    root.title("Map")
    app = MapApp(root, tall, wide, robots_copy, cell_size=6)
    root.mainloop()
