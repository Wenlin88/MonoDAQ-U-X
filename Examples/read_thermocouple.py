from isotel.idm import gateway, monodaq
import pickle
from pathlib import Path

# For quick access; remote ip adress; username and password is stored at little.secrets pickle. Note! Newer use donwloaded pickle. It can be hacked!
little_secrets = pickle.load(open(str(Path.home()) + "/little.secrets", "rb" ) )
remote_ip = little_secrets["remote_ip"]
user = little_secrets["user"]
passwd = little_secrets["password"]

# connect to some remote host
mdu = monodaq.MonoDAQ_U( gateway.Group('http://' + remote_ip + ':33000',
                                        username=user,
                                        password=passwd) )


# HW setup --> K type Thermocouple at pins 5 and 6
mdu.reset()
mdu.__dir__()
mdu.name
print(mdu.get_device_status())
mdu['ch.function.function4'] = "Thermocouple"

mdu.wait4ready()
mdu['ch.value.value4']
