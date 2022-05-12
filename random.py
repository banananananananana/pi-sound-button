from pypsexec.client import Client
import random

audio_clips = ['pi1.wav', 'pi2.wav', 'pi3.wav']
random_clip = (random.choice(audio_clips))
print(random_clip)

server = "192.168.90.121"
username = "dinmor"
password = "ernice"
executable = "powershell"
arguments = f"(New-Object Media.SoundPlayer {random_clip} ).PlaySync()"

c = Client(server, username=username, password=password, encrypt=True)

c.connect()
try:
    c.create_service()
    result = c.run_executable(executable, arguments=arguments, working_dir="C:\pi_sound_button")
finally:
    c.remove_service()
    c.disconnect()

print("STDOUT:\n%s" % result[0].decode('utf-8') if result[0] else "")
print("STDERR:\n%s" % result[1].decode('utf-8') if result[1] else "")
print("RC: %d" % result[2])
