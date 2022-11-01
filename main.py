from kivy.lang import Builder
import requests
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker, MDTimePicker

KV = '''
MDFloatLayout:
    MDRaisedButton:
        text: "Schedule"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_date_picker()
    MDRaisedButton:
        text: "Open date picker"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_date_picker()
    MDRaisedButton:
        text: "Open time picker"
        pos_hint: {'center_x': .5, 'center_y': 0.4}
        on_release: app.show_time_picker()
    MDRaisedButton:
        text: "List available time slots for chosen day"
        pos_hint: {'center_x': .5, 'center_y': 0.3}
        on_release: app.show_time_picker()
    MDRaisedButton:
        text: "List available time slots for chosen month"
        pos_hint: {'center_x': .5, 'center_y': 0.2}
        on_release: app.thishastobedone()
    MDRaisedButton:
        text: "Book Appointment"
        pos_hint: {'center_x': .5, 'center_y': 0.1}
        on_release: app.thishastobedone()
'''


class Test(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)
    def show_time_picker(self, *args):
        '''Open time picker dialog.'''

        MDTimePicker().open()
    def get_time(self, instance, time):
     '''
     The method returns the set time.

      :type instance: <kivymd.uix.picker.MDTimePicker object>
     :type time: <class 'datetime.time'>
       '''
     return time     
    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''


        values: str = str(value)
        values2 = values.split('-')
        global year1
        global month1
        global day1
        year1 = values2[0]
        month1 = values2[1]
        day1 = values2[2]
        print(year1)
        print(month1)
        print(day1)

    def thishastobedone():
        getDaysAvaliableDays(month1,year1)
    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
def getDaysAvaliableDays(month: str, year: str):
    URL = 'http://129.146.242.239:8080/days?' + 'year=' + year + '&month' + month
    r = requests.get(url=URL, params={'month': month})

    return r

def getTimeSlots(year: str, month: str, day: str):
    URL = 'http://129.146.242.239:8080/timeslots?' + 'year=' + year + '&month=' + month + '&day=' + day
    r = requests.get(url=URL, params={
        'month': month,
        'day': day
    })

def addTimeSlot(year: str, month: str, day: str, hour: str, minute: str):
    URL = 'http://129.146.242.239:8080/book?' + 'year=' + year + '&month=' + month + '&day=' + day + '&hour=' + hour + '&minute=' + minute
    r = requests.post(url=URL, params={
        'year': year,
        'month': month,
        'day': day,
        'hour': hour,
        'minute': minute
    })
Test().run()