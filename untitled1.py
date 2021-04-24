# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 18:29:33 2021

@author: sisi
"""

import glassdoor_scraper as gs

paths = "C:/Users/sisi/Documents/ds_salary_coco/chromedriver.exe"

df = gs.get_jobs('data scientist',15, False, paths, 15)