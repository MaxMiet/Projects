using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Runtime.InteropServices;
//using System.Timers;

namespace Sleepify
{
    public partial class Form1 : MetroFramework.Forms.MetroForm
    {
        private int hours;
        private int minutes;
        private int seconds;
        private int trig = 0;

        public const int KEYEVENTF_EXTENTEDKEY = 1;
        public const int KEYEVENTF_KEYUP = 0;
        public const int VK_MEDIA_NEXT_TRACK = 0xB0;// code to switch to next song
        public const int VK_MEDIA_PLAY_PAUSE = 0xB3;// code to play or pause a song
        public const int VK_MEDIA_PREV_TRACK = 0xB1;// code to switch to prev song

        [DllImport("user32.dll")]
        public static extern void keybd_event(byte virtualKey, byte scanCode, uint flags, IntPtr extraInfo);

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            mLabelH.Font = new System.Drawing.Font(mLabelH.Font.Name, 10F);
            mLabelM.Font = new System.Drawing.Font(mLabelM.Font.Name, 10F);
            mLabelS.Font = new System.Drawing.Font(mLabelS.Font.Name, 10F);

        }

        private void metroButton1_Click(object sender, EventArgs e)
        {
            hours = Convert.ToInt32(Math.Round(numericUpDown1.Value, 0));
            minutes = Convert.ToInt32(Math.Round(numericUpDown2.Value, 0));
            seconds = Convert.ToInt32(Math.Round(numericUpDown3.Value, 0));

            mLabelH.Text = hours.ToString();
            mLabelM.Text = minutes.ToString();
            mLabelS.Text = seconds.ToString();
            if (trig == 0)
            {
                timer1 = new Timer();
                timer1.Tick += new EventHandler(timer1_Tick);
                timer1.Interval = 1000; // 1 sec
                trig = 1;
                //timer1.Start();
            }
            timer1.Start();
        }

        private void metroButton2_Click(object sender, EventArgs e)
        {
            timer1.Stop();
            hours = 0;
            minutes = 0;
            seconds = 0;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //verify if the time passed or not
            if ((minutes == 0) && (hours == 0) && (seconds == 0))
            {
                //if the time is done, reset all settings and fields
                //show the message, notifying that the time is over
                //timer1.Enabled = false;
                timer1.Stop();
                keybd_event(VK_MEDIA_PLAY_PAUSE, 0, KEYEVENTF_EXTENTEDKEY, IntPtr.Zero);
                MessageBox.Show("Music has been paused.", "Sleepify");
                numericUpDown1.Value = 0;
                numericUpDown2.Value = 0;
                numericUpDown3.Value = 0;

            }
            else
            {
                //else continue counting.
                if (seconds < 1)
                {
                    seconds = 59;
                    if (minutes == 0)
                    {
                        minutes = 59;
                        if (hours != 0)
                            hours -= 1;

                    }
                    else
                    {
                        minutes -= 1;
                    }
                }
                else
                    seconds -= 1;
                //display the current values of hours, minutes and seconds in
                //the corresponding fields
                mLabelH.Text = hours.ToString();
                mLabelM.Text = minutes.ToString();
                mLabelS.Text = seconds.ToString();
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Have your music already playing when pressing Start.", "Basiq:");
        }
    }
}
