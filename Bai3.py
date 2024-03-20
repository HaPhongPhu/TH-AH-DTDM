# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def button_1_click(self, **event_args):
    try:
        numbers = [int(x) for x in self.text_box_1.text.split()]
        self._merge_sort(numbers)
        self.label_1.text = "Sorted numbers: " + ' '.join(map(str, numbers))
    except ValueError:
        self.label_1.text = "Error: Please enter integers separated by spaces"

def _merge_sort(self, arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        self._merge_sort(L)
        self._merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Run the app
if __name__ == '__main__':
    app = Form1()
    app.show()
