import glfw

def main():
    if not glfw.init():
        return
    
    window=glfw.create_window(1000,1000,"My OpenGL Window",None,None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    while not glfw.window_should_close(window):
        glfw.poll_events()
        glfw.swap_buffers(window)
    glfw.terminate()
if __name__=="__main__":
    main()