import time
from toDo import response
from toDo import seslendirme
from toDo import record

seslendirme("Merhaba nasıl yardımcı olabilirim")


time.sleep(1)
while 1:
    voice=record()
    print(voice)
    response(voice)
    
   

    