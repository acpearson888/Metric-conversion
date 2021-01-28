# Andrew's program for calculating dilutions.

## Supported units:

1. g/l (mass/volume)
2. U/l (units/volume)
3. M (molarity)
4. % (mass percentage)
5. ppt, ppm, ppb (parts per thousand, million, and billion)

## Usage
Run the python script
```
$ python3 metric.py
```
Answer the questions regarding concentration in the format "## unit" (space between number and unit)
Example: 
```
$ python3 metric.py 
What is your starting concentration? (## units): 10 mM
What is your desired concentration? (## units): 15 fM

Start: 0.01 M
1:100 x5
1:66.66666666666666666666666667
End: 1.5E-14 M
Thanks!

Go again?(y/n) n
All done!
```

Hope this is helpful!
