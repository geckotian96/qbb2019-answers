#!/bin/bash

grep "SRR072893" SRR072893.sam | cut -f 3 | sort | uniq -c > sorted.SRR072893.sam 


##this codei is from the presenter's code


