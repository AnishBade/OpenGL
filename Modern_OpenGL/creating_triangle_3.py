
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy 

def main():
    #initialize glfw
    if not glfw.init():
        return

    #create glfw window
    window=glfw.create_window(1200,1000,"My OpenGL Wingow",None,None)
    
    if not window:
        glfw.terminate()
        return
    
    glfw.make_context_current(window)
    triangle = [-0.5, -0.5, 0.0,
                 0.5, -0.5, 0.0,    
                 0.0,  0.5, 0.0]
    triangle = numpy.array(triangle, dtype = numpy.float32)
    vertex_shader="""
    #version 330
    in vec4 position;

    void main(){
        gl_Position=position;
    }
    """
    fragment_shader="""
    #version 330
    void main(){
        gl_FragColor=vec4(1.0f,0.0f,0.0f,1.0f);
    }
    """
    shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
                                              OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))
    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, 36, triangle, GL_STATIC_DRAW)

    position = glGetAttribLocation(shader, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 0,None)
    glEnableVertexAttribArray(position)

    # color = glGetAttribLocation(shader, "color")
    # glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    # glEnableVertexAttribArray(color)


    glUseProgram(shader)

    glClearColor(0.2,0.3,0.2,1.0)
    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)
        glDrawArrays(GL_TRIANGLES, 0, 3)

        glfw.swap_buffers(window)
    glfw.terminate()

if __name__=="__main__":
    main()