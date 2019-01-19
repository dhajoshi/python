#!/usr/bin/env python

import re

upper_check = r'.*([A-Z].*){2,}'                         ## 2 Upper case in string
digit_check = r'.*([0-9].*){3,}'                         ## 3 Digits in string
alphanumeric_and_length_check = r'([A-Za-z0-9]){10}$'    ## Exactly 10 char and no special char
repeat_check = r'.*(.).*\1'                              ## Repeate check
