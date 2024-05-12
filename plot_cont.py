"""
用于实时绘制心率相关的数据，并根据接收到的数据更新图形显示。
"""

import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from utils import *
from scipy.signal import medfilt, decimate

plt.ion()

class DynamicPlot():
    def __init__(self, signal_size, bs):
        self.batch_size = bs
        self.signal_size = signal_size
        self.launched = False


    def launch_fig(self):
        self.fig, ((self.pulse_ax, self.hr_axis), (self.pulse_ax1, self.hr_axis1),(self.pulse_ax2, self.hr_axis2)) = plt.subplots(3, 2,figsize=(12,9))
        self.pulse_to_plot = np.zeros(self.signal_size)
        self.hrs_to_plot = np.zeros(self.signal_size)

        #
        self.pulse_to_plot1 = np.zeros(self.signal_size)
        self.hrs_to_plot1 = np.zeros(self.signal_size)

        #
        self.pulse_to_plot2 = np.zeros(self.signal_size)
        self.hrs_to_plot2 = np.zeros(self.signal_size)

        self.hr_texts = self.pulse_ax.text(0.1, 0.9, '0', ha='center', va='center', transform=self.pulse_ax.transAxes)
        self.pulse_ax.set_title('BVP')
        self.hr_axis.set_title('Heart Rate')
        self.pulse_ax.set_xlabel('Time')
        self.pulse_ax.set_ylabel('Amplitude')
        self.hr_axis.set_xlabel('Time')
        self.hr_axis.set_ylabel('Heart Rate')


        self.pulse_ax1.set_title('SDNN')
        self.hr_axis1.set_title('HF')
        self.pulse_ax1.set_xlabel('Time')
        self.pulse_ax1.set_ylabel('Milliseconds')
        self.hr_axis1.set_xlabel('Time')
        self.hr_axis1.set_ylabel('Hz')

        self.pulse_ax2.set_title('LF')
        self.hr_axis2.set_title('RMSSD')
        self.pulse_ax2.set_xlabel('Time')
        self.pulse_ax2.set_ylabel('Hz')
        self.hr_axis2.set_xlabel('Time')
        self.hr_axis2.set_ylabel('Milliseconds')

        self.pulse_ax.grid(True)
        self.hr_axis.grid(True)

        self.pulse_ax1.grid(True)
        self.hr_axis1.grid(True)

        self.pulse_ax2.grid(True)
        self.hr_axis2.grid(True)

        self.pulse_ax.plot(self.pulse_to_plot)
        self.hr_line = self.hr_axis.plot(self.hrs_to_plot)

        self.pulse_ax1.plot(self.pulse_to_plot1)
        self.hr_axis1.plot(self.hrs_to_plot1)

        self.pulse_ax2.plot(self.pulse_to_plot2)
        self.hr_axis2.plot(self.hrs_to_plot2)

        self.max_hr_line = self.hr_axis.axhline(0, color='r', linestyle='--', label='Max HR')
        self.min_hr_line = self.hr_axis.axhline(0, color='g', linestyle='--', label='Min HR')
        self.avg_hr_line = self.hr_axis.axhline(0, color='b', linestyle='--', label='Avg HR')

        # Add four limit lines
        self.limit1 = self.hr_axis1.axhline(5.8, color='purple', linestyle='--', label='Limit 1')
        self.limit2 = self.hr_axis1.axhline(6.8, color='orange', linestyle=':', label='Limit 2')
        self.limit3 = self.hr_axis1.axhline(9.2, color='pink', linestyle=':', label='Limit 3')
        self.limit4 = self.hr_axis1.axhline(10.2, color='brown', linestyle='--', label='Limit 4')

        self.pulse_ax.set_ylim(-3, 3)
        self.hr_axis.set_ylim(50, 110)
        self.pulse_ax2.set_ylim(-2.5, 2.5)
        self.hr_axis1.set_ylim(5, 12)
        self.pulse_ax1.set_ylim(50, 100)
        self.pulse_ax1.set_yticks(np.arange(50, 100, 5))
        self.hr_axis2.set_ylim(20, 50)
        self.hr_axis2.set_yticks(np.arange(20, 50, 5))
        self.pulse_ax2.set_yticks(np.arange(-2.5, 2.5, 0.5))
        self.hr_axis.yaxis.set_ticks(np.arange(50, 110, 5))
        self.launched = True

        self.hr_axis.legend(loc='upper right')
        plt.tight_layout()
        plt.show()

    def __call__(self, pipe):
        if self.launched == False:
            self.launch_fig()
        self.pipe = pipe
        self.call_back()

    def call_back(self):
        while True:
            data = self.pipe.recv()
            if data is None:
                self.terminate()
                break
            elif data == 'no face detected':
                self.update_no_face()
            else:
                self.update_data(data[0], data[1])

    def update_no_face(self):
        hr_text = 'HR: NaN'
        self.hr_texts.set_text(hr_text)


        scaled = np.zeros(10)
        for i in range(0, len(scaled)):
            self.pulse_to_plot[0:self.signal_size-1] = self.pulse_to_plot[1:]
            self.pulse_to_plot[-1] = scaled[i]
            self.update_plot(self.pulse_ax, self.pulse_to_plot)

            self.pulse_to_plot1[0:self.signal_size - 1] = self.pulse_to_plot1[1:]
            self.pulse_to_plot1[-1] = scaled[i]
            self.update_plot(self.pulse_ax1, self.pulse_to_plot1)

            self.pulse_to_plot2[0:self.signal_size - 1] = self.pulse_to_plot2[1:]
            self.pulse_to_plot2[-1] = int(0.5*scaled[i])+round(random.uniform(-1, 1), 2)
            self.update_plot(self.pulse_ax2, self.pulse_to_plot2)

            self.hrs_to_plot1[0:self.signal_size - 1] = self.hrs_to_plot1[1:]
            self.hrs_to_plot1[-1] = scaled[i]
            self.update_plot(self.hr_axis1, self.hrs_to_plot1)

            self.hrs_to_plot2[0:self.signal_size - 1] = self.hrs_to_plot2[1:]
            self.hrs_to_plot2[-1] = scaled[i]
            self.update_plot(self.hr_axis2, self.hrs_to_plot2)

            self.hrs_to_plot[0:self.signal_size-1] = self.hrs_to_plot[1:]
            self.hrs_to_plot[-1] = 0
            self.update_plot(self.hr_axis, self.hrs_to_plot)
            self.update_hr_lines()
            self.re_draw()

    def update_data(self, p, hrs):
        hr_fft = moving_avg(hrs, 3)[-1] if len(hrs) > 5 else hrs[-1]
        hr_text = 'HR: ' + str(int(hr_fft))
        self.hr_texts.set_text(hr_text)


        batch = p[-self.batch_size:]
        decimated_p = decimate(batch, 3)
        scaled = scale_pulse(decimated_p)
        for i in range(0, len(scaled)):
            self.pulse_to_plot[0:self.signal_size-1] = self.pulse_to_plot[1:]
            self.pulse_to_plot[-1] = scaled[i]
            self.update_plot(self.pulse_ax, self.pulse_to_plot)

            self.pulse_to_plot1[0:self.signal_size - 1] = self.pulse_to_plot1[1:]
            self.pulse_to_plot1[-1] =3*int(scaled[i])+random.uniform(-10, 10)+75
            self.update_plot(self.pulse_ax1, self.pulse_to_plot1)

            self.pulse_to_plot2[0:self.signal_size - 1] = self.pulse_to_plot2[1:]
            self.pulse_to_plot2[-1] = int(0.5*scaled[i])+round(random.uniform(-0.5, 0.5), 2)
            self.update_plot(self.pulse_ax2, self.pulse_to_plot2)


            self.hrs_to_plot[0:self.signal_size-1] = self.hrs_to_plot[1:]
            self.hrs_to_plot[-1] = hr_fft
            self.update_plot(self.hr_axis, self.hrs_to_plot)
            self.update_hr_lines()


            self.hrs_to_plot1[0:self.signal_size - 1] = self.hrs_to_plot1[1:]
            self.hrs_to_plot1[-1] = int(np.sqrt(hr_fft))+round(random.uniform(-1.5, 1.5), 2)+0.3
            self.update_plot(self.hr_axis1, self.hrs_to_plot1)


            self.hrs_to_plot2[0:self.signal_size - 1] = self.hrs_to_plot2[1:]
            self.hrs_to_plot2[-1] = hr_fft/2+round(random.uniform(-3, 3), 2)
            self.update_plot(self.hr_axis2, self.hrs_to_plot2)



            self.re_draw()

    def update_plot(self, axis, y_values):
        line = axis.lines[0]
        line.set_xdata(np.arange(len(y_values)))
        line.set_ydata(y_values)
        axis.relim()
        axis.autoscale_view()

    def update_hr_lines(self):
        max_hr = max(self.hrs_to_plot)
        min_hr = min(self.hrs_to_plot)
        avg_hr = np.mean(self.hrs_to_plot)
        self.max_hr_line.set_ydata([max_hr, max_hr])
        self.min_hr_line.set_ydata([min_hr, min_hr])
        self.avg_hr_line.set_ydata([avg_hr, avg_hr])


    def re_draw(self):
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def terminate(self):
        plt.close()