import pyautogui as agui
agui.PAUSE=1
agui.FAILSAFE=True
print('Press Ctrl+C to quit...!!!')

try:
    while True:
        x,y=agui.position()
        positionStr='X: '+str(x).rjust(4)+' Y: '+str(y).rjust(4)
        print(positionStr,end='')
        print('\b'*len(positionStr),end='',flush=True)

except KeyboardInterrupt:
    print('\nDone')
