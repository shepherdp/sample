from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class NGUI:

    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Social Network Evolution Engine")

        self.graph = None
        self.fig = None
        self.ax = None
        self.canvas = None
        self.points = None
        self.pos = None
        self.posvals = None
        self.x, self.y = list(), list()
        self.texts, self.lines = list(), dict()
        self.drawing = False
        self.numsteps = 0
        self.clearflag = False

        # START OF GRAPH TAB AND PLOT INITIATION

        self.status = tk.Label(self.statusframe, text='Ready for a command!', fg='green')
        self.status.grid(padx=10, pady=10)

        self.plotframe = tk.LabelFrame(self.graphtab, padx=5, pady=5, text="Social Network Simulation Graph", bg="White")
        self.plotframe.grid(padx=5, pady=5, row=0, column=1, rowspan=3)

        self.init_plot()

        # Simulation Parameters Tab initiation code

        self.root.mainloop()




    def init_plot(self):
        """This initializes the plot setup in the constructor and allos plotting, graphing, animating, and other plotting/graphing functions."""

        self.fig = Figure(figsize=(8, 6), dpi=100)
        self.ax = self.fig.add_subplot(111)

        self.ax.set_xticks([])
        self.ax.set_yticks([])

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plotframe)  # A tk.DrawingArea.
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(self.canvas, self.plotframe)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    
    def plot_network(self):

        # If there are no dots on the screen
        if self.points is None:
            self.points = self.ax.scatter(*self.pos.T, s=350, alpha=.5, c=colors)

            # Draw edges
            for (u, v) in self.graph._graph.edges(): #Update this if to be clean, no longer need to check inverse
                line, = self.ax.plot([self.pos[u][0],self.pos[v][0]],[self.pos[u][1],self.pos[v][1]],'k',alpha=0.25,label=f'({u},{v})')

        else:
            # Adjust positions of nodes
            self.points.set_offsets(np.c_[self.pos.T[0], self.pos.T[1]])
            # Adjust color of nodes
            self.points.set_color(colors)

        # Set axis limits
        self.ax.set_xlim([-1.1, 1.1])
        self.ax.set_ylim([-1.1, 1.1])
        
        # Draw any updates to the canvas
        self.canvas.draw()
    
    def clear(self):
        """
        Clear the plot and all class attributes associated with it.
        :return: None
        """
        if self.drawing:
            self.drawing = False
        self.ax.clear()
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.canvas.draw()
        self.graph = None
        self.x, self.y = None, None
        self.texts = list()
        self.points = None
        self.lines = dict()
        self.pos = None
        self.posvals = None
        self.numsteps = 0
        self.clearflag = True
        self.set_status('Graph cleared.', 'green')

    def advance(self):
        """
        :return:
        """

        if self.graph is not None:
            self.graph.update()
            self.plot_network()
        else:
            self.set_status('No active network!', 'red')

    
    def init_animation(self):
        """
        :return:
        """
        self.drawing = True
        self.animate()
        self.root.update()

    def animate(self):
        """
        :return:
        """
        if self.graph is None and not self.clearflag:
            self.set_status('No graph to animate!', 'red')
            return

        self.clearflag = False
        speed = self.vals['speed_in']
        if self.drawing:
            self.advance()
            if speed == 'Slow':
                self.root.after(1000, self.animate)
            elif speed == 'Normal':
                self.root.after(500, self.animate)
            elif speed == 'Fast':
                self.root.after(100, self.animate)

    def stop_animation(self):
        """
        :return:
        """
        self.drawing = False


def main():
    NGUI()


main()
