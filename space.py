import pyautogui
import time

time.sleep(3)

for i in range(500):
	pyautogui.typewrite(["space"])


#Used JS Code in Console to equal highlighted word in page, then looped space  in python
#$( "#inputfield​" ).keyup(function() { $("#inputfield​").val( $(".highlight").text() )});
	
