#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 18:40:52 2023

@author: mattfariselli

This contains the methods for standard UI elements.
"""
import tkinter as tk

class standard_textbox:
    def __init__(self, frame, row, column, span):
        text = tk.Text(frame,
                         height = .1,
                         width = 10)
        
        text.grid(column = column, 
                    row = row, 
                    sticky = 'EW', 
                    padx=5, 
                    pady=5, 
                    columnspan=span)


class standard_button:
    def __init__(self, frame, text, command, row, column, span):
        button = tk.Button(frame,
                           text = text,
                           highlightbackground = 'gray',
                           command = command)
        
        button.grid(column = column, 
                    row = row, 
                    sticky = 'NESW', 
                    padx=5, 
                    pady=5, 
                    columnspan=span)
        
        

class standard_label:
    def __init__(self, frame, text, row, column, span=1, anchor = 'w', justify='left'):
        label = tk.Label(frame,
                       text = text,
                       anchor = anchor,
                       justify = justify)
            
        label.grid(column = column, 
                  row = row, 
                  sticky = 'EW', 
                  padx=5, 
                  pady=5, 
                  columnspan=span)