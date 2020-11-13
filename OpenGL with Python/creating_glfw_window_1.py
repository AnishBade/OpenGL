import glfw

class Window:
    def __init__(self,width:int,height:int,title:str):
        if not glfw.init():
            raise Exception("Cannot initialize glfw")
        self.win=glfw.create_window(width,height,title,None,None)

        if not self.win:
            glfw.terminate()
            raise Exception("glfw window cannot be created")
        glfw.set_window_pos(self.win,500,80)
        glfw.make_context_current(self.win)

    def main_loop(self):
        while not glfw.window_should_close(self.win):
            glfw.poll_events()
            glfw.swap_buffers(self.win)

        glfw.terminate()
if __name__=="__main__":
    win=Window(1200,800,'My OpenGL Window')
    win.main_loop()

