from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow
from plotly.graph_objects import Figure, Scatter, Layout
import plotly

import numpy as np


class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        # some example data
        x = ['day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'today']
        y = [0, 0, 0, 0, 0, 0, 0]

        # create the plotly figure
        fig = Figure(data=Scatter(x=x, y=y), layout = Layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
            ))
        fig.update_xaxes(showline=True, linewidth=2, linecolor='white', gridcolor='Red')
        fig.update_yaxes(showline=True, linewidth=2, linecolor='white', gridcolor='Red')

        # we create html code of the figure
        html = '<html><body style="background:black;">'
        html += plotly.offline.plot(fig, output_type='div', include_plotlyjs='cdn')
        html += '</body></html>'

        # we create an instance of QWebEngineView and set the html code
        plot_widget = QWebEngineView()
        plot_widget.setHtml(html)

        # set the QWebEngineView instance as main widget
        self.setCentralWidget(plot_widget)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()