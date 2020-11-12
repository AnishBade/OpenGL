import glfw
from OpenGL.GL import *

def main():
    #initialize glfw
    if not glfw.init():
        return

    #create glfw window
    window=glfw.create_window(1000,800,"My OpenGL Wingow",None,None)
    
    if not window:
        glfw.terminate()
        return
    
    glfw.make_context_current(window)
    glClearColor(1,0,0,0)
    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        glfw.swap_buffers(window)
    glfw.terminate()

if __name__=="__main__":
    main()