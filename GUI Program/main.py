"""
Main File, initiates and creates the necessary objects required. 
"""

import window as w
import mainScreen as ms
import portcom as pc


port_manager = pc.PortCom()
windowobj = w.Window()

main_frame = ms.MainScreen(windowobj.window, serial=port_manager)

windowobj.window.mainloop()