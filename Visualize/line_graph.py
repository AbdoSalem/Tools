from Visualize import init
import matplotlib.pyplot as plt

def draw_line_graph(xs,ys,ys1=None,xlabel = None,ylabel = None,ylabel1=None,lines_label=[],lines_label1=[],pdf_dir=None,show = False):
    fig,ax = init(plt.rcParams.get('figure.figsize'))
    if ys1:
        ax1 = ax.twinx()

    if not isinstance(ys[0], list):
        ax.plot(xs, ys, label=lines_label if lines_label else 'f(x)')
    else:
        for i,ysi in enumerate(ys):
            ax.plot(xs, ysi,label=lines_label[i] if lines_label else r'$f_{%s}i(x)$'%i)
    if ys1 and ax1:
        if not isinstance(ys1[0], list):
            ax1.plot(xs, ys1, label=lines_label1 if lines_label1 else r'f^{2}(x)')
        else:
            for i, ysi in enumerate(ys1):
                ax1.plot(xs, ysi, label=lines_label1[i] if lines_label1 else r'$f^{2}_{%s}i(x)$' % i)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
        if ys1:
            ax1.set_ylabel(ylabel1)

    ax.legend(loc='upper left')
    ax1.legend(loc='upper right')
    if(pdf_dir):
        plt.savefig(pdf_dir, format='pdf')
    if show:
        plt.show()


draw_line_graph([0,1,2,3,4],[[0,1,2,3,4],[0,1,4,9,16]],ys1=[160,90,40,10,0],xlabel='X',ylabel='Y',ylabel1='Y2',lines_label=['Y=X',r'$Y=X^2$'],lines_label1=r'Y=10X',show=True)